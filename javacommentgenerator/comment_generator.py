import javalang
import re
from .utils import get_access_modifier, extract_block
from .comment_generators.default_generator import DefaultCommentGenerator
from .comment_generators.openrouter_generator import OpenRouterCommentGenerator


def get_method_names_from_tree(tree):
    method_names = set()
    for _, node in tree.filter(javalang.tree.MethodDeclaration):
        method_names.add(node.name)
    return method_names


def make_method_regex(method_names):
    if not method_names:
        return None
    return re.compile(r'\b(' + '|'.join(re.escape(name) for name in method_names) + r')\b')


def generate_comments(filepath, tree, generator):
    with open(filepath, 'r') as f:
        original_lines = f.readlines()
        java_code = ''.join(original_lines)

    parsed_tree = javalang.parse.parse(java_code)
    method_names = get_method_names_from_tree(parsed_tree)
    method_regex = make_method_regex(method_names)

    commented_lines = []
    class_info = {
        "name": None,
        "methods": [],
        "dependencies": []
    }

    i = 0
    while i < len(original_lines):
        line = original_lines[i]
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)].rstrip("\n")
        tokens = stripped.split()

        # Detect class
        if "class" in tokens:
            class_index = tokens.index("class")
            class_name = tokens[class_index + 1].split("{")[0]
            access_modifier = get_access_modifier(tokens)
            class_info["name"] = class_name

            class_block, offset = extract_block(original_lines, i)
            comment, dependencies = generator.generate_class_comment(
                class_name, indent, access_modifier, class_block
            )
            class_info["dependencies"].extend(dependencies)

            commented_lines.extend(comment)
            commented_lines.append(line)
            i += 1
            continue

        # Detect method declaration (void or non-void) using method name
        if method_regex and method_regex.search(line) and "(" in line and "class" not in tokens:
            try:
                method_name = method_regex.search(line).group(1)
                access_modifier = get_access_modifier(tokens)
                class_info["methods"].append(f"{access_modifier} {method_name}()")

                method_block, offset = extract_block(original_lines, i)
                comment, _ = generator.generate_method_comment(
                    method_name, indent, access_modifier, method_block
                )
                commented_lines.append(comment)
                commented_lines.append(line)
                i += 1
                continue
            except Exception:
                pass  # fallback to original logic if anything breaks

        commented_lines.append(line)
        i += 1

    return commented_lines, class_info
