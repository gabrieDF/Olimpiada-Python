def pangrama(str): 
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for frase in alfabeto: 
        if frase not in str.lower(): 
            return False
  
    return True
      
palavra = input("Digite uma frase ou palavra: ")
if(pangrama(palavra) == True): 
    print("Esta palavra/frase é um pangrama") 
else: 
    print("Esta palavra/frase não é um pangrama") 