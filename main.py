import argparse
import os
import glob
from dotenv import load_dotenv

from parser import parse_java_file
from comment_generator import generate_comments
from diagram_generator import generate_class_diagram
from utils import write_commented_file

def process_codebase(input_dir, output_diagram_path, token=None, model=None):
    java_files = glob.glob(os.path.join(input_dir, '**', '*.java'), recursive=True)
    all_class_info = []

    for java_file in java_files:
        if java_file.endswith("_commented.java"):
            continue

        print(f"Processing {java_file}")
        tree = parse_java_file(java_file)
        commented_code, class_info = generate_comments(java_file, tree, token=token, model=model)
        write_commented_file(java_file, commented_code)
        all_class_info.append(class_info)

    generate_class_diagram(all_class_info, output_path=output_diagram_path)

if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description="CodeComprehender: Java code annotation & diagram tool")
    parser.add_argument("-i", "--input", default="examples", help="Path to directory containing Java files")
    parser.add_argument("-o", "--output", default="output/code_structure", help="Output diagram file path (without extension)")
    parser.add_argument("-t", "--token", default=None, help="OpenRouter API token")
    parser.add_argument("-m", "--model", default=None, help="Model name to use (e.g. deepseek/deepseek-r1-0528-qwen3-8b:free)")

    args = parser.parse_args()

    token = args.token or os.getenv("API_KEY")
    model = args.model or os.getenv("MODEL")

    process_codebase(args.input, args.output, token=token, model=model)
