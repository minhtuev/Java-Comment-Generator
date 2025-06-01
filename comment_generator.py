from utils import get_access_modifier, extract_block
from comment_generators.default_generator import DefaultCommentGenerator

def generate_comments(filepath, tree, token=None):
    with open(filepath, 'r') as f:
        original_lines = f.readlines()

    commented_lines = []
    class_info = {
        "name": None,
        "methods": [],
        "dependencies": []
    }

    comment_gen = DefaultCommentGenerator()
    i = 0
    while i < len(original_lines):
        line = original_lines[i]
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)].rstrip("\n")
        tokens = stripped.split()

        # ---- Class-level detection ----
        if "class" in tokens:
            class_index = tokens.index("class")
            class_name = tokens[class_index + 1].split("{")[0]
            access_modifier = get_access_modifier(tokens)
            class_info["name"] = class_name

            class_block, offset = extract_block(original_lines, i)
            comment = comment_gen.generate_class_comment(class_name, indent, access_modifier, class_block)
            commented_lines.extend(comment)
            commented_lines.append(line)
            i += 1
            continue

        # ---- Method-level detection ----
        if "void" in tokens:
            access_modifier = get_access_modifier(tokens)
            method_name = tokens[tokens.index("void") + 1].split("(")[0]
            class_info["methods"].append(f"{access_modifier} {method_name}()")

            method_block, offset = extract_block(original_lines, i)
            comment = comment_gen.generate_method_comment(method_name, indent, access_modifier, method_block)
            commented_lines.append(comment)
            commented_lines.append(line)
            i += 1
            continue

        commented_lines.append(line)
        i += 1

    return commented_lines, class_info
