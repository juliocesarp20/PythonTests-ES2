from setuptools import setup, find_packages

setup(
    name="user-management-package",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "ruff",
        "pytest",
    ],
)