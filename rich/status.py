import time
from rich.console import Console

import asyncio

console = Console()

# Run the following command to see the available choices for spinner:
# python -m rich.spinner
def do_work(sec: float) -> None:
    time.sleep(sec)

async def worker(sec: float, name: str)-> None:
    with console.status(f"Working on task: {name} ....", spinner_style="bold magenta"):
        await asyncio.sleep(sec)
    
    return f"Done {name}"

async def main():
    with console.status("Working ...", spinner_style="red3"):
        do_work(2)

    with console.status("Working ...", spinner="monkey"):
        do_work(2)
    
    for data in await asyncio.gather(
            worker(3, "A"),
            worker(3, "B"),
            worker(3, "C")
        ):
        print(data)
    

if __name__ == "__main__":
    asyncio.run(main())