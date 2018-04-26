import ast
import sys
import pkgutil

all_modules = [module.name for module in pkgutil.iter_modules()]

class FindImports(ast.NodeVisitor):
    
    def __init__(self):
        self.module = set()

    def visit_ImportFrom(self, node):
        if node.module not in all_modules:
            self.module.add(node.module.split('.')[0])

    def visit_Import(self, node):
        for child in ast.walk(node):
            if isinstance(child, ast.alias):
                if child.name not in all_modules:
                    self.module.add(child.name)




