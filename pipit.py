from pkgutil import iter_modules

import ast
import sys
import argparse
import subprocess

class FindImports(ast.NodeVisitor):
    def __init__(self):
        self.modules = set()
        self._all_modules = [module.name for module in iter_modules(path=['.']+sys.path)] + \
                list(sys.modules.keys())

    def visit_ImportFrom(self, node):
        module_name = node.module.split('.')[0]
        if module_name not in self._all_modules:
            self.modules.add(module_name)
        
    def visit_Import(self, node):
        for child in ast.walk(node):
            if isinstance(child, ast.alias):
                if child.name not in self._all_modules:
                    self.modules.add(child.name)
                    
                    
def install(imported_modules):
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install'] + list(imported_modules))
    except subprocess.CalledProcessError as err:
        print('Error: ', err)


def main():
    parser = argparse.ArgumentParser(description='Install dependencies of a python script.')
    parser.add_argument(dest='script_name', metavar='filename')
    args = parser.parse_args()
    
    tree = ast.parse(open(args.script_name).read())
    imported = FindImports()
    imported.visit(tree)
    
    if not imported.modules:
        print('No new dependencies found.')
    else:
        while True:
            user_choice = input('Installing ' +  ', '.join(imported.modules) + '\n Proceed (y/n)? ')
            if user_choice.isalpha():
                if user_choice.lower() == 'y':
                    install(imported.modules)
                    break
                elif user_choice.lower() == 'n':
                    break


if __name__ == '__main__':
    main()
