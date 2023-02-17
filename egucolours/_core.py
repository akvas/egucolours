
class Colour(str):
    """
    Class representation of a colour.

    The colour is instantiated by its hex value, i.e. Colour(name, hex_value). This class is designed to be compatible with the
    matplotlib colour mechanics, but holds additional metadata in the form of the
    colour name.
    """

    def __new__(cls, name, hex_value):
        return super(Colour, cls).__new__(cls, hex_value.lower())

    def __init__(self, name, hex_value):
        """
        :param name: Colour name
        :type name: str
        :param hex_value: Hexadecimal representation of the colour (e.g., "#ffffff")
        :type hex_value: str
        """
        self._name = name
        super().__init__()

    @property
    def name(self):
        """Colour name

        :return: Colour name
        :rtype: str
        """
        return self._name

    @property
    def hex(self):
        """HEX representation of colour

        :return: Colour hex string (e.g. #ffffff)
        :rtype: str
        """
        return self

    @property
    def RGB(self):
        """RGB representation of colour

        :return: RGB triple (e.g. (255, 255, 255))
        :rtype: tuple of int
        """
        return tuple(int(self[i:i + 2], 16) for i in (1, 3, 5))

    @property
    def rgb(self):
        """rgb representation of colour

        :return: rgb triple (e.g. (1.0, 1.0, 1.0))
        :rtype: tuple of float
        """
        return tuple(int(self[i:i + 2], 16) / 255 for i in (1, 3, 5))

    def __str__(self):
        a = self.RGB
        return '{0:14s} RGB {1:3d} | {2:3d} | {3:3d}      ({4})'.format('EGU ' + self.name + ':', a[0], a[1], a[2], super().__str__())


class ColourMapping(dict):
    """
    Class representation of a colour dictionary. The key/value pairs cannot be altered after instantiation.
    """
    def __init__(self, colour_dict):
        """
        :param colour_dict: dictionary of name: hex_value pairs
        :type colour_dict: dict
        """
        temp = {key: Colour(key, value) for key, value in colour_dict.items()}
        super().__init__(temp)

    def __setitem__(self, key, value):
        raise ValueError('ColourMapping items cannot be altered after instantiation.')

    def __delitem__(self, key):
        raise ValueError('ColourMapping items cannot be altered after instantiation.')