from edv_number import EDVNumber

def InputSearchEDV():
    search_edv = EDVNumber.validate_edv(str(input("Wprowadź szukany nr edv narzędzia: ")))

    return search_edv