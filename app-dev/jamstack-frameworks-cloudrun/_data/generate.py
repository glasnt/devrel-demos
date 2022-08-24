

import datetime
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


templateLoader = FileSystemLoader(searchpath="templates/")
env = Environment(
    loader=templateLoader,
    autoescape=select_autoescape()
)

platform = "cloudrun"
frameworks = Path("data").glob("*.yml")

for config in frameworks: 
    framework = config.stem

    template = env.get_template(f"{platform}.md.j2")

    template.globals['now'] = datetime.datetime.utcnow

    with open(config) as f:
        data = yaml.safe_load(f.read())

    if "skip_cloudrun" not in data.keys(): 
        with open(f"../{framework}/README.md", 'w') as f:
            f.write(template.render(**data))