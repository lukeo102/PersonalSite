from json import load
from pathlib import Path
from jinja2 import Environment, PackageLoader, select_autoescape


def read_config(file) -> list[dict]:
    with open(Path.joinpath(root, f"config/{file}.json"), 'r') as file:
        contents = load(file)

    return contents


if __name__ == "__main__":
    # Jinja setup
    root = Path.cwd()
    jinja = Environment(
        loader=PackageLoader("generate"),
        autoescape=select_autoescape()
    )
    template = jinja.get_template("index.jinja2")

    # Read configs
    projects = read_config("projects")
    friends = read_config("friends")

    # Render webpage
    rendered = template.render(projects=projects, friends=friends)

    # Delete the old webpage
    index_path = Path.joinpath(root, "www/index.html")
    index_path.unlink(missing_ok=True)
    index_path.touch()

    # Save the new webpage
    with index_path.open("w") as file:
        file.write(rendered)
