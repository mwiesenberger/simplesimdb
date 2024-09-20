.. simplesimdb documentation master file, created by
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

simplesimdb: A lightweight simulation data creator and database manager
=======================================================================

A python module for creation and management of simple simulation data.
Essentially, a very basic database manager that creates its own data.

Simplesimdb is typically used to generate and analyse research data
from a Python script, where the data generation is done by an external
(typically highly optimized, written in C/C++ say) code that generates
an output for a given set of input parameters.  The emphasize here is
on the fact that the parameter generation, code execution and data
management loop is **automated**, which allows the user to run large
parameter scans with a few lines of Python code **without manual
interference**.  In this way for example publication grade plots can
be (re-)produced from scratch by just executing Python scripts. (See
for example the `impurities project <https://github.com/mwiesenberger/impurities>`_)

.. toctree::
   :maxdepth: 2
   :caption: Reference

   API Reference <api>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
