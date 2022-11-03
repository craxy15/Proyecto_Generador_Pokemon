import csv
import sys
import random
from tabulate import tabulate

# Project name: Pokemon wallet generator

def main():
    menu = """"
    Select a leader:

    Bulbasaur   Charmander      Squirtle        Caterpie        Weedle
    Ivysaur     Charmeleon      Wartortle       Metapod         Pikachu
    Venusaur    Charizard       Blastoise       Butterfree

    """
    print(menu)
    nombre = input("Enter the leader name: ").strip().capitalize()
    nombre_inp = nombre_pokemon(nombre)
    lista_pokemons = read_csv_file()
    wallet_= wallet_pokemons(nombre_inp,lista_pokemons)
    quest = input("You need more pokemons? (yes/no)").lower().strip()
    generate_p = generate_pokemon(quest)
    new_wallet(wallet_,generate_p)
    read_csv_tabulate()

#Check the name input
def nombre_pokemon(nombre):
        lista_lider = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Pikachu"]
        if nombre in lista_lider:
            return nombre
        if nombre not in lista_lider :
            sys.exit("Choose a leader")
            

#Check the csv file and return a list
def read_csv_file():
    try:    
        lista_pokemon = []
        with open("Proyecto_f/nombres_pokemons.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                lista_pokemon.append({"name": row["name"], "especie": row["especie"], "habilidad": row["habilidad"], "color": row["color"], "velocidad": row["velocidad"], "fortaleza": row["fortaleza"], "precision": row["precision"], "resistencia": row["resistencia"], "salto": row["salto"],"identificador": row["identificador"]})
        return lista_pokemon
    except FileNotFoundError:
        sys.exit("File not found")

#Check the name if is in the list of csv file and return a new list if is name in list
def wallet_pokemons(name,lista):
    wallet=[]
    for line in lista:
        if name in line["name"]:
            print("The pokemon has been added to the wallet")
            wallet.append(line)
            return wallet
        

#Create the mold for the pokemon
class Pokemon:
    def __init__(self,name,especie,habilidad,color,velocidad,fortaleza,precision,resistencia,salto,identificador):
        self.name = name
        self.especie = especie
        self.habilidad = habilidad
        self.color = color
        self.velocidad = velocidad
        self.fortaleza = fortaleza
        self.precision = precision
        self.resistencia = resistencia
        self.salto = salto
        self.identificador = identificador
    #Implementing values to the attributes so that each time we call the object it generates a new character with random values
    @classmethod
    def get(cls):
        names = ["Goldshark","Voltrex","Persito","Magnetone","Steelcrow","Hipnotico","Electrocat","Vichar"]
        name = random.choice(names)
        especies = ["Semilla","Lagartija","Llama","Tortuguita","Tortuga","Armazon","Gusano","Capullo","Mariposa","Oruga","Raton"]
        especie = random.choice(especies)
        habilidades = ["Electricidad estatica","Mar llamas","Espesura","Pararrayos","Cabeza roca","Fuga","Absorbe fuego","Clorofila","Enjambre","Madrugar","Corte fuerte","Rompemoldes","Absorbtion electrica"]
        habilidad = random.choice(habilidades)
        colores = ["Rojo","Azul","Blanco","Amarillo","Gris","Negro","Naranja"]
        color = random.choice(colores)
        velocidad = random.randint(1,7)
        fortaleza = random.randint(1,7)
        precision = random.randint(1,7)
        resistencia = random.randint(1,7)
        salto = random.randint(1,7)
        identificador = random.randint(1000,9999)
        return cls(name,especie,habilidad,color,velocidad,fortaleza,precision,resistencia,salto,identificador)

#Generate new pokemons through the class in a new list with a maximum amount of five pokemons
def generate_pokemon(quest):
    wallet_2 =[]
    cantidad = 0
    while True:
        # more = input("Need more?(yes/no) ")
        if quest == "yes":
            pokemon = Pokemon.get()
            dict_pokemon = pokemon.__dict__
            # print("You have generated a pokemon")
            wallet_2.append(dict_pokemon)
            cantidad += 1
            if cantidad == 5:
                print("Your wallet is ready")
                break
        elif quest == "no":
            print("The CSV file of your wallet has been generated")
            break
        else :
            print("Choose a yes or no answer")
    return wallet_2
    

#Generating a csv file where we put together the first list (if the name coincided with the name of the list) and the second list (where the pokemons have been generated) generating a csv file (wallet) with the new pokemons
def new_wallet(wallet,generate_pokemon):
    new_wallet = wallet + generate_pokemon
    with open("Proyecto_f/wallet_pokemon.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "especie", "habilidad", "color", "velocidad", "fortaleza", "precision", "resistencia", "salto", "identificador"])
        writer.writerow({"name": "name", "especie": "especie", "habilidad": "habilidad", "color": "color", "velocidad": "velocidad", "fortaleza": "fortaleza", "precision": "precision", "resistencia": "resistencia", "salto": "salto", "identificador": "identificador" })
        for line in new_wallet:
            writer.writerow({"name": line["name"], "especie": line["especie"], "habilidad": line["habilidad"], "color": line["color"], "velocidad": line["velocidad"], "fortaleza": line["fortaleza"], "precision": line["precision"], "resistencia": line["resistencia"], "salto": line["salto"], "identificador": line["identificador"]})
    return list(new_wallet)   
#Read the generated csv file and print it to the console in a different visual format
def read_csv_tabulate():
    lista = []
    try:
        with open("Proyecto_f/wallet_pokemon.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                lista.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    print("Preview file:")
    print(tabulate(lista[1:], headers=lista[0],tablefmt="grid"))

if __name__ == "__main__":
    main()