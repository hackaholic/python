import typer
from typing_extensions import Annotated
from typing import Optional, TypeAlias


app = typer.Typer()

greet_arg: TypeAlias = Annotated[Optional[str], typer.Option("--name", "-n", metavar="<name>")]
@app.command(name="greet")
def greet(name: greet_arg):
    print(f"Hello {name}")


@app.command()
def goodbye(
    name: Annotated[Optional[str], typer.Option("--name", "-n")],
    formal:  Annotated[bool, typer.Option("--formal", "-n")]=False
    ):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}")


if __name__ =="__main__":
    app()