import ast

class CodeAnalyzer(ast.NodeVisitor):
    
    def __init__(self):
        self.module = set()

    def visit_ImportFrom(self, node):
        self.module.add(node.module)



if __name__ == '__main__':

    c = CodeAnalyzer()
    code = ast.parse(open('testfile.py').read(), 'exec')
    c.visit(code)
    
    print('Modules: ', c.module)


