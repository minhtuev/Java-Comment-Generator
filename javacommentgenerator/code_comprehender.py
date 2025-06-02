import os
import glob
from .parser import parse_java_file
from .comment_generator import generate_comments
from .diagram_generator import generate_class_diagram
from .utils import write_commented_file


class CodeComprehender:
    def __init__(self, input_dir, output_diagram_path, generator):
        print("Initializing CodeComprehender")
        self.input_dir = input_dir
        self.output_diagram_path = output_diagram_path
        self.generator = generator

    def run(self):
        java_files = glob.glob(os.path.join(self.input_dir, '**', '*.java'), recursive=True)
        all_class_info = []

        for java_file in java_files:
            if java_file.endswith("_commented.java"):
                continue

            print(f"Processing {java_file}")
            tree = parse_java_file(java_file)
            commented_code, class_info = generate_comments(java_file, tree, self.generator)
            write_commented_file(java_file, commented_code)
            all_class_info.append(class_info)

        generate_class_diagram(all_class_info, output_path=self.output_diagram_path)
