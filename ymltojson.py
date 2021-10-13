import sys
import os
import pkg_resources

import json

yml_file = sys.argv[1].replace('.\\', '')
installed = {pkg.key for pkg in pkg_resources.working_set}

if 'pyyaml' not in installed:
    print("exists module")
    os.system('pip install pyyaml')    

import yaml

with open(yml_file, 'r') as file:
    os_list = yaml.load(file, Loader=yaml.FullLoader)
    jsonFIle = yml_file.replace('.yml', '.json').replace('.yaml', '.json')
    with open(jsonFIle, 'w') as outfile:
        json.dump(os_list, outfile, indent=2)