import argparse
import os
import glob
from parser import parse_java_file
from comment_generator import generate_comments
from diagram_generator import generate_class_diagram
from utils import write_commented_file

def process_codebase(input_dir, output_diagram_path, token=None):
    java_files = glob.glob(os.path.join(input_dir, '**', '*.java'), recursive=True)
    all_class_info = []

    for java_file in java_files:
        if java_file.endswith("_commented.java"):
            continue

        print(f"Processing {java_file}")
        tree = parse_java_file(java_file)
        commented_code, class_info = generate_comments(java_file, tree, token=token)
        write_commented_file(java_file, commented_code)
        all_class_info.append(class_info)

    generate_class_diagram(all_class_info, output_path=output_diagram_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CodeComprehender: Java code annotation & diagram tool")
    parser.add_argument(
        "-i", "--input", 
        default="examples",
        help="Path to directory containing Java files (default: examples/)"
    )
    parser.add_argument(
        "-o", "--output", 
        default="output/code_structure",
        help="Output diagram file path without extension (default: output/code_structure)"
    )
    parser.add_argument(
        "-t", "--token",
        default=None,
        help="Optional API token (e.g., for OpenAI-powered commenting)"
    )

    args = parser.parse_args()

    process_codebase(args.input, args.output, token=args.token)
