# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from setuptools import setup, find_packages

import importlib
import io
import logging
import os
import sys

logger = logging.getLogger(__name__)

PY3 = sys.version_info[0] == 3 and sys.version_info[1] >= 5

if not PY3:
    raise NotImplementedError(
        ("ucloud-sdk-python3 should be used in 3.5 " "and above of python interpreter")
    )


def load_version():
    return importlib.import_module(
        "ucloud.version", os.path.join("ucloud", "version.py")
    ).version


def load_long_description():
    try:
        with io.open("README.md", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def load_requirements(requirements_file):
    try:
        with io.open(requirements_file, encoding="utf-8") as f:
            return list(f.readlines())
    except FileNotFoundError:
        return []


dependencies = load_requirements("requirements.txt")

dependencies_test = dependencies + ["flake8>=3.6.0", "pytest>=4.6", "pytest-cov", "requests_mock"]

dependencies_doc = dependencies + ["sphinx"]

dependencies_ci = list(set(dependencies_test + dependencies_doc))

dependencies_dev = list(set(dependencies_ci + ["black"]))


def do_setup():
    setup(
        name="ucloud-sdk-python3",
        description="UCloud Service Development Kit - Python",
        long_description=load_long_description(),
        long_description_content_type="text/markdown",
        license="Apache License 2.0",
        version=load_version(),
        packages=find_packages(exclude=["tests*"]),
        package_data={"": []},
        include_package_data=True,
        zip_safe=False,
        install_requires=dependencies,
        extras_require={
            "test": dependencies_test,
            "doc": dependencies_doc,
            "dev": dependencies_dev,
            "ci": dependencies_ci,
        },
        dependencies_test=dependencies_test,
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Topic :: Software Development",
        ],
        author="ucloud",
        author_email="esl_ipdd@ucloud.cn",
        url="https://github.com/ucloud/ucloud-sdk-python3",
        python_requires=">=3.5",
    )


if __name__ == "__main__":
    do_setup()
