def getSalesTax(subtotal):
    salest=round(subtotal*.06,2)
    return salest

def getTotal(subt,salest):
    total=round(subt+salest,2)
    return total
    