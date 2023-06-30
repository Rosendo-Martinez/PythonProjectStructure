import argparse
import os

def createDirAndFiles(dirPath, fileNames):
    os.mkdir(dirPath)
    for name in fileNames:
        with open(os.path.join(dirPath, name), 'w') as f:
            pass

parser = argparse.ArgumentParser(prog='CreateProjectStructure',
                                 description='Creates the initial structure of a Python project repository (based off Kenneth Reitz\'s ideal Python repository).')

parser.add_argument('path', help='the location where the project repository will be put (required, rel or abs path)')
parser.add_argument('projectName', help='the project name (required)')

args = parser.parse_args()

root = os.path.join(args.path, args.projectName)
module = os.path.join(root, args.projectName)
docs = os.path.join(root, 'docs')
tests = os.path.join(root, 'tests')
createDirAndFiles(root, ['README.rst', 'LICENSE', 'setup.py', 'requirements.txt'])
createDirAndFiles(module, ['__init__.py', 'core.py', 'helpers.py', ])
createDirAndFiles(docs, ['conf.py', 'index.rst'])
createDirAndFiles(tests, ['test_basic.py', 'test_advanced.py'])