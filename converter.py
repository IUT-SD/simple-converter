# Convertisseur d'unités facile

def km_to_meters(km):
    return km * 1000

def m_to_cm(m):
    return m*100

def kg_to_g(kg):
    return kg * 1000


def show_menu():
    print("Convertisseur d'unités")
    print("1. Kilomètres en Mètres")
    print("2. Mètre en Centimètres")
    print("3. Kilogrammes en Grammes")
    print("4. Quitter") 

def main():
    while True:
        show_menu()
        choice = input("Choisissez une option (1-4): ")
        
        if choice == '1':
            km = float(input("Entrez la distance en kilomètres: "))
            meters = km_to_meters(km)
            print(f"{km} kilomètres = {meters} mètres\n")
        elif choice == '2':
            m = float(input("Entrez la distance en mètres: "))
            cm = m_to_cm(m)
            print(f"{m} mètres = {cm} centimètres\n")
        elif choice == '3':
            kg = float(input("Entrez le poids en kilogrammes: "))
            grams = kg_to_g(kg)
            print(f"{kg} kilogrammes = {grams} grammes\n")
        elif choice == '4':
            print("Fin du programme.")
            break
        else:
            print("Option invalide, veuillez réessayer.\n")
if __name__ == "__main__":
    main()  