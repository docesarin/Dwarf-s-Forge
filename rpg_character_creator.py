# primeiro vou definir todas as coisas que falta para o user poder fazer um de cada vez

nomeFeito = False

def nomePersonagem():
    nomePersonagem = input("Qual o nome do seu personagem? ")
    nomeFeito = True

def raca():
    print("Qual a raça do seu personagem?")
    raca = {
        "Anão":{
            "habilidade":"Seu valor de Constituição aumenta em 2."
        }
    }