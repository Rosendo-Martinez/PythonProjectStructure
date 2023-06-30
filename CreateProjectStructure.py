import argparse

parser = argparse.ArgumentParser(prog='CreateProjectStructure',
                                 description='Creates the initial structure of a Python project repository.')

parser.add_argument('path', help='the location where the project repository will be put (required, rel or abs path)')
parser.add_argument('projectName', help='the project name (required)')

args = parser.parse_args()

print(args)