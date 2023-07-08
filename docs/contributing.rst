How to Contribute
=================

Introduction
------------
The project is hosted on `GitHub <https://github.com/FRC5190/FalconDocumentation>`_ 

Prerequisites
-------------
To contribute to the documentation, make sure you have the following installed:
- `Python <https://www.python.org/downloads/>`_
- `Sphinx <https://www.sphinx-doc.org/en/master/usage/installation.html>`_


Cloning
-------
To clone the repository, run the following command in powershell (windows) or terminal (mac/linux):

.. code-block:: bash

    git clone https://github.com/FRC5190/FalconDocumentation.git

After that you can open the project in Visual Studio Code.

Building
--------
All files that are pages on this website are located in the ``docs`` folder. To build the website locally, run the following command in the ``doc`` powershell (windows) or terminal (mac/linux):
.. code-block::

    .\make html

This will build the website in the ``docs/_build/html`` folder. To view the website, open the ``index.html`` file in that folder.

Pushing Changes
---------------
After you have tested the documentation locally, you can push your changes to the repository after creating a new branch and creating a pull request. 
