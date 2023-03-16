nascimento=1997
nome='Emanuelly'
anoAtual=2023
nascimentojovem=2006

def calculoIdade (nascimento, anoAtual):
 idade= anoAtual-nascimento
 return idade 
idade=calculoIdade (nascimento, anoAtual)
idadeJovem=calculoIdade (nascimentojovem , anoAtual)
print('Idade é' + str (idade))
print('IdadeJovem' + str (idadeJovem))