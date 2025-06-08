from csv import excel

from classes.task_manager import TaskManager

def show_menu():
    print("\n📝 SPRÁVCA ÚLOH")
    print("1. Pridať úlohu")
    print("2. Zobraziť úlohy")
    print("3. Označiť úlohu ako hotovú")
    print("4. Odstrániť úlohu")
    print("5. Označiť úlohu ako nehotovú")
    print("0. Ukončiť")

def main():
    manager = TaskManager()
    manager.load_from_file()

    while True:
        show_menu()
        choice = input("Zvoľ možnosť: ")

        if choice == "1":
            name = input("Názov úlohy: ")
            description = input("Popis (nepovinný): ")
            manager.add_task(name, description)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            try:
                id = int(input("Zadaj ID úlohy, ktorú chceš označiť ako hotovú: "))
                manager.mark_task_done(id)
            except ValueError:
                print("⚠️ Zadaj platné číslo.")

        elif choice == "4":
            try:
                id = int(input("Zadaj ID úlohy, ktorú chceš odstrániť: "))
                manager.delete_task(id)
            except ValueError:
                print("⚠️ Zadaj platné číslo.")

        elif choice == "5":
            try:
                id = int(input("Zadaj ID úlohy, ktorú chceš označiť ako nehotovú: "))
                manager.mark_task_undone(id)
            except ValueError:
                print("⚠️ Zadaj platné číslo.")


        elif choice == "0":
            print("👋 Ukončujem program. Maj pekný deň!")
            break

        else:
            print("⚠️ Neplatná voľba. Skús znova.")

if __name__ == "__main__":
    main()

