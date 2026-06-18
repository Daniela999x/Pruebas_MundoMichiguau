from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


def ejecutar_validacion_carga_inicio():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    evidencia = "evidencias/01_validar_carga_inicio.png"

    try:
        url = "https://mantistcy.cl/mundomichiguau/sitio/index.php"
        driver.get(url)

        time.sleep(3)

        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot(evidencia)

        titulo_pagina = driver.title
        contenido_pagina = driver.page_source

        if "Mundo Michi Guau" in contenido_pagina:
            return (
                True,
                "Se valida la carga correcta de la página principal del sitio Mundo Michiguau.",
                "La página principal debe cargar correctamente y mostrar contenido del sitio.",
                f"La página cargó correctamente. Título detectado: {titulo_pagina}",
                "Funcional ",
                evidencia
            )

        return (
            False,
            "Se valida la carga correcta de la página principal del sitio Mundo Michiguau.",
            "La página principal debe cargar correctamente y mostrar contenido del sitio.",
            "La página cargó, pero no se encontró el texto esperado 'Mundo Michi Guau'.",
            "Funcional ",
            evidencia
        )

    except Exception as error:
        return (
            False,
            "Se valida la carga correcta de la página principal del sitio Mundo Michiguau.",
            "La página principal debe cargar correctamente y mostrar contenido del sitio.",
            f"Error durante la ejecución de Selenium: {error}",
            "Funcional ",
            evidencia
        )

    finally:
        driver.quit()