from Classes.Cotation import Cotation
from Classes.Secteur import Secteur
import json
import re
class Voie():
    def __init__(self, 
                id: int,
                nom: str,
                cotation : Cotation, 
                secteur: Secteur,
                longueur: int,
                lien_c2c = None,
                nb_points: int = None,
                altitude: int = None,
                duree: str = None,
                ):
        self.id = id
        self.nom = nom
        self.lien_c2c = lien_c2c
        self.cotation = Cotation(cotation)
        self.longueur = longueur
        self.nb_points = nb_points
        self.altitude = altitude
        self.secteur = secteur
        self.duree = duree


    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, value: int) -> None:
        assert isinstance(value, int), f"l'id de la voie doit être un nombre. Current type vs. value: {type(value)} vs. {value}"
        self._id = value

    @property
    def cotation(self) -> Cotation:
        return self._cotation
    @cotation.setter
    def cotation(self, value: Cotation):
        assert isinstance(value, Cotation), f"[DEBUG] La cotation doit être une Cotation. Current Type vs. value: {type(value)} vs. {value}"        
        self._cotation = value

    @property
    def nom(self) -> str:
        return self._nom
    @nom.setter
    def nom(self, value: str) -> None:
        assert isinstance(value, str), f"[DEBUG]Le nom de la voie doit être un String. Current type vs. value: {type(value)} vs. {value}"
        self._nom = value

    @property
    def lien_c2c(self) -> str:
        return self._lien_c2c
    @lien_c2c.setter
    def lien_c2c(self, value: str) -> None:
        assert isinstance(value, str) and bool(re.fullmatch(r"^https:\/\/www\.camptocamp\.org(\/[^\s]*)?$"), value), f"lien_c2c doit être un String qui appartenient au domaine https://www.camptocamp.org/. Current type vs. value: {type(value)} vs. {value}"
        self._lien_c2c = value

    @property
    def longueur(self) -> int:
        return self._longueur
    @longueur.setter
    def longueur(self, value: int):
        assert isinstance(value, int), f"La longueur de la voie doit être un nombre. Current type vs. value: {type(value)} vs. {value}"
        self._longueur = value

    @property
    def nb_points(self) -> int:
        return self._nb_points
    @nb_points.setter
    def nb_points(self, value: int) -> None:
        assert isinstance(value, int) and value >= 0, f"Le nombre de points de la voie doit être un nombre positif. Current type vs. value: {type(value)} vs. {value}"
        self._nb_points = value

    @property
    def altitude(self) -> int:
        return self._altitude
    @altitude.setter
    def altitude(self, value: int) -> None:
        assert isinstance(value, int) and value >= 0, f"L'altitude de la voie doit être un nombre positif. Current type vs. value: {type(value)} vs. {value}"
        self._altitude = value
    
    @property
    def secteur(self) -> Secteur:
        return self._secteur
    @secteur.setter
    def secteur(self, value: Secteur):
        assert isinstance(value, Secteur), f"[DEBUG] Le secteur de la voie doit être un Secteur. Current Type vs. value: {type(value)} vs. {value}"
        self._secteur = value

    @property
    def duree(self) -> str:
        return self._duree
    @duree.setter
    def duree(self, value: str) -> None:
        assert isinstance(value, str) and bool(re.fullmatch(r"^([1-9][0-9]*h(30)?|[1-9][0-9]*min)$", value)), f"La durée de la voie doit être une chaine de la forme HH:MM:SS. Current type vs. value: {type(value)} vs. {value}"
        self._duree = value

    def __json__(self):
        return str(self.__dict__)

    def __repr__(self):
        return json.dumps(str(self.__dict__))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(Voie("1", "6A", "THT", "c2c_link.com"))

