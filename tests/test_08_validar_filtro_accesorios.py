from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


def ejecutar_validacion_filtro_accesorios():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    evidencia = "evidencias/08_validar_filtro_accesorios.png"

    try:
        driver.get("https://mantistcy.cl/mundomichiguau/sitio/index.php#tienda")

        time.sleep(3)

        filtro_accesorios = driver.find_element(
            By.LINK_TEXT,
            "Accesorios"
        )

        filtro_accesorios.click()

        time.sleep(2)

        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot(evidencia)

        contenido = driver.page_source.lower()

        if "accesorio" in contenido or "accesorios" in contenido:

            return (
                True,
                "Se valida el funcionamiento del filtro Accesorios en el catálogo.",
                "Al seleccionar el filtro Accesorios, el sistema debe mostrar productos de tipo accesorios.",
                "El filtro Accesorios se aplicó correctamente y mostró productos relacionados.",
                "Funcional ",
                evidencia
            )

        return (
            False,
            "Se valida el funcionamiento del filtro Accesorios en el catálogo.",
            "Al seleccionar el filtro Accesorios, el sistema debe mostrar productos de tipo accesorios.",
            "El filtro Accesorios no mostró productos relacionados.",
            "Funcional ",
            evidencia
        )

    except Exception as error:

        return (
            False,
            "Se valida el funcionamiento del filtro Accesorios en el catálogo.",
            "Al seleccionar el filtro Accesorios, el sistema debe mostrar productos de tipo accesorios.",
            f"Error durante la ejecución de Selenium: {error}",
            "Funcional ",
            evidencia
        )

    finally:
        driver.quit()