#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anytialize",
    version="0.1",
    author="Leon Puchinger",
    description="language neutral initialization tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeonPuchinger/anytialize",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires =">=3.6",
)