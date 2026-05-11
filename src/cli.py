import argparse
from pathlib import Path
from rich import print
from .generator import TestCaseGenerator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="Requirement text file")
    args = parser.parse_args()

    requirement = Path(args.file).read_text(encoding="utf-8")
    generator = TestCaseGenerator()
    result = generator.generate(requirement)

    print(f"[green]Generated {len(result['test_cases'])} test cases successfully.[/green]")
    print("[cyan]Output saved in output/ folder.[/cyan]")

if __name__ == "__main__":
    main()
