from proyecto_final import *
import pytest
def main():
    test_nombre_pokemon()
    test_wallet_pokemons()
    test_new_wallet()

def test_nombre_pokemon():
    assert nombre_pokemon("Pikachu") == "Pikachu"

def test_wallet_pokemons():
    nombre = nombre_pokemon("Pikachu")
    lista = read_csv_file()
    n_a = wallet_pokemons(nombre,lista)
    assert wallet_pokemons(nombre,lista) == n_a



def test_new_wallet():
    name = nombre_pokemon("Pikachu")
    lista = read_csv_file()
    wallet = wallet_pokemons(name,lista)
    generate_p = generate_pokemon("yes")
    n_wallet = new_wallet(wallet,generate_p)
    assert new_wallet(wallet,generate_p) == n_wallet
    
if __name__ == "__main__":
    main()