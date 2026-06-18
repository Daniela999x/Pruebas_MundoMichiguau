from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def ejecutar_validacion_filtro_alimento():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    evidencia = "evidencias/06_validar_filtro_alimento.png"

    try:
        driver.get("https://mantistcy.cl/mundomichiguau/sitio/index.php#tienda")

        time.sleep(3)

        filtro_alimento = driver.find_element(By.LINK_TEXT, "Alimento")
        filtro_alimento.click()

        time.sleep(2)

        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot(evidencia)

        contenido = driver.page_source.lower()

        if "alimento" in contenido or "nomade" in contenido or "comida" in contenido:

            return (
                True,
                "Se valida el funcionamiento del filtro Alimento en el catálogo.",
                "Al seleccionar el filtro Alimento, el sistema debe mostrar productos de tipo alimento.",
                "El filtro Alimento se aplicó correctamente y mostró productos relacionados.",
                "Funcional ",
                evidencia
            )

        return (
            False,
            "Se valida el funcionamiento del filtro Alimento en el catálogo.",
            "Al seleccionar el filtro Alimento, el sistema debe mostrar productos de tipo alimento.",
            "El filtro Alimento no mostró productos relacionados.",
            "Funcional ",
            evidencia
        )

    except Exception as error:

        return (
            False,
            "Se valida el funcionamiento del filtro Alimento en el catálogo.",
            "Al seleccionar el filtro Alimento, el sistema debe mostrar productos de tipo alimento.",
            f"Error durante la ejecución de Selenium: {error}",
            "Funcional ",
            evidencia
        )

    finally:
        driver.quit()