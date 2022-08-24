import datetime
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


templateLoader = FileSystemLoader(searchpath="templates/")
env = Environment(loader=templateLoader, autoescape=select_autoescape())

frameworks = sorted(Path("data").glob("*.yml"))

template = env.get_template("deployment.md.j2")
gcr_readme = env.get_template("cloudrun.md.j2")
firebase_readme = env.get_template("firebase.md.j2")
framework_list = []

for config in frameworks:
    framework = config.stem


    template.globals["now"] = datetime.datetime.utcnow

    with open(config) as f:
        data = yaml.safe_load(f.read())

    framework_list.append((data["name"], framework, data["language"]))

    if "skip_cloudrun" not in data.keys():
        with open(f"../{framework}/README.md", "w") as f:
            f.write(template.render(**data, platform="Cloud Run"))

    if "skip_firebase" not in data.keys():
        with open(f"../../jamstack-frameworks-firebase/{framework}/README.md", "w") as f:
            f.write(template.render(**data, platform="Firebase"))



with open("../README.md", "w") as f:
    f.write(gcr_readme.render(frameworks=framework_list))

with open("../../jamstack-frameworks-firebase/README.md", "w") as f:
    f.write(firebase_readme.render(frameworks= framework_list))