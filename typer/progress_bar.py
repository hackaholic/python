import typer
from rich.progress import track

import time


def main():
    total = 0
    for val in track(range(100), description="Processing Data..."):
        time.sleep(0.01)
        total += 1
    
    print(f"Processed {total} total")


if __name__ == "__main__":
    typer.run(main)
