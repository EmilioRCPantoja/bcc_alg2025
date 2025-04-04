def countparts(frase, delim):
    tmp=frase.split(delim)
    return len(tmp)

def getpart(frase, delim, i):
    tmp=frase.split(delim)
    return tmp[i-1]
