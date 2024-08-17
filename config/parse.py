def dict2md(dict_input, key, value):
    head = f"|{key}|{value}|"
    mid = "|:---:|:---:|"
    body = []
    for k, v in dict_input.items():
        body.append(f"|{k}|{v}|")
    table = [head, mid] + body
    return "\n".join(table)


def parse_json(file_path_in, file_path_out, level=1):
    import json
    from stringcase import sentencecase

    with open(file_path_in, "r") as f:
        package = json.loads(f.read())
    dependencies = package["dependencies"]
    dev_dependencies = package["devDependencies"]
    dependencies = dict2md(dependencies, "pakage", "version")
    dev_dependencies = dict2md(dev_dependencies, "pakage", "version")
    dependencies_title = "#" * level + " " + sentencecase("dependencies")
    dev_dependencies_title = "#" * level + " " + sentencecase("devDependencies")

    doc = "\n".join(
        [dependencies_title, dependencies, dev_dependencies_title, dev_dependencies]
    )
    with open(file_path_out, "w") as f:
        f.write(doc)


def parse_yml(file_path_in, file_path_out, level=1):
    import yaml

    with open(file_path_in, "r") as f:
        env = yaml.safe_load(f)
    dependencies = env["dependencies"]
    python = list(filter(lambda x: "python" in x, dependencies))[0]
    pip = list(filter(lambda x: isinstance(x, dict), dependencies))[0]["pip"]
    pip = {k: v for (k, v) in map(lambda x: x.split("=="), pip)}
    pip = dict2md(pip, "package", "version")
    python_title = "#" * level + " Python"
    python_body = f"python: {python.split('=')[1]}"
    pip_title = "#" * level + " Python Packages"
    pip_body = pip
    doc = "\n".join([python_title, python_body, pip_title, pip_body])
    with open(file_path_out, "w") as f:
        f.write(doc)


if __name__ == "__main__":
    # parse_json("config/frontend/package.json", "config/frontend.md")
    parse_yml("config/backend/environment.yaml", "config/backend.md")
