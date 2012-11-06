#! /usr/bin/env python

from setuptools import setup, find_packages
import dojo

setup(
    name="dojo",
    version=dojo.__version__,
    description="Add Dojo to your Django projects and run Dojo builds with manage.py commands",
    author="Mike Kibbel",
    author_email="mkibbel@gmail.com",
    license="BSD License",
    platforms=["OS Independent"],
    install_requires=[
        "Django>=1.4"
    ],
    packages=find_packages(exclude=["example", "example.*"]),
    include_package_data=True,
    zip_safe=False,
)
