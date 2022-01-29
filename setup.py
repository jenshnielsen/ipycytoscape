#!/usr/bin/env python

# Copyright (c) 2020, QuantStack, Mariana Meireles and ipycytoscape Contributors
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.

import os
from glob import glob
from os import path

from jupyter_packaging import (
    combine_commands,
    create_cmdclass,
    ensure_targets,
    get_version,
    install_npm,
)
from setuptools import find_packages, setup

# The name of the project
name = "ipycytoscape"

HERE = os.path.dirname(os.path.abspath(__file__))

# Get our version
version = get_version(path.join(name, "_version.py"))

nb_path = path.join(HERE, name, "nbextension", "static")
lab_path = path.join(HERE, name, "labextension")

# Representative files that should exist after a successful build
jstargets = [
    path.join(nb_path, "index.js"),
    path.join(HERE, "lib", "plugin.js"),
]

package_data_spec = {name: ["*"]}

data_files_spec = [
    ("share/jupyter/nbextensions/jupyter-cytoscape", nb_path, "**"),
    ("share/jupyter/labextensions/jupyter-cytoscape", lab_path, "**"),
    ("etc/jupyter/nbconfig/notebook.d", HERE, "jupyter-cytoscape.json"),
]


cmdclass = create_cmdclass(
    "jsdeps", package_data_spec=package_data_spec, data_files_spec=data_files_spec
)
cmdclass["jsdeps"] = combine_commands(
    install_npm(HERE, build_cmd="build"),
    ensure_targets(jstargets),
)

setup_args = dict(
    version=version,
    scripts=glob(path.join("scripts", "*")),
    cmdclass=cmdclass,
)

if __name__ == "__main__":
    setup(**setup_args)
