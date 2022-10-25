from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    text_file = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text_file),
        "linhas_do_arquivo": text_file,
    }
    if any(
        file_name["nome_do_arquivo"] == path_file
        for file_name in instance._data
    ):
        return
    instance.enqueue(result)
    return sys.stdout.write(str(result))


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")

    path_file = instance._data[0]["nome_do_arquivo"]
    instance.dequeue()
    sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    if position >= (instance.__len__()) or position < 0:
        return sys.stderr.write("Posição inválida\n")
    return sys.stdout.write(str(instance.search(position)))
