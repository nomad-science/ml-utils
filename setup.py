from setuptools import setup, find_packages

setup(
    name='mllocalutils',
    version='0.1.0',
    packages=find_packages(where="ml_utils", include=['ml_utils*'])
)

