import os

def write_commented_file(original_path, commented_lines):
    dirname, filename = os.path.split(original_path)
    new_filename = filename.replace(".java", "_commented.java")
    new_path = os.path.join(dirname, new_filename)

    with open(new_path, "w") as f:
        f.writelines(commented_lines)

    print(f"✅ Commented file written to: {new_path}")


def get_access_modifier(tokens):
    for modifier in ["public", "private", "protected"]:
        if modifier in tokens:
            return modifier
    return "default"


def extract_block(lines, start_index):
    block = []
    brace_count = 0
    in_block = False
    i = start_index

    while i < len(lines):
        line = lines[i]
        block.append(line)

        if "{" in line:
            brace_count += line.count("{")
            in_block = True
        if "}" in line:
            brace_count -= line.count("}")
        if in_block and brace_count == 0:
            break

        i += 1

    return block, (i - start_index + 1)
