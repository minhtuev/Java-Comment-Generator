import requests
import json

class OpenRouterCommentGenerator:
    def __init__(self, token, model):
        self.token = token
        self.model = model
        self._validate_model()

    def _validate_model(self):
        try:
            print("🔎 Fetching model list from OpenRouter...")
            response = requests.get(
                "https://openrouter.ai/api/v1/models",
                headers={"Authorization": f"Bearer {self.token}"}
            )
            response.raise_for_status()
            models = response.json()
            available_models = [m["id"] for m in models.get("data", [])]
            if self.model not in available_models:
                raise ValueError(f"❌ Model `{self.model}` not available on OpenRouter.")
        except Exception as e:
            raise RuntimeError(f"❌ Failed to fetch model list from OpenRouter: {e}")

    def generate_class_comment(self, class_name, indent, access_modifier, class_body):
        prompt = self._build_class_prompt(class_name, access_modifier, class_body)
        try:
            comment_text, dependencies = self._query_llm(prompt, expect_json=True)
        except Exception as ex:
            print("Exception: ", ex)
            return [], []

        comment_lines = [f"{indent}/**\n"] + [f"{indent} * {line.strip()}\n" for line in comment_text.splitlines()] + [f"{indent} */\n"]
        return comment_lines, dependencies

    def generate_method_comment(self, method_name, indent, access_modifier, method_body):
        prompt = self._build_method_prompt(method_name, access_modifier, method_body)
        try:
            comment_text, _ = self._query_llm(prompt, expect_json=False)
        except Exception as ex:
            print("Exception: ", ex)
            return [], []

        comment_line = f"{indent}// {comment_text.strip()}\n"
        return comment_line, []

    def _build_class_prompt(self, class_name, access_modifier, class_body):
        body_str = "\n".join(class_body)
        return f"""You are an expert Java developer.

Given the following Java class named `{class_name}` (access: {access_modifier}), do two things:
1. Write a concise comment for the class, do not include any code or quotes in the documentation, one or two lines.
2. Compute class-level dependencies of this class.

Return a JSON object with:
  - `comment`: the concise comment, one or two lines. Only return the comment. Do not include code or quotes.
  - `dependencies`: list of other class names used in this class (e.g., via instantiation, method calls, inheritance, etc).

Example output:
{{
  "comment": "This class is responsible for greeting users and depends on HelloWorld.",
  "dependencies": ["HelloWorld"]
}}

Class code:
{body_str}
"""

    def _build_method_prompt(self, method_name, access_modifier, method_body):
        body_str = "\n".join(method_body)
        prompt = (
            f"You're an expert Java developer. Write a short comment describing what this {access_modifier} method `{method_name}` does:\n\n"
            f"{body_str}\n\n"
            "Respond in one line."
        )
        return prompt

    def _query_llm(self, prompt, expect_json=True):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "HTTP-Referer": "https://openrouter.ai",  # optional for usage tracking
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=json.dumps(payload)
        )
        response.raise_for_status()

        content = response.json()["choices"][0]["message"]["content"]

        if expect_json:
            # clean out triple backticks or language tags if present
            if content.startswith("```"):
                content = content.strip().strip("```").strip("json").strip()
            data = json.loads(content)
            return data["comment"], data.get("dependencies", [])
        else:
            return content.strip(), []
