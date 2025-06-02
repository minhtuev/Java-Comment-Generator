import json
import openai
from .llm_generator import LLMCommentGenerator


class OpenAICommentGenerator(LLMCommentGenerator):
    def __init__(self, token, model="gpt-4"):
        super().__init__(token, model)
        openai.api_key = token
        self.client = openai.OpenAI(api_key=token)

    def _query_llm(self, prompt, expect_json=False):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        content = response.choices[0].message.content.strip()
        content = self._process_artifacts(content)

        if expect_json:
            data = json.loads(content)
            return data["comment"], data.get("dependencies", [])
        else:
            return content.strip(), []
