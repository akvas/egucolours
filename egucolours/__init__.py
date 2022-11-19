

class Colour(str):
    """
    Class representation of a colour. The colour is instantiated by its hex value, 
    i.e. Color(name, hex_value).

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
    def __new__(self, name, hex_value):
        self._name = name 
        return super(Colour, self).__new__(self, hex_value.lower())

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
