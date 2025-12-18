import os
import tkinter as tk
from tkinter import messagebox
from organisms import Organisms
from species import Species
from type import Type
from class1 import Class
from order import Order
from family import Family
from genus import Genus
def load_organisms_from_file(filename):
    organisms = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 4:
                name, obitanie, vid, characteristics = parts
            elif len(parts) == 3:
                name, obitanie, vid = parts
                characteristics = ""
            else:
                continue
            organism = Species(name, obitanie, vid, characteristics)
            organisms.append(organism)
    return organisms
def main():
    organisms = load_organisms_from_file('in.txt')
    query_name = input("Наименование обитателя: ")
    for organism in organisms:
        if organism.name.lower() == query_name.lower():
            print(organism.get_info())
            organism.print_inheritance_tree()
            break
    else:
        print("Обитатель не найден.")
if __name__ == "__main__":
    main()
