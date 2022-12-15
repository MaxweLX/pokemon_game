from pokemon import*

from pessoa import*

def escolher_pokemon_inicial(player):
    print("Ola {}, Você podera escolher um pokemon que ira lhe acompanhar nessa jornada!".format(player))

    pikachu = PokemonEletrico("Pikachu", level=1)
    Charmander = PokemonFogo("Charmander", level=1)
    Squirtle = PokemonAgua("Squirtle", level=1)

    print("Você possui 3 escolhas: ")
    print("1 -", pikachu)
    print("1 -", Charmander)
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




player = Player("Maxwel")
player.mostrar_dinheiro()
player.capturar(PokemonEletrico("Pikachu", level=1))

inimigo1 = Inimigo(nome="Gary", pokemons=[PokemonAgua("squirtle", level=1)])

player.batalhar(inimigo1)