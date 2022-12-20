from pokemon import*

from pessoa import*

def escolher_pokemon_inicial(player):
    print("Ola {}, Você podera escolher um pokemon que ira lhe acompanhar nessa jornada!".format(player))

    pikachu = PokemonEletrico("Pikachu", level=1)
    Charmander = PokemonFogo("Charmander", level=1)
    Squirtle = PokemonAgua("Squirtle", level=1)

    print("Você possui 3 escolhas: ")
    print("1 -", pikachu)
    print("2 -", Charmander)
    print("3 -", Squirtle)

    while True:
        escolha = input("Escolha o seu pokemon: ")

        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(Charmander)
            break
        elif escolha == "3":
            player.capturar(Squirtle)
            break
        else:
            print("Escolha invalida")

if __name__ == "__main__":
    print("----------------------------------------")
    print("Bem vindo ao game Pokemon de terminal")
    print("----------------------------------------")
    
    
    nome = input("Ola qual o seu nome ?: ")
    player = Player(nome)
    print("Olá {}, esse é um mundo habitado por pokemons,"
    "sua missão é se toranar um mestre pokemon".format(player))
    print("Capture o máximo de pokemons que conseguir para derrotar seus inimigos")
    player.mostrar_dinheiro()
    
    if player.pokemons:
        print("já vi que você tem alguns pokemons ")
        player.mostrar_pokemons()
    else:
        print("Você não tem nenhum pokemon, no entanto posso te ajudar com isso "
        "você pode escolher um pokemon para começar sua jornada!")
        escolher_pokemon_inicial(player)

    print("Pronto, agora você possui um pokemon, para testar suas habilidades enfrente "
    "seu arqui-rival desde o jardim de infância Gary")
    gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("squirtle", level=1)])
    player.batalhar(gary)
    
    while True:
        print("----------------------------------------")
        print("O que deseja fazer?")
        print("1 Explorar o mundão a fora")
        print("2 Lutar com um inimigo")
        print("0 Sair do jogo")
        escolha = input("Sua escolha: ")
        print("----------------------------------------")
        if escolha == "1":
            player.explorar()
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
        elif escolha == "0":
            print("Fechando o jogo")
            break
        else:
            print("Escolha inválida!")
