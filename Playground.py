

from jinja2 import Environment, FileSystemLoader
import yaml
import os


with open("source.yaml", 'r') as stream:
    Devices = (yaml.safe_load(stream))

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
j2_env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)


for device, data in Devices.items():
    configuration = j2_env.get_template('template.j2').render(data)
    with open(os.path.join(THIS_DIR, device + ".txt"), 'w') as config_file:
        config_file.write(configuration) 
