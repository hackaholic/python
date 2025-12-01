"""
To see how the progress display looks, try this from the command line:
python -m rich.progress
"""



import time

from rich.progress import track, Progress


for data in track(range(100)):
    time.sleep(0.01)


with Progress() as progress:
    task1 = progress.add_task("[red]Downloading...", total=1000)
    task2 = progress.add_task("[green]Processing...", total=1000)
    task3 = progress.add_task("[cyan]Cooking...", total=1000)

    while not progress.finished:
        progress.advance(task_id=task1, advance=0.5)
        progress.advance(task_id=task2, advance=0.3)
        progress.advance(task_id=task3, advance=0.9)
        time.sleep(0.01)
