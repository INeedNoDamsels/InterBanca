#!/usr/bin/python
import sys
import glob

"""
Pueden utilizar este script para ejecutar los tests dentro de Thonny.
(ejecutenló como otro programa)
"""


def generador_bloque(mensaje, ancho=80):
    print("~" * 10)
    print(mensaje)
    print("~" * 10)


def do_pytest():
    try:
        import pytest

        generador_bloque("Comenzando tests")
        pytest.main()
    except ImportError as exc:
        print("Pylint no disponible")


def do_pylint():
    try:
        from pylint.lint import Run as RunPylint

        generador_bloque("Ejecutando Pylint")
        sources = list(glob.glob("src/practica/*.py"))
        tests = list(glob.glob("tests/*.py"))
        archivos = sources + tests
        RunPylint(archivos)
    except ImportError as exc:
        print("Pylint no disponible")


def do_codestyle():

    try:
        import pycodestyle

        generador_bloque("Ejecutando codestyle")
        style = pycodestyle.StyleGuide()
        style.input_dir(".")
    except ImportError as exc:
        print("PyCodeStyle no disponible")


if __name__ == "__main__":
    sys.path.append("src")
    do_pytest()
    do_codestyle()
    do_pylint()
