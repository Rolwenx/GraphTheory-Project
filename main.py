import os
import time

from utils import *

print("Welcome to our Graph Theory Project")
print("Presented by :")
time.sleep(0.5)
print("1. BAUDET Quentin")
time.sleep(0.5)
print("2. BEZOT Maxime")
time.sleep(0.5)
print("3. BRACONNIER Roxane")
time.sleep(0.5)
print("4. DUPONT Nicolas")
time.sleep(0.5)
print("5. NGASSA Yoke")
time.sleep(1)

def select_file():
    directory = os.getcwd()
    text_files = [f for f in os.listdir(str(directory+"/tables")) if f.endswith('.txt')]

    text_files = sorted(text_files, key=lambda x: (len(x), x))
    print("\nHere are all the automata available in the current directory:")
    for index, file in enumerate(text_files,1):
        if index not in [31,32,33,34,35]:
            print(index, ":", file)


    file_input = int(input("Enter the index of the automaton you want to use:\n>>> "))
    file = text_files[file_input - 1]
    file = file[:-4]

    return file

print("\nPlease select the file you want to import the graph from")
file = select_file()
graph = create_dict('tables/'+file+'.txt')
print("\nYou selected: ", file)

while True:

    print("\n Please select your action:")
    print("1. Display the matrix associated to the graph")
    print("2. Check properties of the graph")
    print("3. Compute the ranks")
    print("4. Compute the earliest dates, the latest dates, and the floats")
    print("5. Compute the critical path(s) and display it or them")
    print("6. Change the graph")
    print("7. Exit")
    action = int(input(">>> "))

    if action == 1:
        value_matrix(graph)
    elif action == 2:
        continue
    elif action == 3:
        continue
    elif action == 4:
        continue
    elif action == 5:
        continue
    elif action == 6:
        file = select_file()
        graph = create_dict('tables/'+file+'.txt')
        print("\nYou selected: ", file)
    elif action == 7:
        break
    else:
        while action not in [1,2,3,4,5,6,7]:
            print("Please select a valid action")
            action = int(input(">>> "))






test = create_dict('tables/easytest.txt')
print_graph(test)
print_vertices(test)
value_matrix(test)

print("GRAPH THEORY PROJECT FIRST FILE")