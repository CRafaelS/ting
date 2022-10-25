def exists_word(word, instance):
    word_lower = word.lower()
    result = []
    for index in instance._data:
        base_structure = {
            "palavra": word,
            "arquivo": index["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for i, words in enumerate(index["linhas_do_arquivo"]):
            if word_lower in words.lower():
                base_structure["ocorrencias"].append({"linha": i + 1})
        if len(base_structure["ocorrencias"]) > 0:
            result.append(base_structure)
    return result


def search_by_word(word, instance):
    word_lower = word.lower()
    result = []
    for index in instance._data:
        base_structure = {
            "palavra": word,
            "arquivo": index["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for i, words in enumerate(index["linhas_do_arquivo"]):
            if word_lower in words.lower():
                base_structure["ocorrencias"].append({
                        "linha": i + 1,
                        "conteudo": words
                        })
        if len(base_structure["ocorrencias"]) > 0:
            result.append(base_structure)
    return result
