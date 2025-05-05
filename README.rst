==================================
sphinxcontrib-prettyspecialmethods
==================================

Shows special methods as the python syntax that invokes them

Overview
--------

This module renders docs like

.. code-block:: rst

    .. method:: __add__(other)
        Docstring


as

self + other
    Docstring


Installing
----------

Install this fork directly from github:

.. code-block:: sh

    pip install git+https://github.com/ktbarrett/prettyspecialmethods


After installing this module, add the following to your `conf.py` to enable it

.. code-block:: python

    extensions = [
        ...  # your other extensions
        'sphinxcontrib.prettyspecialmethods',
    ]
