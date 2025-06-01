import javalang

def parse_java_file(filepath):
    with open(filepath, 'r') as file:
        code = file.read()
    tree = javalang.parse.parse(code)
    return tree
