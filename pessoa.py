import random

from pokemon import *

NOMES = ["João","Maria","Fernando" ,"Bruno" ,"Carlos" ,"Guilherme" ,"Vicnicios"]

POKEMONS = [
    PokemonFogo("charmander"),
    PokemonFogo("Flarion"),
    PokemonFogo("charmilion"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Magicarp") 
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[], dinheiro = 100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        
        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
        else:
            print("{} não tem pokemons".format(self))
        
    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("ERRO: Esse jogador não tem pokemons")
            
    def mostrar_dinheiro(self):
        print("Você possui $ {}".format(self.dinheiro))

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("Você ganhou ${}".format(quantidade))
        self.mostrar_dinheiro()

    def batalhar(self,pessoa):
        print("{} iniciou uma batalha com {}".format(self,pessoa))
        
        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()
        
        if pokemon and pokemon_inimigo:
            while True:
               vitoria = pokemon.atacar(pokemon_inimigo)
               if vitoria:
                print("{} ganhou a batalha".format(self))
                break
                
               vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
        else:
            print("Essa batalha não pode ocorrer !")

class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}!".format(self, pokemon))

    def escolher_pokemon(self):
        self.mostrar_pokemons()
        
        if self.pokemons:
            while True:
                escolha = input("Escolha o seu pokemon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{} eu escolho você!!!".format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("escolha invalida")
        else:
            print("esse jogador não possui nenhum pokemon para ser escolhido")

        
                

    def batalhar(self,pessoa):
        print("{} iniciou uma batalha com {}".format(self,pessoa))
        
        self.mostrar_pokemons()
        self.escolher_pokemon()


        if pokemon and Pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("você gnahou!")
                    break
                
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print("você perdeu")
                    break

        else:
            print("Essa batalha não pode ocorrer !!")

class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1,6)):
                pokemons.append(random.choice(POKEMONS))
        super().__init__(nome=None, pokemons=pokemons)