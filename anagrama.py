def anagramas(palavra):
    if len(palavra) <=1:
        return palavra
    else:
        ana = []
        for auxi in anagramas(palavra[1:]):
            for i in range(len(palavra)):
                ana.append(auxi[:i] + palavra[0:1] + auxi[i:])
        return ana

print(anagramas('abcde'))