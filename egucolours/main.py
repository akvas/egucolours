"""
egucolours.main
===============

EGU main palette (blue/yellow).
"""

from ._color_data import MAIN_PALETTE
from ._core import Colour, ColourMapping


#:
blue = Colour('blue', MAIN_PALETTE['blue'])
#:
yellow = Colour('yellow', MAIN_PALETTE['yellow'])
#:
colours = ColourMapping(MAIN_PALETTE)
