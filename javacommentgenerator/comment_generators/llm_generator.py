from abc import ABC, abstractmethod
from .base_generator import BaseCommentGenerator


class LLMCommentGenerator(BaseCommentGenerator):
    def __init__(self, token, model, max_tries=3):
        self.token = token
        self.model = model
        self.max_tries = max_tries

    @abstractmethod
    def _query_llm(self, prompt):
        raise NotImplementedError

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

    def generate_class_comment(self, class_name, indent, access_modifier, class_body):
        prompt = self._build_class_prompt(class_name, access_modifier, class_body)
        for i in range(self.max_tries):
            try:
                comment_text, dependencies = self._query_llm(prompt, expect_json=True)
                comment_lines = [f"{indent}/**\n"] + [f"{indent} * {line.strip()}\n" for line in comment_text.splitlines()] + [f"{indent} */\n"]
                return comment_lines, dependencies
            except Exception as ex:
                print("Encoutering exception, will retry: ", ex)
        return [], []

    def generate_method_comment(self, method_name, indent, access_modifier, method_body):
        prompt = self._build_method_prompt(method_name, access_modifier, method_body)
        for i in range(self.max_tries):
            try:
                comment_text, _ = self._query_llm(prompt, expect_json=False)
                comment_line = f"{indent}// {comment_text.strip()}\n"
                return comment_line, []
            except Exception as ex:
                print("Encoutering exception, will retry: ", ex)
        return [], []

