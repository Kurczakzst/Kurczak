def pokaz_menu():
    print("\n--- MOJA LISTA ZADAŃ ---")
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Wyjdź")

def main():
    zadania = []
    
    while True:
        pokaz_menu()
        wybor = input("Wybierz opcję (1-4): ")

        if wybor == '1':
            if not zadania:
                print("\nTwoja lista jest pusta.")
            else:
                print("\nTWOJE ZADANIA:")
                for i, zadanie in enumerate(zadania, 1):
                    print(f"{i}. {zadanie}")
        
        elif wybor == '2':
            nowe_zadanie = input("Wpisz treść zadania: ")
            zadania.append(nowe_zadanie)
            print("Zadanie dodane!")
        
        elif wybor == '3':
            if not zadania:
                print("\nNie ma czego usuwać.")
            else:
                try:
                    nr = int(input("Podaj numer zadania do usunięcia: "))
                    zadania.pop(nr - 1)
                    print("Zadanie usunięte.")
                except (ValueError, IndexError):
                    print("Błędny numer!")
        
        elif wybor == '4':
            print("Do widzenia!")
            break
        else:
            print("Niepoprawny wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()
