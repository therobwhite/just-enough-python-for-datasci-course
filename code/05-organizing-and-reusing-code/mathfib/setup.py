from setuptools import setup, find_packages

setup(
    name="mathfib",
    version="0.1.0",
    packages=find_packages(where=".", include=["mathfib*"]),  # Include both mathfib and mathfib.mathfib
)