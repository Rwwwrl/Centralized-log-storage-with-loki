from setuptools import setup, find_packages

with open('requirements/prod.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='loki_real_testing',
    version='0.0.0',
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
)
