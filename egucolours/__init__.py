

class Colour(str):
    """
    Class representation of a colour. The colour is instantiated by its hex value, 
    i.e. Colour(name, hex_value). This class is designed to be compatible with the
    matplotlib colour mechanics, but holds additional metadata in the form of the 
    colour name.

    Properties
    ----------
    name : str
        Colour name.
    hex : str
        Hexadecimal representation of the colour (e.g., "#ffffff").
    RGB : tuple of int
        Red, green, blue primary values of the colour in the range 0 - 255.
    rgb : tuple of float
        Red, green, blue primary values of the colour in the range 0.0 - 1.0.

    """
    def __new__(cls, name, hex_value):
        return super(Colour, cls).__new__(cls, hex_value.lower())

    def __init__(self, name, hex_value):
        self._name = name 
        super().__init__()

    @property
    def name(self):
        return self._name

    @property
    def hex(self):
        return self 

    @property
    def RGB(self):
        return tuple(int(self[i:i+2], 16) for i in (1, 3, 5))

    @property
    def rgb(self):
        return tuple(int(self[i:i+2], 16) / 255 for i in (1, 3, 5))

    def __str__(self):
        a = self.RGB
        return '{0:14s} RGB {1:3d} | {2:3d} | {3:3d}      ({4})'.format('EGU ' + self.name + ':', a[0], a[1], a[2], super().__str__())
