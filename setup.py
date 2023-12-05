"""
Setup file for Typhoon API.
"""

from setuptools import setup

setup(
    name="typhoon",
    packages=[
        "app",
        "app.routes",
        "app.utils",
    ],
    install_requires=[
        "flask",
    ],
    author="Pixelz",
)