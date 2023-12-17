def zamena(massiv, index, znachenie):
    massiv[index] = znachenie.replace('\t', '    ')
    return massiv