from integraciones.integracionMantis import enviar_resultado_mantis
from tests.test_01_validar_carga_inicio import ejecutar_validacion_carga_inicio
from tests.test_02_validar_registro import ejecutar_validacion_registro
from tests.test_03_validar_login import ejecutar_validacion_login
from tests.test_04_validar_catalogo import ejecutar_validacion_catalogo
from tests.test_05_validar_busqueda import ejecutar_validacion_busqueda
from tests.test_06_validar_filtro_alimento import ejecutar_validacion_filtro_alimento
from tests.test_07_validar_filtro_juguetes import ejecutar_validacion_filtro_juguetes
from tests.test_08_validar_filtro_accesorios import ejecutar_validacion_filtro_accesorios


def ejecutar_y_reportar(nombre_prueba, funcion_prueba):
    print(f"\nEjecutando: {nombre_prueba}")

    try:
        exito, descripcion, resultado_esperado, resultado_obtenido, tipo_prueba, evidencia = funcion_prueba()

        print(descripcion)
        print("Resultado obtenido:", resultado_obtenido)

        codigo, respuesta = enviar_resultado_mantis(
            resumen=nombre_prueba,
            descripcion=descripcion,
            resultado_esperado=resultado_esperado,
            resultado_obtenido=resultado_obtenido,
            tipo_prueba=tipo_prueba,
            evidencia=evidencia
        )

        print("Mantis respondió:", codigo)
        print(respuesta)

    except Exception as error:
        print(f"Error ejecutando {nombre_prueba}: {error}")


def main():
    print("Inicio de pruebas automatizadas - Mundo Michiguau")

    ejecutar_y_reportar(
        "Test 01 - Validar carga de inicio",
        ejecutar_validacion_carga_inicio
    )

    ejecutar_y_reportar(
        "Test 02 - Validar página de registro",
        ejecutar_validacion_registro
    )

    ejecutar_y_reportar(
        "Test 03 - Validar página de login",
        ejecutar_validacion_login
    )

    ejecutar_y_reportar(
        "Test 04 - Validar catálogo",
        ejecutar_validacion_catalogo
    )

    ejecutar_y_reportar(
        "Test 05 - Validar búsqueda de productos",
        ejecutar_validacion_busqueda
    )

    ejecutar_y_reportar(
        "Test 06 - Validar filtro Alimento",
        ejecutar_validacion_filtro_alimento
    )

    ejecutar_y_reportar(
        "Test 07 - Validar filtro Juguetes",
        ejecutar_validacion_filtro_juguetes
    )
    
    ejecutar_y_reportar(
        "Test 08 - Validar filtro Accesorios",
        ejecutar_validacion_filtro_accesorios
    )

    print("Fin de ejecución de pruebas automatizadas")


if __name__ == "__main__":
    main()