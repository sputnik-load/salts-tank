#!/usr/bin/env python

from setuptools import setup

setup(
    name="salts-tank",
    version="0.0.0.2",
    description="Salts-tank server",
    author="Ilya Krylov",
    author_email="ilya.krylov@gmail.com",
    url="http://github.com/sputnik-load/salts-tank",
    packages=["salts_tank_app"],
    package_dir={"salts_tank_app": "salts_tank_app"},
    install_requires=[
    ],
    scripts=['scripts/run-salts-tank', 'scripts/run-salts-tank'],
)
