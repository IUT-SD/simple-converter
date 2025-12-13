# Convertisseur d'unités facile

def km_to_meters(km):
    return km * 1000

def meters_to_centimeters(m):
    return m * 100

def kg_to_g(kg):
    return kg * 1000


def show_menu():
    print("Convertisseur d'unités")
    print("1. Kilomètres en Mètres")
    print("2. Kilogrammes en Grammes")
    print("3. Quitter") 
    print("4. Mètres en Centimètre")

def main():
    while True:
        show_menu()
        choice = input("Choisissez une option (1-4): ")
        
        if choice == '1':
            km = float(input("Entrez la distance en kilomètres: "))
            meters = km_to_meters(km)
            print(f"{km} kilomètres = {meters} mètres\n")
        elif choice == '2':
            kg = float(input("Entrez le poids en kilogrammes: "))
            grams = kg_to_g(kg)
            print(f"{kg} kilogrammes = {grams} grammes\n")
        elif choice == '3':
            print("Fin du programme.")
            break
        elif choice == '4':
            meters = float(input("Entrez la distance en mètres: "))
            centi = meters_to_centimeters(meters)
            print(f"{meters} mètre = {centi} centimètre\n")
        else:
            print("Option invalide, veuillez réessayer.\n")
if __name__ == "__main__":
    main()  