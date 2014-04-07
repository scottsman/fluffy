from setuptools import setup

setup(
    name='fluffy',
    version='0.1.0',
    description='Add some fluff to your project',
    author='Scott Novak',
    author_email='scottsman@gmail.com',
    packages=['fluffy'],
    package_dir={'fluffy': 'python'},
    package_data={'fluffy': ['resources/cats/*.txt']}
)

