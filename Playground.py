
# import csv
# from jinja2 import Template
# source_file = 'book2.csv'
# interface_template_file = 'template.j2'

# with open(interface_template_file) as f:
#     interface_template = Template(f.read(),keep_trailing_newline=True)

# interafce_configs = ""
# with open(source_file) as f:
#     reader = csv.DictReader(f)
#     for raw in reader:
#         interface_config = interface_template.render(
#             interface = raw['interface'],
#             description = raw['description'],
#             address = raw['address']
#         )
#         interafce_configs += interface_config

# with open('configuration_interfaces.txt', 'w') as f:
#     f.write(interafce_configs)

from jinja2 import Environment, FileSystemLoader
import yaml
import os
from pprint import pprint

with open("source.yaml", 'r') as stream:
    Devices = (yaml.safe_load(stream))

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
j2_env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)


for device, data in Devices.items():
    configuration = j2_env.get_template('template.j2').render(data)
    with open(os.path.join(THIS_DIR, device + ".txt"), 'w') as config_file:
        config_file.write(configuration) 