import re
import json
class Cotation():
    def __init__(self, _cotation):
        """Initialise une cotation

        Args:
            _cotation (str): cotation d'escalade
        >>> Cotation("6A")
        {"_cotation": "6A"}
        """
        self._cotation = _cotation

    @property
    def cotation(self):
        """Retourne la cotation

        Returns:
            str: cotation
        """
        return self._cotation
    @cotation.setter
    def cotation(self, value):
        self._cotation = value

    @staticmethod
    def verif_cotation(value):
        """Vérifie que la cotation est possible

        Args:
            value (str): cotation à tester

        Returns:
            bool: True: la cotation existe, False: la cotation n'existe pas

        ToDo:
            - Prendre en compte les différents types de cotations
        >>> print(Cotation.verif_cotation("6A"))
        True
        >>> print(Cotation.verif_cotation("1A"))
        False
        >>> print(Cotation.verif_cotation("5C+"))
        True
        >>> print(Cotation.verif_cotation("7D"))
        False
        >>> print(Cotation.verif_cotation("7C-"))
        False
        """
        return bool(re.fullmatch(pattern=r"[2-9]([A-C]?\+?)?", string=value))

    def __json__(self):
        return self.__dict__

    def __repr__(self):
        return json.dumps(self.__dict__)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(Cotation.verif_cotation("6A"))
