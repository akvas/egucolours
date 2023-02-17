"""
egucolours.neutral
==================

EGU neutral palette (white/grey).
"""

from ._color_data import NEUTRAL_PALETTE
from ._core import Colour, ColourMapping


white = Colour('white', NEUTRAL_PALETTE['white'])  #:
grey = Colour('grey', NEUTRAL_PALETTE['grey'])  #:

colours = ColourMapping(NEUTRAL_PALETTE)  #:
