import argparse
import os
import glob
from dotenv import load_dotenv

from .code_comprehender import CodeComprehender
from .comment_generators.default_generator import DefaultCommentGenerator
from .comment_generators.openrouter_generator import OpenRouterCommentGenerator


def select_generator(generator_type, token=None, model=None):
    if generator_type == "openrouter":
        if not token or not model:
            raise ValueError("❌ OpenRouter generator requires both --token and --model (or set them in .env)")
        return OpenRouterCommentGenerator(token=token, model=model)

    if generator_type == "default":
        return DefaultCommentGenerator()

    # Auto-detect if not explicitly specified
    if token and model:
        print("⚠️  No generator specified. Falling back to OpenRouter since token is provided.")
        return OpenRouterCommentGenerator(token=token, model=model)

    print("⚠️  No generator specified. Falling back to default.")
    return DefaultCommentGenerator()


def process_codebase(input_dir, output_diagram_path, generator):
    code_comprehender = CodeComprehender(input_dir, output_diagram_path, generator)
    code_comprehender.run()


def cli_entry_point():
    load_dotenv()

    parser = argparse.ArgumentParser(description="JavaCommentGenerator: Java code annotation & diagram tool")
    parser.add_argument("-i", "--input", default="examples", help="Path to directory containing Java files")
    parser.add_argument("-o", "--output", default="output/code_structure", help="Output diagram file path (without extension)")
    parser.add_argument("-t", "--token", default=None, help="OpenRouter API token")
    parser.add_argument("-m", "--model", default=None, help="Model name to use (e.g. deepseek/deepseek-r1-0528-qwen3-8b:free)")
    parser.add_argument("-g", "--generator", choices=["default", "openrouter"], default=None, help="Which comment generator to use")

    args = parser.parse_args()

    token = args.token or os.getenv("API_KEY")
    model = args.model or os.getenv("MODEL")

    generator = select_generator(args.generator, token=token, model=model)
    process_codebase(args.input, args.output, generator=generator)