from setuptools import setup, find_packages

setup(
    name='machine_learning_local_utils',
    version='0.1.0',
    packages=find_packages(include=['machine_learning', 'machine_learning.*'])
)

