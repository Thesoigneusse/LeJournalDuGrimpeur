import re
import json

class Cotation():
    # Liste des cotations possibles 
    possible_libre = ["2",
                    "3A", "3A+", "3B", "3B+", "3C", "3C+", 
                    "4A", "4A+", "4B", "4B+", "4C", "4C+", 
                    "5A", "5A+", "5B", "5B+", "5C", "5C+",
                    "6A", "6A+", "6B", "6B+", "6C", "6C+", 
                    "7A", "7A+", "7B", "7B+", "7C", "7C+", 
                    "8A", "8A+", "8B", "8B+", "8C", "8C+",
                    "9A", "9A+", "9B", "9B+", "9C", "9C+", 
                    ]
    possible_artif = ["A0", "A0+", 
                    "A1", "A1+", 
                    "A2", "A2+", 
                    "A3", "A3+",
                    "A4", "A4+", 
                    "A5", "A5+", 
                    "A6", "A6+"]
    possible_globa = ["PD", 
                    "AD-", "AD", "AD+", 
                    "D-", "D", "D+", 
                    "TD-", "TD", "TD+", 
                    "ED-", "ED", "ED+"]
    possible_engag = ["I", "II", "III", "IV"]
    possible_risqu = ["X1", "X2", "X3", "X4", "X5"]
    possible_equip = ["P1", "P1+", "P2", "P2+", "P3", "P3+", "P4", "P4+"]
    possible_expos = ["E1", "E2", "E3", "E4", "E5", "E6"]
    def __init__(self, 
                 libre: str = None, 
                 globale: str = None,  
                 obligatoire: str = None,  
                 artificielle: str = None , 
                 engagement: str = None, 
                 risque: str = None, 
                 equipement: str = None,
                 exposition: str = None
                 ):
        """Initialise une cotation
        Args:
            _libre (str): cotation d'escalade
        # >>> Cotation(libre = "6A", globale = "D+")
        # "{'_libre': '6A', '_globale': 'D+'}"
        """
        self.libre = libre 
        self.globale = globale
        self.obligatoire = obligatoire
        self.artificielle = artificielle
        self.engagement = engagement
        self.equipement = equipement
        self.risque = risque
        self.exposition = exposition


    @property
    def libre(self) -> str:
        """Retourne la libre

        Returns:
            str: libre : [3A, 3A+, 3B, etc]
        """
        return self._libre
    @libre.setter
    def libre(self, value: str) -> None:
        assert value is None or self.verif_libre(value), f"La cotation libre n'est pas correct. Current value vs. correct value: {value} vs. {self.possible_libre}"
        self._libre = value

    @property
    def globale(self) -> str:
        return self._globale
    @globale.setter
    def globale(self, value: str) -> None:
        assert value is None or self.verif_globale(value), f"La cotation globale n'est pas correcte. Current value vs. correct value: {value} vs. {Cotation.possible_globa}"
        self._globale = value

    @property
    def obligatoire(self) -> str:
        return self._obligatoire
    @obligatoire.setter
    def obligatoire(self, value: str) -> None:
        assert value is None or self.verif_obligatoire(value), f"La cotation obligatoire n'est pas correcte. Current value vs. correct value: {value} vs. {Cotation.possible_libre}"
        self._obligatoire = value

    @property
    def artificielle(self) -> str:
        return self._artificielle
    @artificielle.setter
    def artificielle(self, value: str) -> None:
        assert value is None or self.verif_artificielle(value), f"La cotation artificielle n'est pas correcte. Current value vs. correct value: {value} vs. {Cotation.possible_artif}"
        self._artificielle = value

    @property
    def engagement(self) -> str:
        return self._engagement
    @engagement.setter
    def engagement(self, value: str) -> None:
        assert value is None or self.verif_engagement(value), f"La cotation d'engagement n'est pas correcte. Current value vs. correct value: {value} vs. {Cotation.possible_engag}"
        self._engagement = value

    @property
    def equipement(self) -> str:
        return self._equipement
    @equipement.setter
    def equipement(self, value: str) -> None:
        assert value is None or self.verif_equipement(value), f"La cotation d'équipement n'est pas correcte. Current value vs. correct value: {value} vs. {Cotation.possible_equip}"
        self._equipement = value

    @property
    def risque(self) -> str:
        return self._risque
    @risque.setter
    def risque(self, value: str) -> None:
        assert value is None or self.verif_risque(value), f"La cotation de risque n'est pas correcte. Current value vs. correct value: {value} vs. {Cotation.possible_risqu}"
        self._risque = value

    @staticmethod
    def verif_libre(value: str) -> bool:
        """Vérifie que la cotation est possible

        Args:
            value (str): cotation à tester

        Returns:
            bool: True: la cotation existe, False: la cotation n'existe pas

        ToDo:
            - Prendre en compte les différents types de cotations
        >>> print(Cotation.verif_libre("6A"))
        True
        >>> print(Cotation.verif_libre("1A"))
        False
        >>> print(Cotation.verif_libre("5C+"))
        True
        >>> print(Cotation.verif_libre("7D"))
        False
        >>> print(Cotation.verif_libre("7C-"))
        False
        """
        return value in Cotation.possible_libre
        # assert isinstance(value, str) and bool(re.fullmatch(pattern=r"^[2-9]([A-C]?\+?)?$", string=value)), f"Cotation libre erronée. Value: {value}"
            
    @staticmethod
    def verif_globale(value: str) -> bool:
        """Vérifie que la cotation globale est possible. c-a-d: PD, AD-, AD, AD+, D-, D, D+, TD-, TD, TD+, ED-, ED, ED+

        Args:
            value (str): valeur de la cotation globale

        Returns:
            bool: True: la cotation existe, False: la cotation n'existe pas

        >>> print(Cotation.verif_globale("AD-"))
        True
        >>> print(Cotation.verif_globale("AD*"))
        False
        >>> print(Cotation.verif_globale("RD"))
        False
        >>> print(Cotation.verif_globale("TD"))
        True
        
        """
        return value in Cotation.possible_globa
        # assert isinstance(value, str) and bool(re.fullmatch(pattern=r"^(PD|AD|D|TD|ED)([-+]?)$", string=value)), f"Cotation globale erronée. Value: {value}"

    @staticmethod
    def verif_obligatoire(value: str) -> bool:
        """Vérifie que la cotation est possible

        Args:
            value (str): cotation à tester

        Returns:
            bool: True: la cotation existe, False: la cotation n'existe pas

        ToDo:
            - Prendre en compte les différents types de cotations
        >>> print(Cotation.verif_libre("6A"))
        True
        >>> print(Cotation.verif_libre("1A"))
        False
        >>> print(Cotation.verif_libre("5C+"))
        True
        >>> print(Cotation.verif_libre("7D"))
        False
        >>> print(Cotation.verif_libre("7C-"))
        False
        """
        return value in Cotation.possible_libre
        # assert isinstance(value, str) and bool(re.fullmatch(pattern=r"^[2-9]([A-C]?\+?)?$", string=value)), f"Cotation obligatoire erronée. Value: {value}"

    @staticmethod
    def verif_artificielle(value: str) -> bool:
        """Vérifie que la cotation est possible

        Args:
            value (str): cotation à tester

        Returns:
            bool: True: la cotation existe, False: la cotation n'existe pas

        ToDo:
            - Prendre en compte les différents types de cotations
        >>> print(Cotation.verif_artificielle("A0"))
        True
        >>> print(Cotation.verif_artificielle("A1+"))
        True
        >>> print(Cotation.verif_artificielle("B0"))
        False
        >>> print(Cotation.verif_artificielle("A"))
        False
        >>> print(Cotation.verif_artificielle("A7"))
        False
        """
        return value in Cotation.possible_artif
        # assert bool(re.fullmatch(pattern=r"^A([0-5]\+?|6)$", string=value)), f"Cotation obligatoire erronée. Value: {value}"

    @staticmethod
    def verif_engagement(value: str) -> bool:
        """Vérifie que la cotation est possible

        Args:
            value (str): cotation à tester

        Returns:
            bool: True: la cotation existe, False: la cotation n'existe pas

        ToDo:
            - Prendre en compte les différents types de cotations
        >>> print(Cotation.verif_engagement("I"))
        True
        >>> print(Cotation.verif_engagement("L"))
        False
        >>> print(Cotation.verif_engagement("II"))
        True
        >>> print(Cotation.verif_engagement("V"))
        False
        >>> print(Cotation.verif_engagement("IV"))
        True
        """
        return value in Cotation.possible_engag
        # assert value in ['I', 'II', 'III', 'IV'], f"Cotation obligatoire erronée. Value: '{value}'"

    @staticmethod
    def verif_equipement(value: str) -> bool:
        """Vérifie que la cotation est possible

        Args:
            value (str): cotation à tester

        Returns:
            bool: True: la cotation existe, False: la cotation n'existe pas

        ToDo:
            - Prendre en compte les différents types de cotations
        >>> print(Cotation.verif_equipement("P0"))
        False
        >>> print(Cotation.verif_equipement("P1+"))
        True
        >>> print(Cotation.verif_equipement("P2"))
        True
        >>> print(Cotation.verif_equipement("P5"))
        False
        >>> print(Cotation.verif_equipement("A1"))
        False
        """
        return value in Cotation.possible_equip
        # assert bool(re.fullmatch(pattern=r"^P([1-4]\+?)$", string=value)), f"Cotation equipement erronée. Value: {value}"

    @staticmethod
    def verif_exposition(value: str) -> bool:
        """Vérifie que la cotation est possible

        Args:
            value (str): cotation à tester

        Returns:
            bool: True: la cotation existe, False: la cotation n'existe pas

        ToDo:
            - Prendre en compte les différents types de cotations
        >>> print(Cotation.verif_exposition("E1"))
        True
        >>> print(Cotation.verif_exposition("e2"))
        False
        >>> print(Cotation.verif_exposition("K3"))
        False
        >>> print(Cotation.verif_exposition("E5"))
        True
        >>> print(Cotation.verif_exposition("E7"))
        False
        """
        return value in Cotation.possible_expos
        

    @staticmethod
    def verif_risque(value: str) -> bool:
        """Vérifie que la cotation est possible

        Args:
            value (str): cotation à tester

        Returns:
            bool: True: la cotation existe, False: la cotation n'existe pas

        Tests:            
        >>> print(Cotation.verif_risque("X1"))
        True
        >>> print(Cotation.verif_risque("X6"))
        False
        >>> print(Cotation.verif_risque("E3"))
        False
        >>> print(Cotation.verif_risque("P5"))
        False
        >>> print(Cotation.verif_risque("x5"))
        False
        """
        return value in Cotation.possible_risqu
        

    def all_verif(self, libre, globale, obligatoire, artificielle, engagement, risque, equipement, exposition) -> bool:
        """Vérifie que toutes les cotations sont valides"""
        return { "libre": Cotation.verif_libre(libre),
                "globale": Cotation.verif_globale(globale),
                "obligatoire": Cotation.verif_obligatoire(obligatoire),
                "artificielle": Cotation.verif_artificielle(artificielle),
                "engagement": Cotation.verif_engagement(engagement),
                "risque": Cotation.verif_risque(risque),
                "equipement": Cotation.verif_equipement(equipement),
                "exposition": Cotation.verif_exposition(exposition)}

    


    def __json__(self):
        return self.__dict__

    def __repr__(self):
        return json.dumps(str(self.__dict__))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
