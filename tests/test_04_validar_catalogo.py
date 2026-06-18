from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


def ejecutar_validacion_catalogo():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    evidencia = "evidencias/04_validar_catalogo.png"

    try:
        driver.get("https://mantistcy.cl/mundomichiguau/sitio/index.php")

        time.sleep(2)

        boton_catalogo = driver.find_element(By.LINK_TEXT, "Ver Catálogo")
        boton_catalogo.click()

        time.sleep(3)

        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot(evidencia)

        url_actual = driver.current_url

        if "catalogo" in url_actual.lower():

            return (
                True,
                "Se valida que el catálogo de productos cargue correctamente.",
                "Al seleccionar Ver Catálogo el sistema debe mostrar el catálogo de productos.",
                f"El catálogo cargó correctamente. URL detectada: {url_actual}",
                "Funcional ",
                evidencia
            )

        return (
            False,
            "Se valida que el catálogo de productos cargue correctamente.",
            "Al seleccionar Ver Catálogo el sistema debe mostrar el catálogo de productos.",
            f"No se detectó una página de catálogo. URL obtenida: {url_actual}",
            "Funcional ",
            evidencia
        )

    except Exception as error:

        return (
            False,
            "Se valida que el catálogo de productos cargue correctamente.",
            "Al seleccionar Ver Catálogo el sistema debe mostrar el catálogo de productos.",
            f"Error durante la ejecución de Selenium: {error}",
            "Funcional ",
            evidencia
        )

    finally:
        driver.quit()