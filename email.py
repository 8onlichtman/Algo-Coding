
import re


def email(file_name):
    """

    :param file_name:
    :return: valid for a valid email address and invalid for an invalid email address
    """

    """
    >>> email("file.txt")
    hello@ is invalid
    gff@gmail.com is valid
    .dscksd@jnjn is invalid
    abc.def@mail-archive.com is valid
    abc.def@mail#archive.com is invalid
    hgvgv@hgv@hcyf.com is invalid
    """

    words = open(file_name, "r").read().split()
    for word in words:
        if re.fullmatch("[A-Za-z0-9]+([\._-]?[A-Za-z0-9])*[@][A-Za-z0-9-]*\.[A-Za-z0-9-]{2,}",word):
            print(word + " is valid")
        else:
            if re.fullmatch(".*[@].*", word):
                print(word + " is invalid")


