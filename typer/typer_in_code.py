"""
💬 Run your application
python typer_in_code.py
"""

import typer

def main(name: str) -> None:
    print(f"Hello {name}!")

if __name__ == "__main__":
    typer.run(main)