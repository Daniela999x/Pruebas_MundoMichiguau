from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


def ejecutar_validacion_busqueda():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    evidencia = "evidencias/05_validar_busqueda.png"

    try:
        driver.get("https://mantistcy.cl/mundomichiguau/sitio/index.php#tienda")

        time.sleep(3)

        buscador = driver.find_element(By.NAME, "q")
        buscador.send_keys("perro")

        time.sleep(1)

        boton_buscar = driver.find_element(
            By.XPATH,
            "//button[contains(text(),'Buscar')]"
        )
        boton_buscar.click()

        time.sleep(2)

        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot(evidencia)

        contenido = driver.page_source.lower()

        if "perro" in contenido or "producto" in contenido:

            return (
                True,
                "Se valida el funcionamiento del buscador de productos.",
                "Al ingresar un término de búsqueda, el sistema debe mostrar productos relacionados.",
                "La búsqueda se ejecutó correctamente.",
                "Funcional ",
                evidencia
            )

        return (
            False,
            "Se valida el funcionamiento del buscador de productos.",
            "Al ingresar un término de búsqueda, el sistema debe mostrar productos relacionados.",
            "La búsqueda no mostró resultados relacionados.",
            "Funcional ",
            evidencia
        )

    except Exception as error:

        return (
            False,
            "Se valida el funcionamiento del buscador de productos.",
            "Al ingresar un término de búsqueda, el sistema debe mostrar productos relacionados.",
            f"Error durante la ejecución de Selenium: {error}",
            "Funcional ",
            evidencia
        )

    finally:
        driver.quit()