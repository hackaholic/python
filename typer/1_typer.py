"""
This script doesn't even use Typer internally. But you can use the typer command to run it as a CLI application.

try to run from cli
typer 1_typer.py run "coco"
typer 1.typer.py run --help
"""

def main(name: str):
    print(f"Hello {name}!")

