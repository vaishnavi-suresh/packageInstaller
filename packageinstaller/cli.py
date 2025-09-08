import click
from openai import OpenAI
from ollama import generate
import subprocess
import sys 
# Regular response





@click.command()

def auth() -> None:
    """A simple CLI that echoes the provided prompt."""
    list_string = ""\

    prompt = input("what would you like to build? spare no detail ")
    stream = generate(
        model='gpt-oss',
        prompt=f'return a comma separated list of ALL of the packages I need to install to create the following program: {prompt}. the name of each package should be the name used to install it using homebrew (i.e. brew install ___)',
        stream=True,
        keep_alive="30m",

    )
    
    
    for chunk in stream:

        if "response" in chunk and chunk['response']!='' and chunk['response']!=None:
            click.echo(chunk['response'])
            list_string += chunk["response"]  # stream tokens
        if chunk.get("done"):
            break
    list = list_string.split(", ")  
    click.echo(list)
    for package in list:
        click.echo(f"Installing {package}...")
        try:
            subprocess.run(["brew", "install", package], check=True)
            click.echo(f"Successfully installed {package}.")
        except subprocess.CalledProcessError as e:
            click.echo(f"Failed to install {package}. Error: {e}")
        except FileNotFoundError:
            click.echo("Homebrew is not installed or not found in PATH.")
            sys.exit(1) 



if __name__ == "__main__":
    auth()
   

    