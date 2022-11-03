
# Pokemon wallet generator
#### Video Demo:  <URL HERE>
#### Description:
Hello , this is a project in python in which it is about reading a csv file where we can choose a character as a leader and create other characters randomly saving all the characters in a new csv file and presenting it in a table format in the terminal.

## Libraries that have been implemented

```
import csv
import sys
import random
from tabulate import tabulate
```

## Functions that have been implemented

### 1.Check the name input
We verify if the value of the input is in the character list. If it is true, the function will return the value of the input, otherwise the program will close
```
def nombre_pokemon(nombre):
        lista_lider = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Pikachu"]
        if nombre in lista_lider:
            return nombre
        if nombre not in lista_lider :
            sys.exit("Choose a leader")

```

### 2.Check the csv file
We look for the csv file and we are going to read it, in case the file is not found the program will close and it will return "File not found".
Once the file is opened, all the values will be passed to an (empty) list and the function will return the list with the values of the file

```
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
```

### 3.Check the name if is in the list of csv file and return a new list if is name in list
We take the value of the first function and the second. If the name matches the value of the "name" key, the corresponding dictionary will be added to a new list.
```
def wallet_pokemons(name,lista):
    wallet=[]
    for line in lista:
        if name in line["name"]:
            print("The pokemon has been added to the wallet")
            wallet.append(line)
            return wallet
```
### 4.Create the mold for the pokemon

```
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
```
### Implementing values to the attributes so that each time we call the object it generates a new character with random values

```
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
```
### 5.Generate new pokemons through the class in a new list with a maximum amount of five pokemons

```
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
```

### 6.Generating a csv file where we put together the first list (if the name coincided with the name of the list) and the second list (where the pokemons have been generated) generating a csv file (wallet) with the new pokemons
```
def new_wallet(wallet,generate_pokemon):
    new_wallet = wallet + generate_pokemon
    with open("Proyecto_f/wallet_pokemon.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "especie", "habilidad", "color", "velocidad", "fortaleza", "precision", "resistencia", "salto", "identificador"])
        writer.writerow({"name": "name", "especie": "especie", "habilidad": "habilidad", "color": "color", "velocidad": "velocidad", "fortaleza": "fortaleza", "precision": "precision", "resistencia": "resistencia", "salto": "salto", "identificador": "identificador" })
        for line in new_wallet:
            writer.writerow({"name": line["name"], "especie": line["especie"], "habilidad": line["habilidad"], "color": line["color"], "velocidad": line["velocidad"], "fortaleza": line["fortaleza"], "precision": line["precision"], "resistencia": line["resistencia"], "salto": line["salto"], "identificador": line["identificador"]})
    return list(new_wallet)
```
### 7.Read the generated csv file and print it to the console in a different visual format

```
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
```