"""
Setup for indico apis
"""
from setuptools import setup, find_packages

setup(
    name="indicoio",
    version="2.0.2",
    packages=find_packages(),
    description="""A Python Wrapper for indico app API.""",
    license="MIT License (See LICENSE)",
    long_description=open("README.rst").read(),
    url="https://github.com/IndicoDataSolutions/indico-ipa",
    author="indico",
    author_email="engineering@indico.io",
    tests_require=["pytest>=5.2.1"],
    install_requires=[
        "msgpack==1.0.0",
        "msgpack-numpy==0.4.4.3",
        "numpy==1.15.4",
        "Pillow>=6.2.0",
        "requests>=2.22.0",
        "setuptools>=41.4.0",
    ],
)
