from graphviz import Digraph


def generate_class_diagram(class_infos, output_path):
    dot = Digraph(comment='Java Code Architecture')

    for info in class_infos:
        if not info["name"]:
            continue

        method_lines = "\\l".join(info["methods"]) + "\\l" if info["methods"] else ""
        label = f"{{{info['name']}|{method_lines}}}"
        dot.node(info["name"], label=label, shape="record")

        for dep in info["dependencies"]:
            dot.edge(info["name"], dep)

    dot.render(output_path, format='png', cleanup=True)
