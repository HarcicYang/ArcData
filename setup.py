# setup.py

from setuptools import setup

import ArcData

setup(
    name="arcdata",
    version=ArcData.VERSION,
    description="专为 Python 语言设计、易用、轻量的数据库",
    author="Harcic",
    author_email="harcic@outlook.com",
    url="https://github.com/HarcicYang/ArcData",
    packages=["ArcData", "ArcData.Utils"],
    include_package_data=True,
)
