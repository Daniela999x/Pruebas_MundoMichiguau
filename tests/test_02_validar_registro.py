from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


def ejecutar_validacion_registro():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    evidencia = "evidencias/02_validar_registro.png"

    try:
        driver.get("https://mantistcy.cl/mundomichiguau/sitio/index.php")
        time.sleep(2)

        boton_menu = driver.find_element(By.CLASS_NAME, "navbar-toggler")
        boton_menu.click()
        time.sleep(1)

        boton_registrar = driver.find_element(By.LINK_TEXT, "Registrar")
        boton_registrar.click()
        time.sleep(2)

        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot(evidencia)

        contenido = driver.page_source

        if (
            "Nombre Completo" in contenido
            and "Correo Electrónico" in contenido
            and "Contraseña" in contenido
            and "Confirmar Contraseña" in contenido
            and "REGISTRARME" in contenido
        ):
            return (
                True,
                "Se valida que la página de registro cargue correctamente desde el botón Registrar.",
                "La página de registro debe mostrar los campos Nombre Completo, Correo Electrónico, Contraseña, Confirmar Contraseña y el botón Registrarme.",
                "La página de registro cargó correctamente y mostró todos los campos esperados.",
                "Funcional ",
                evidencia
            )

        return (
            False,
            "Se valida que la página de registro cargue correctamente desde el botón Registrar.",
            "La página de registro debe mostrar los campos Nombre Completo, Correo Electrónico, Contraseña, Confirmar Contraseña y el botón Registrarme.",
            "La página de registro cargó, pero no se encontraron todos los campos esperados.",
            "Funcional ",
            evidencia
        )

    except Exception as error:
        return (
            False,
            "Se valida que la página de registro cargue correctamente desde el botón Registrar.",
            "La página de registro debe mostrar correctamente el formulario de registro.",
            f"Error durante la ejecución de Selenium: {error}",
            "Funcional ",
            evidencia
        )

    finally:
        driver.quit()