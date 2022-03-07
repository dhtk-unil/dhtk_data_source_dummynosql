"""Setup DHTK.
"""
from setuptools import setup, find_namespace_packages

with open('requirements.txt', encoding="utf-8") as f:
    requirements = f.read().splitlines()
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dhtk_data_source_dummynosql",
    url='http://dhtk.unil.ch',
    author='Mattia Egloff and Davide Picca',
    author_email='davide.picca@unil.ch',
    version="0.2",
    packages=find_namespace_packages(include=['dhtk', 'dhtk.*',]),
license= \
        "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License",
    long_description=long_description,
    zip_safe=False,
    install_requires=requirements

)
