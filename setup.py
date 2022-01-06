# Copyright 2019 TerraPower, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup.py script for the Example App for ARMI"""
import re
from setuptools import setup, find_packages

from myapp import __version__


with open("README.md") as f:
    README = f.read()


setup(
    name="armi-example-app",
    version=__version__,
    description="A simple example application built using the Advanced Reactor "
    "Modeling Interface (ARMI)",
    author="TerraPower, LLC",
    author_email="armi-devs@terrapower.com",
    url="https://github.com/terrapower/armi/",
    license="Apache 2.0",
    long_description=README,
    python_requires=">=3.6",
    packages=find_packages(),
    entry_points={"console_scripts": ["armiexample = armiexample.__main__:main"]},
    install_requires=[
        "armi @ git+https://github.com/terrapower/armi",
        "terrapower-dragon @ git+https://github.com/terrapower/dragon-armi-plugin",
    ],
    tests_require=["nbconvert", "jupyter_client", "ipykernel"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: Apache Software License",
    ],
)
