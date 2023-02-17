
"""
European Geosciences Union (EGU) Colours
========================================

European Geosciences Union (EGU) colour palettes and division colours derived from
EGU's `visual identity <https://www.egu.eu/visual-identity/>`_ and
`structure overview <https://www.egu.eu/structure/divisions/>`_.
The package can be installed via `pip`:

.. code-block:: bash

    python -m pip install egucolours


Separate sub-modules for the main palette, neutral palette, and division colors are available.
Each module contains a dict-like collection `colours` which holds all colours of the respective
palette. The colours are compatible with the `matplotlib` colour mechanics and can be used in the
same fashion as hex-strings or RGB triples.

.. code-block:: python

    >>> import matplotlib.pyplot as plt
    >>> import egucolours

    >>> plt.plot(x, y, color=egucolours.division.AS)

Colours can be accessed by their name. For the `main` palette, this looks like as follows:

.. code-block:: python

   >>> import egucolours
   >>> print(egucolours.main.colours)
   {'blue': '#0072bc', 'yellow': '#ffde00'}

   >>> print(egucolours.main.blue)
   EGU blue:      RGB   0 | 114 | 188      (#0072bc)

   >>> print(egucolours.main.colours['blue'])
   EGU yellow:    RGB 255 | 222 |   0      (#ffde00)


Division colours can be accessed in a similar fashion:

.. code-block:: python

   >>> import egucolours
   >>> print(egucolours.division.AS)
   EGU AS:        RGB  66 |  66 | 212      (#4242d4)

   >>> print(egucolours.division.colours['AS'])
   EGU AS:        RGB  66 |  66 | 212      (#4242d4)


The `egucolours` package contains a top-level dict-like collection with all palettes:

.. code-block:: python

    >>> import egucolours
    >>> print(egucolours.colours)
    {'blue': '#0072bc', 'yellow': '#ffde00', 'white': '#ffffff', 'grey': '#a8a9ad', 'AS': '#4242d4',
    'BG': '#1a4d04', 'CL': '#5f3172', 'CR': '#007db8', 'EMRP': '#87251f', 'ERE': '#2a6736',
    'ESSI': '#6a4a96', 'G': '#a450ce', 'GD': '#aa292b', 'GI': '#757575', 'GM': '#497e74',
    'GMPV': '#dc3728', 'HS': '#258838', 'NH': '#753f2f', 'NP': '#0f1e3d', 'OS': '#274b96',
    'PS': '#932d75', 'SM': '#a03150', 'SSP': '#916b2a', 'SSS': '#6b4a08', 'ST': '#75387a',
    'TS': '#be5409'}


.. image:: images/full.png


Modules
=======

.. automodule:: egucolours.main
    :members:

.. automodule:: egucolours.neutral
    :members:

.. automodule:: egucolours.division
    :members:

Classes
=======

.. autoclass:: egucolours.Colour
    :members:

.. autoclass:: egucolours.ColourMapping
    :members:
"""

from ._core import ColourMapping, Colour
from . import division
from . import main
from . import neutral


colours = ColourMapping(main.MAIN_PALETTE | neutral.NEUTRAL_PALETTE | division.DIVISION_COLOURS)
