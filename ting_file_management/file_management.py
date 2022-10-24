import sys
import pathlib


def txt_importer(path_file):
    if not path_file:
        print(f"Arquivo {path_file} não encontrado\n", file=sys.stderr)
    if (pathlib.Path(path_file).suffix == ".txt"):
        print("Formato inválido\n", file=sys.stderr)
