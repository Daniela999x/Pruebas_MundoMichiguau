from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


def ejecutar_validacion_filtro_juguetes():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    evidencia = "evidencias/07_validar_filtro_juguetes.png"

    try:
        driver.get("https://mantistcy.cl/mundomichiguau/sitio/index.php#tienda")
        time.sleep(3)

        filtro_juguetes = driver.find_element(By.LINK_TEXT, "Juguetes")
        filtro_juguetes.click()
        time.sleep(2)

        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot(evidencia)

        contenido = driver.page_source.lower()

        if "juguete" in contenido or "juguetes" in contenido:

            return (
                True,
                "Se valida el funcionamiento del filtro Juguetes en el catálogo.",
                "Al seleccionar el filtro Juguetes, el sistema debe mostrar productos de tipo juguetes.",
                "El filtro Juguetes se aplicó correctamente y mostró productos relacionados.",
                "Funcional ",
                evidencia
            )

        return (
            False,
            "Se valida el funcionamiento del filtro Juguetes en el catálogo.",
            "Al seleccionar el filtro Juguetes, el sistema debe mostrar productos de tipo juguetes.",
            "El filtro Juguetes no mostró productos relacionados.",
            "Funcional ",
            evidencia
        )

    except Exception as error:

        return (
            False,
            "Se valida el funcionamiento del filtro Juguetes en el catálogo.",
            "Al seleccionar el filtro Juguetes, el sistema debe mostrar productos de tipo juguetes.",
            f"Error durante la ejecución de Selenium: {error}",
            "Funcional ",
            evidencia
        )

    finally:
        driver.quit()