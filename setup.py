"""
The setup.py file is an essential part of packaging and distributing
Python projects. It is used by setuptools
(or distutils in older Python versions) to define the configuration of our project,
such as its metadata, dependencies, and more.
"""

from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function will return a list of requirements.
    """
    requirements = []
    try:
        with open('requirements.txt', 'r') as file:
            for line in file:
                requirement = line.strip()
                # Ignore empty lines and '-e .'
                if requirement and requirement != '-e .':
                    requirements.append(requirement)
    except FileNotFoundError:
        raise FileNotFoundError("requirements.txt file not found")

    return requirements


setup(
    name="networksecurity",  # Adjust the name for proper formatting (e.g., no spaces).
    version="0.0.1",
    author="Koushik",
    author_email="koushikkmkoushikkm61@gmail.com",
    packages=find_packages(include=["networksecurity", "networksecurity.*"]),  # Specify valid packages.
    install_requires=get_requirements(),
)
