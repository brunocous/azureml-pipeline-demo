#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent


def read(rel_path):
    with open(here / rel_path) as fh:
        return fh.read()


setup(
    name="my_awesome_project",
    version="0.0.1", 
    description="A sample Python project",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="you",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Scheduling",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.5, <4",
)
