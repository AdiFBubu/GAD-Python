from datetime import datetime

def create_files():
    with open("tasks.txt", 'w') as file:
        pass
    with open("categorii.txt", 'w') as file:
        pass



def menu():

    print("\n\nMeniu\n ")
    print("1. Listare date")
    print("2. Sortare")
    print("3. Filtrare date")
    print("4. Adaugare nou task in lista initiala")
    print("5. Editare detalii referitoare la task, data, persoana, categorie")
    print("6. Stergere task din lista initiala")
    print("7. Iesire din aplicatie")


def add_category(categorii):

    with open('categorii.txt', 'w') as file:
        print("Introduceti de la tastatura categoriile dorite: ")
        print("Daca ai finalizat operatia anterioara, introduceti litera: 'x'")
        categorie = input()
        while True:
            if categorie == 'x':
                print("Ai iesit din functionalitatea de adaugare categorii!\n")
                return
            else:
                if categorie in categorii:
                    print("Exista deja aceasta categorie inregistrata!\n")
                else:
                    categorii.append(categorie)
                    file.write(categorie)
                    file.write('\n')
            categorie = input()

def add_task(categorii, tasks):
    task_name = input("Introdu numele task-ului: ")
    date = input("Intodu data limita de realizare a task-ului: ")
    attr = date.split(' ')

    date = attr[0]
    time = attr[1]

    person = input("Introdu numele persoanei responsabile cu realizarea task-ului respectiv: ")
    category = input("Introduceti categoria din care face parte task-ul: ")
    if category not in categorii:
        print("Nu exista categoria introdusa!")
        return
    task = task_name + '/' + date+ '/'  + time + '/' + person + '/' + category
    if task in tasks:
        print("Acest task a fost introdus deja!")
        return
    tasks.append(task)

    with open('tasks.txt', 'a') as file:
        file.write(task)
        file.write('\n')
    print("Task adaugat cu succes!")

    return

def get_tasks():
    tasks_copy = []
    with open("tasks.txt", 'r') as file:
        for line in file.readlines():
            line = list(line)
            if line[-1] == '\n':
                line = line[:-1]
            line = ''.join(line)
            task_copy = line.split('/')
            tasks_copy.append(task_copy)
    return tasks_copy
def date_list():

    tasks_copy = get_tasks()
    print(tasks_copy)

    if len(tasks_copy) == 0:
        print("Nu exista niciun task inregistrat!")
    else:
        print("\n\nListarea datelor ordonate dupa categoria task-ului: ")
        sorted_tasks = sorted(tasks_copy, key = lambda x: x[4])
        for task in sorted_tasks:
            line = ""
            for text in task:
                line += text
                line += ' '
            print(line)

def sorting_menu():
    print("Meniu sortari: ")
    print("1. sortare ascendenta task")
    print("2. sortare descendenta task")
    print("3. sortare ascendenta data")
    print("4. sortare descendenta data")
    print("5. sortare ascendenta persoana responsabila")
    print("6. sortare descendenta persoana responsabila")
    print("7. sortare ascendenta categorie")
    print("8. sortare descendenta categorie")

def sorting():
    sorting_menu()
    try:
        cmd = int(input("Intodu cifra corespunzatoare operatiei dorite: "))
    except ValueError:
        print("Trebuie sa introduci o cifra!")
        return
    tasks_copy = get_tasks()
    if cmd == 1:
        sorted_tasks = sorted(tasks_copy, key = lambda x: x[0])
    elif cmd == 2:
        sorted_tasks = sorted(tasks_copy, key = lambda x: x[0], reverse = True)
    elif cmd == 3:
        sorted_tasks = sorted(tasks_copy, key = lambda x: datetime.strptime(x[1], "%d.%m.%Y"))
    elif cmd == 4:
        sorted_tasks = sorted(tasks_copy, key = lambda x: datetime.strptime(x[1], "%d.%m.%Y"), reverse = True)
    elif cmd == 5:
        sorted_tasks = sorted(tasks_copy, key = lambda x: x[3])
    elif cmd == 6:
        sorted_tasks = sorted(tasks_copy, key = lambda x: x[3], reverse = True)
    elif cmd == 7:
        sorted_tasks = sorted(tasks_copy, key = lambda x: x[4])
    elif cmd == 8:
        sorted_tasks = sorted(tasks_copy, key = lambda x: x[4], reverse = True)
    else:
        print("Nu ai introdus o cifra potrivita!")
        return
    print("\n\nTask-urile sortate sunt: ")
    for task in sorted_tasks:
        line = ""
        for text in task:
            line += text
            line += ' '
        print(line)

    return


create_files()
categorii = []
tasks = []
add_category(categorii)

while True:

    menu()
    try:
        cmd = int(input("Introdu cifra dorita: "))
    except ValueError:
        print("Trebuie sa introduci o cifra!")
        continue

    if cmd == 1:
        date_list()

    elif cmd == 2:
        sorting()

    if cmd == 4:
        add_task(categorii, tasks)

    if cmd == 7:
        break

