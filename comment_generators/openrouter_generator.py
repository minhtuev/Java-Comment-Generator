from comment_generators.base_generator import BaseCommentGenerator
import requests

class OpenRouterCommentGenerator(BaseCommentGenerator):
    def __init__(self, token, model=None):
        if not model:
            raise ValueError("❌ No model specified. Please pass --model or set MODEL in .env")

        self.api_key = token
        self.model = model
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self._validate_model()

    def _validate_model(self):
        print("🔎 Fetching model list from OpenRouter...")
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        try:
            response = requests.get("https://openrouter.ai/api/v1/models", headers=headers)
            response.raise_for_status()
            models_response = response.json()
            available_models = [m["id"] for m in models_response.get("data", [])]
        except Exception as e:
            raise RuntimeError(f"❌ Failed to fetch model list from OpenRouter: {e}")

        if self.model not in available_models:
            raise ValueError(
                f"❌ Model '{self.model}' not found on OpenRouter.\n"
                f"🧠 Available models include:\n  " +
                "\n  ".join(sorted(available_models[:10])) + "\n  ..."
            )

    def _query_llm(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://yourdomain.com",  # optional
            "X-Title": "CodeComprehender"
        }
        body = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3
        }

        response = requests.post(self.api_url, headers=headers, json=body)

        if response.status_code != 200:
            print(f"❌ OpenRouter Error ({response.status_code}):")
            print(response.text)
            response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]

    def generate_class_comment(self, class_name, indent, access_modifier, class_body):
        java_code = "".join(class_body)
        prompt = (
            f"You're an expert Java developer. Write a concise comment describing the purpose of this {access_modifier} class named `{class_name}`:\n\n"
            f"{java_code}\n\n"
            "Use 1-2 lines only."
        )
        comment_text = self._query_llm(prompt)
        return [f"{indent}/**\n"] + [f"{indent} * {line.strip()}\n" for line in comment_text.splitlines()] + [f"{indent} */\n"]

    def generate_method_comment(self, method_name, indent, access_modifier, method_body):
        java_code = "".join(method_body)
        prompt = (
            f"You're an expert Java developer. Write a short comment describing what this {access_modifier} method `{method_name}` does:\n\n"
            f"{java_code}\n\n"
            "Respond in one line."
        )
        comment_text = self._query_llm(prompt)
        return f"{indent}// {comment_text.strip()}\n"
