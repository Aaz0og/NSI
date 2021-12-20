def creer_file():
    x = []
    return x


def taille_file(file):
    return len(file)


def file_vide(file):
    if len(file) != 0:
        return False
    else:
        return True


def ajouter_file(file, x):
    return file.append(x)


def retirer_file(file):
    return file.pop(0)


def premier_file(file):
    return file[0]
#! BRUH