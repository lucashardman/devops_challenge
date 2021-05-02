import re


def sku_valido(sku):
    """" Valida SKU para conter apenas letras e números """""
    model = '^\w+$'
    fit = re.findall(model, sku)
    return fit


def barcode_valido(barcode):
    """" Valida código de barras para conter apenas números """""
    model = '^([\s\d]+)$'
    fit = re.findall(model, barcode)
    return fit
