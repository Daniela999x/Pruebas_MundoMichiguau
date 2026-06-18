from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


def ejecutar_validacion_login():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    evidencia = "evidencias/03_validar_login.png"

    try:
        driver.get("https://mantistcy.cl/mundomichiguau/sitio/index.php")
        time.sleep(2)

        boton_menu = driver.find_element(By.CLASS_NAME, "navbar-toggler")
        boton_menu.click()
        time.sleep(1)

        boton_login = driver.find_element(By.LINK_TEXT, "Entrar")
        boton_login.click()
        time.sleep(2)

        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot(evidencia)

        contenido = driver.page_source

        if "Correo" in contenido and "Contraseña" in contenido:
            return (
                True,
                "Se valida que la pagina de inicio de sesion cargue correctamente.",
                "La pagina de login debe mostrar los campos Correo Electronico y Contraseña.",
                "La pagina de login cargo correctamente y mostro los campos esperados.",
                "Funcional ",
                evidencia
            )

        return (
            False,
            "Se valida que la pagina de inicio de sesion cargue correctamente.",
            "La pagina de login debe mostrar los campos Correo Electronico y Contraseña.",
            "La pagina cargo pero no se encontraron todos los campos esperados.",
            "Funcional ",
            evidencia
        )

    except Exception as error:
        return (
            False,
            "Se valida que la página de inicio de sesión cargue correctamente.",
            "La página de login debe mostrar correctamente el formulario.",
            f"Error durante la ejecución de Selenium: {error}",
            "Funcional ",
            evidencia
        )

    finally:
        driver.quit()