import typer

app = typer.Typer()

@app.command(name="greet",
             help="Greet people",
             epilog="<prog> hello <name>")
def hello(name: str) -> None:
    print(f"hello {name}")

@app.command()
def goodbye(name: str, formal: bool = False) -> None:
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}")

if __name__ == "__main__":
    app()