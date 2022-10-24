import sys
import pathlib
import os


def txt_importer(path_file):
    if not os.path.exists(path_file):
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    elif not (pathlib.Path(path_file).suffix == ".txt"):
        return sys.stderr.write("Formato inválido\n")

    with open(path_file, "r") as file:
        file_text = file.read().splitlines()
        return file_text
