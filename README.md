# ipycytoscape

[![Build Status](https://travis-ci.org/Quantstack/ipycytoscape.svg?branch=master)](https://travis-ci.org/Quantstack/ipycytoscape)

Python implementation of the graph visualization tool Cytoscape.

Try it out using binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/QuantStack/ipycytoscape/stable?filepath=examples)

![cytoscape screencast](https://user-images.githubusercontent.com/17600982/76328068-bbbbcf00-62e2-11ea-93ed-01ba392ac50c.gif)

#### Supports:

* Conversion from NetworkX see [example](https://github.com/QuantStack/ipycytoscape/blob/master/examples/Test%20NetworkX%20methods.ipynb)
* Conversion from Pandas DataFrame see [example](https://github.com/QuantStack/ipycytoscape/blob/master/examples/DataFrame%20interaction.ipynb)

## Installation

With `conda`: (recommended)

```
conda install -c conda-forge ipycytoscape
```

With `pip`:

```bash
pip install ipycytoscape
```

#### For jupyterlab users:

There is an aditional step if you're using JupyterLab:

```bash
jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-cytoscape
```

If you are using Jupyter Notebook 5.2 or earlier, you may also need to enable
the nbextension:
```bash
jupyter nbextension enable --py [--sys-prefix|--user|--system] ipycytoscape
```

## For a development installation:
**(requires npm)**

While not required, we recommend creating a conda environment to work in:
```bash
conda create -n ipycytoscape -c conda-forge jupyterlab nodejs
conda activate ipycytoscape

# clone repo
git clone https://github.com/QuantStack/ipycytoscape.git
cd ipycytoscape

# Install python package for development, runs npm install and npm run build
pip install -e .
```

When developing ipycytoscape, you need to manually enable the extension with the
notebook / lab frontend. For lab, this is done by the command:

```
# install jupyterlab-manager and this extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
jupyter labextension install .
```

For classic notebook, you can run:

```
jupyter nbextension install --sys-prefix --symlink --overwrite --py <your python package name>
jupyter nbextension enable --sys-prefix --py <your python package name>
```

Note that the `--symlink` flag doesn't work on Windows, so you will here have to run
the `install` command every time that you rebuild your extension. For certain installations
you might also need another flag instead of `--sys-prefix`, but we won't cover the meaning
of those flags here.

### How to see your changes
#### Typescript: 
To continuously monitor the project for changes and automatically trigger a rebuild, start Jupyter in watch mode:
```bash
jupyter lab --watch
```
And in a separate session, begin watching the source directory for changes:
```bash
npm run watch
```

#### Python:
If you make a change to the python code then you need to restart the notebook kernel to have it take effect.

## License

We use a shared copyright model that enables all contributors to maintain the
copyright on their contributions.

This software is licensed under the BSD-3-Clause license. See the
[LICENSE](LICENSE) file for details.
