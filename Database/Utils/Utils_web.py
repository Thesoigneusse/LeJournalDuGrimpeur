from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Classes.Cotation import Cotation

def extract_html(url):
    """Extrait le code html de la page à l'url donné

    Args:
        url (str): url de la page à traiter

    Returns:
        str: str du code de la page html à l'url donné
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    # Attendre le chargement de la page si nécessaire
    driver.implicitly_wait(10)

    try:
        # Récupérer le ou les blocs avec la classe "page-content is-block-print"
        page_content_elements = driver.find_elements(By.CSS_SELECTOR, "div.page-content.is-block-print")

        # Traiter chaque élément WebElement
        for element in page_content_elements:
            # Récupérer le HTML de l'élément
            element_html = element.get_attribute("outerHTML")

            # Traiter avec BeautifulSoup
            soup = BeautifulSoup(element_html, "html.parser")
            
            # Exemple : Extraire le texte dans ce bloc
    except Exception as e:
        print("Erreur :", e)

    # Fermer le navigateur
    driver.quit()
    return soup


def extract_info(soup: str, c2c_keyword: str) -> str:
    """Extrait les informations correspondant au keyword de c2c

    Args:
        soup (str): Texte du code html
        c2c_keyword (str): keyword de c2c

    Returns:
        str: valeur correspondant au keyword. "Non trouvé" si pas de keyword correspondant.
    """
    # Recherche du mot-clé dans le code HTML
    keyword_tag = soup.find("span", string=c2c_keyword)
    if keyword_tag:
        # Récupération du texte associé
        return keyword_tag.find_next("span").get_text(strip=False)
    else:
        return "Non trouvé"
    



















