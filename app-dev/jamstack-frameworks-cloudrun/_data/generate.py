

import datetime
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


templateLoader = FileSystemLoader(searchpath="templates/")
env = Environment(
    loader=templateLoader,
    autoescape=select_autoescape()
)

base_readme = "../README.md"
platform = "cloudrun"
frameworks = sorted(Path("data").glob("*.yml"))

with open(base_readme, "w") as f:
    f.write("""
# Cloud Run NodeJS and Jamstack Examples

This demo shows an example of how to deploy some of the popular [Node frameworks](https://jamstack.org/survey/2021/#choices-frameworks) to Cloud Run. 

These examples use the template generator for each framework, and use the provided app runner to serve the examples in a container. For examples of how to host the built versions of these frameworks, see their [Firebase example](../nodejs-frameworks-firebase).

## Example Frameworks

All frameworks are NodeJS based, unless otehrwise marked.

""")

for config in frameworks: 
    framework = config.stem

    template = env.get_template(f"{platform}.md.j2")

    template.globals['now'] = datetime.datetime.utcnow

    with open(config) as f:
        data = yaml.safe_load(f.read())

    if "skip_cloudrun" not in data.keys(): 
        with open(f"../{framework}/README.md", 'w') as f:
            f.write(template.render(**data))
        
        with open(base_readme, 'a') as f: 
            f.write(f" * [{data['name']}]({framework})")
            if data['language'] != "node": 
                f.write(f" ({data['language']})")
            f.write("\n")