import typer

app = typer.Typer(name="flow")

@app.command()
def version():
    typer.echo("archflow 0.1.0")

if __name__ == "__main__":
    app()
