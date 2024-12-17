def criar_ficha():
    print("Bem-vindo ao gerador de fichas D&D 5e!")

    # Passo 1: Coleta de dados básicos
    nome = input("Digite o nome do personagem: ")

    # Escolha de raça
    racas = [
        "Humano", "Elfo", "Anão", "Halfling", "Dragonborn", "Gnomo", "Meio-Elfo", "Meio-Orc", "Tiefling"
    ]
    print("\nEscolha uma raça:")
    for i, raca in enumerate(racas, 1):
        print(f"{i}. {raca}")

    while True:
        try:
            escolha_raca = int(input("Digite o número correspondente à raça: "))
            if 1 <= escolha_raca <= len(racas):
                raca = racas[escolha_raca - 1]
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    # Escolha de classe
    classes = [
        "Guerreiro", "Mago", "Ladino", "Arqueiro", "Paladino", "Feiticeiro", "Bárbaro", "Clérigo", "Druida", 
        "Bardo", "Necromante", "Monge"
    ]
    print("\nEscolha uma classe:")
    for i, classe in enumerate(classes, 1):
        print(f"{i}. {classe}")

    while True:
        try:
            escolha_classe = int(input("Digite o número correspondente à classe: "))
            if 1 <= escolha_classe <= len(classes):
                classe = classes[escolha_classe - 1]
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    # Lista de antecedentes e suas características
    antecedentes = {
        "Nobre": {
            "Descrição": "Você vem de uma família de alta posição social.",
            "Proficiencias": ["História", "Persuasão"],
            "Ferramenta": "Conjunto de jogos",
            "Ouro": 25
        },
        "Forasteiro": {
            "Descrição": "Você cresceu longe da civilização, em harmonia com a natureza.",
            "Proficiencias": ["Sobrevivência", "Atletismo"],
            "Ferramenta": "Conjunto de ferramentas de escalada",
            "Ouro": 10
        },
        "Criminoso": {
            "Descrição": "Você tem um histórico de atividades ilegais.",
            "Proficiencias": ["Enganação", "Furtividade"],
            "Ferramenta": "Ferramentas de ladrão",
            "Ouro": 15
        },
        "Artista": {
            "Descrição": "Você é habilidoso em entreter e inspirar os outros.",
            "Proficiencias": ["Acrobacia", "Performance"],
            "Ferramenta": "Ferramentas de artista",
            "Ouro": 15
        },
        "Sábio": {
            "Descrição": "Você dedicou sua vida à busca de conhecimento.",
            "Proficiencias": ["Arcano", "História"],
            "Ferramenta": "Conjunto de caligrafia",
            "Ouro": 10
        },
        "Soldado": {
            "Descrição": "Você serviu em uma força militar e entende estratégias de combate.",
            "Proficiencias": ["Atletismo", "Intimidação"],
            "Ferramenta": "Ferramentas de jogo de guerra",
            "Ouro": 10
        },
        "Marinheiro": {
            "Descrição": "Você passou sua vida em navios, enfrentando as ondas.",
            "Proficiencias": ["Navegação", "Persuasão"],
            "Ferramenta": "Ferramentas de navegação",
            "Ouro": 10
        },
        "Heremita": {
            "Descrição": "Você viveu em isolamento, longe da civilização.",
            "Proficiencias": ["Medicina", "Religião"],
            "Ferramenta": "Kit de ervas",
            "Ouro": 5
        }, 
        "Aventureiro": {
            "Descrição": "Você sempre buscou emoção e novas experiências.",
            "Proficiencias": ["Acrobacia", "Sobrevivência"],
            "Ferramenta": "Kit de aventura",
            "Ouro": 15
            
        }
    }

    print("\nEscolha um antecedente:")
    antecedentes_lista = list(antecedentes.keys())
    for i, antecedente_nome in enumerate(antecedentes_lista, 1):
        print(f"{i}. {antecedente_nome} - {antecedentes[antecedente_nome]['Descrição']}")

    while True:
        try:
            escolha_antecedente = int(input("Digite o número correspondente ao antecedente: "))
            if 1 <= escolha_antecedente <= len(antecedentes_lista):
                antecedente = antecedentes_lista[escolha_antecedente - 1]
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    # Exibindo as escolhas feitas pelo usuário
    print(f"\nVocê escolheu o antecedente {antecedente}.")
    print(f"Proficiências: {', '.join(antecedentes[antecedente]['Proficiencias'])}")
    print(f"Ferramenta: {antecedentes[antecedente]['Ferramenta']}")
    print(f"Ouro: {antecedentes[antecedente]['Ouro']}")

    # Modificadores raciais
    modificadores = {
        "Humano": {},
        "Elfo": {"Destreza": 2},
        "Anão": {"Constituição": 2},
        "Halfling": {"Destreza": 2},
        "Dragonborn": {"Força": 2, "Carisma": 1},
        "Gnomo": {"Inteligência": 2},
        "Meio-Elfo": {"Carisma": 2},
        "Meio-Orc": {"Força": 2, "Constituição": 1},
        "Tiefling": {"Carisma": 2, "Inteligência": 1}
    }

    # Seleção de modificadores raciais
    atributos_raciais = modificadores.get(raca, {})

    # Exibindo os modificadores raciais
    print(f"\nModificadores raciais para {raca}:")
    for atributo, modificador in atributos_raciais.items():
        print(f"{atributo}: +{modificador}")

    # Perícias de classe
    pericias_classes = {
        "Guerreiro": ["Atletismo", "Intimidação", "Percepção", "Sobrevivência"],
        "Mago": ["Arcano", "História", "Investigação", "Religião"],
        "Ladino": ["Acrobacia", "Furtividade", "Percepção", "Prestidigitação"],
        "Arqueiro": ["Acrobacia", "Atletismo", "Percepção", "Sobrevivência"],
        "Paladino": ["Atletismo", "Intimidação", "Medicina", "Religião"],
        "Feiticeiro": ["Arcanismo", "Enganação", "Intimidação", "Persuasão"],
        "Bárbaro": ["Atletismo", "Intimidação", "Percepção", "Sobrevivência"],
        "Clérigo": ["Religião", "Medicina", "Persuasão", "Percepção"],
        "Druida": ["Arcanismo", "Medicina", "Sobrevivência", "Percepção"],
        "Bardo": ["Acrobacia", "Enganação", "Persuasão", "Performance"],
        "Necromante": ["Arcano", "História", "Intimidação", "Religião"],
        "Monge": ["Acrobacia", "Atletismo", "Percepção", "Religião"]
    }

    # Exibindo as perícias de classe e permitindo escolha
    print(f"\nEscolha 2 perícias para a classe {classe}:")
    pericias_disponiveis = pericias_classes.get(classe, [])
    for i, pericia in enumerate(pericias_disponiveis, 1):
        print(f"{i}. {pericia}")

    habilidades_escolhidas = []
    while len(habilidades_escolhidas) < 2:
        try:
            escolha_pericia = int(input(f"Escolha a {len(habilidades_escolhidas)+1}ª perícia: "))
            if 1 <= escolha_pericia <= len(pericias_disponiveis):
                pericia = pericias_disponiveis[escolha_pericia - 1]
                if pericia not in habilidades_escolhidas:
                    habilidades_escolhidas.append(pericia)
                else:
                    print("Você já escolheu essa perícia. Escolha outra.")
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    # Exibindo a ficha final
    print("\nFicha do Personagem:")
    print(f"Nome: {nome}")
    print(f"Raça: {raca}")
    print(f"Classe: {classe}")
    print(f"Antecedente: {antecedente}")
    print(f"Proficiências raciais: {', '.join(antecedentes[antecedente]['Proficiencias'])}")
    print(f"Ferramenta: {antecedentes[antecedente]['Ferramenta']}")
    print(f"Ouro: {antecedentes[antecedente]['Ouro']}")
    print(f"Modificadores raciais: {', '.join([f'{atributo}: +{modificador}' for atributo, modificador in atributos_raciais.items()])}")
    print(f"Perícias de classe: {', '.join(habilidades_escolhidas)}")

criar_ficha()