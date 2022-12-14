import setuptools
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="proj_mm",
    version="0.0.1",
    author="philip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=[]),
    scripts=[],
    install_requires=[
        'proj_r1@git+ssh://git@github.com/philipkcl/proj_r1.git@master',
        'proj_r2@git+ssh://git@github.com/philipkcl/proj_r2.git@master',
    ],
)
