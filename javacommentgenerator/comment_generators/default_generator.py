from .base_generator import BaseCommentGenerator
from pprint import pprint

class DefaultCommentGenerator:
    def __init__(self):
        self.known_classes = set()

    def generate_class_comment(self, class_name, indent, access_modifier, class_body):
        print(f"Detected class: {class_name}")
        self.known_classes.add(class_name)
        dependencies = self._detect_dependencies(class_body)

        comment = [
            f"{indent}/**\n",
            f"{indent} * {access_modifier.title()} class `{class_name}` defines the main structure and logic for this component.\n",
            f"{indent} */\n"
        ]
        return comment, dependencies

    def generate_method_comment(self, method_name, indent, access_modifier, method_body):
        print(f"Detected method: {method_name}")
        comment = f"{indent}// {access_modifier.title()} method `{method_name}` performs a specific task\n"
        return comment, []  # No method-level dependencies

    def _detect_dependencies(self, body_lines):
        deps = set()
        for line in body_lines:
            for class_name in self.known_classes:
                if class_name in line and not line.strip().startswith("//"):
                    deps.add(class_name)
        return list(deps)
