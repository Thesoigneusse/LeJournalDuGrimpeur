from typing import List
from Classes.Cotation import Cotation

class Secteur():
    def __init__(self,
                 name: str,
                 rock_type: str,
                 site_climb_type: str,
                 rain: str,
                 nb_voie: int,
                 cot_min: Cotation, 
                 cot_max: Cotation,
                 haut_min: int,
                 haut_max: int,
                 climb_type: List[str],
                 temps_acces: str):
        self.name = name
        self.rock_type = rock_type
        self.site_climb_type = site_climb_type
        self.rain = rain
        self.nb_voie = nb_voie
        self.cot_min = cot_min
        self.cot_max = cot_max
        self.haut_min = haut_min
        self.haut_max = haut_max
        self.climb_type = climb_type
        self.temps_acces = temps_acces

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Le nom du secteur doit être une chaîne de caractères.")
        self._name = value

    @property
    def rock_type(self) -> str:
        return self._rock_type
    @rock_type.setter
    def rock_type(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Le type de rocher du secteur doit être une chaîne de caractères.")
        self._rock_type = value
    
    @property
    def site_climb_type(self) -> str:
        return self._site_climb_type
    @site_climb_type.setter
    def site_climb_type(self, value: str) -> None:
        site_climb_type = ['couenne', 'grande voie']
        if not isinstance(value, str) and not value in site_climb_type:
            raise ValueError(f"Le type de site de montagne du secteur doit être une chaîne de caractères comprise dans : {site_climb_type}. Current value: {value}")
        self._site_climb_type = value

    @property
    def rain(self) -> str:
        return self._rain
    @rain.setter
    def rain(self, value: str) -> None:
        rain_types = ['partiellement protégé', 'couvert']
        if not isinstance(value, str) and not value in rain_types:
            raise ValueError(f"Le type de pluie du secteur doit être une chaîne de caractères comprise dans : {rain_types}. Current value: {value}")
        self._rain = value

    @property
    def nb_voie(self) -> int:
        return self._nb_voie
    @nb_voie.setter
    def nb_voie(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Le nombre de voies du secteur doit être un entier positif.")
        self._nb_voie = value
    
    @property
    def cot_min(self) -> Cotation:
        return self._cot_min
    @cot_min.setter
    def cot_min(self, value: Cotation) -> None:
        if not isinstance(value, Cotation):
            raise ValueError("La cotation minimale du secteur doit être une instance de Cotation.")
        self._cot_min = value
    
    @property
    def cot_max(self) -> Cotation:
        return self._cot_max
    @cot_max.setter
    def cot_max(self, value: Cotation) -> None:
        if not isinstance(value, Cotation):
            raise ValueError("La cotation maximale du secteur doit être une instance de Cotation.")
        self._cot_max = value

    @property
    def haut_min(self) -> int:
        return self._haut_min
    @haut_min.setter
    def haut_min(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("La hauteur minimale du secteur doit être un entier positif.")
        self._haut_min = value

    @property
    def haut_max(self) -> int:
        return self._haut_max
    @haut_max.setter
    def haut_max(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("La hauteur maximale du secteur doit être un entier positif.")
        self._haut_max = value
    
    @property
    def climb_type(self) -> List[str]:
        return self._climb_type
    @climb_type.setter
    def climb_type(self, value: List[str]) -> None:
        climb_types = ['vertical', 'dévers-surplomb']
        if not isinstance(value, list) or not all([isinstance(climb_type, str) and climb_type in climb_types for climb_type in value]):
            raise ValueError(f"Les types de montée du secteur doivent être une liste de chaînes de caractères comprise dans : {climb_types}. Current value: {value}")
        self._climb_type = value

    @property
    def temps_acces(self) -> str:
        return self._temps_acces
    @temps_acces.setter
    def temps_acces(self, value: str) -> None:
        if not isinstance(value, str) and bool(re.fullmatch(r"^([1-9][0-9]*h(30)?|[1-9][0-9]*min)$", value)):
            raise ValueError("Le temps d'accès du secteur doit être une chaîne de caractères.")
        self._temps_acces = value

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    cot_min = Cotation("5b"),
    cot_max = Cotation("7a+")

    test = Secteur(name="Secteur de Test",
            rock_type="calcaire",
            site_climb_type="couenne",
            rain="partiellement protégé",
            nb_voie=20,
            cot_min=cot_min,
            cot_max=cot_max,
            haut_min=10,
            haut_max=50,
            climb_type=["vertical", "dévers-surplomb"],
            temps_acces="15min"
        )

















