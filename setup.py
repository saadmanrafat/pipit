from setuptools import setup

setup(
    name='pipit',
    version='0.1.0',
    py_modules=['pipit'],
    install_requires=[
    ],
    entry_points='''
        [console_scripts]
        pipit=pipit:main
    '''
)

