from comment_generators.base_generator import BaseCommentGenerator
from pprint import pprint

class DefaultCommentGenerator(BaseCommentGenerator):
    def generate_class_comment(self, class_name, indent, access_modifier, class_body):
        print(f"🔍 Detected class: {class_name}")
        pprint(class_body)
        return [
            f"{indent}/**\n",
            f"{indent} * {access_modifier.title()} class `{class_name}` defines the main structure and logic for this component.\n",
            f"{indent} */\n"
        ]

    def generate_method_comment(self, method_name, indent, access_modifier, method_body):
        print(f"🔍 Detected method: {method_name}")
        pprint(method_body)
        return f"{indent}// {access_modifier.title()} method `{method_name}` performs a specific task\n"
