"""
Setup file for Typhoon API.
"""

from setuptools import setup

setup(
    name="typhoon",
    packages=[
        "app.api",
        "app.db",
        "app.models",
        "app.services",
        "app.routes",
        "app.utils",
        "app.src",
    ],
    install_requires=[
        "flask",
    ],
    author="Pixelz",
)