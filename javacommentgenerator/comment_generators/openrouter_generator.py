import requests
import json
from .llm_generator import LLMCommentGenerator


class OpenRouterCommentGenerator(LLMCommentGenerator):
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
