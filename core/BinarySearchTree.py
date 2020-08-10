import os
from methods import TreeMethods

class CreateNode:
    def __init__(self, key = None):
        
        self.key = key
        self.right = None
        self.left = None


class Menu:
    def __init__(self):
        
        option = 0

        while (option != 9):

            print("********************************************")
            print("1 -> Cria uma arvore")
            print("2 -> Insere um nó")
            print("3 -> Procura um nó")
            print("4 -> Procura vários nós")
            print("5 -> Retorna todos os nós")
            print("6 -> Retorna o menor elemento")
            print("7 -> Retorna o maior elemento")
            print("9 -> Sair")
            print("********************************************")
            

            option = int(input())
            os.system("clear") or None

            tree = TreeMethods.CreateTree()

            if (option == 1):

                rootKey = int(input("Insira o valor da raiz da arvore: "))
                root = CreateNode(rootKey)

            if (option == 2):

                key = int(input("Insira o valor do nó: "))
                node = CreateNode(key)
                
                tree.insertNode(root, node)

            if (option == 3):

                wantedKey = int(input("Insira a chave desejada: "))
                
                try:
                    tree.showSearchResult(root, wantedKey)
                except UnboundLocalError:
                    print("Arvore não existente")
                    os.system("sleep 5")
                    os.system("clear")

            if (option == 4):

                nodes = []
                print("Forneça uma entrada em branco para finalizar!")

                try:    
                    try:
                        while True:
                            requiredNode = int(input("Insira o valor requisitado: "))
                            nodes.append(requiredNode)
                    except ValueError:
                        print("Inserção finalizada!!!")

                        tree.showMultipleSearchResults(root, nodes)
                except UnboundLocalError:
                    print("Arvore não existente")
                    os.system("sleep 5")
                    os.system("clear")

            if (option == 5):

                try:
                    tree.sortTree(root)
                except UnboundLocalError:
                    print("Arvore não existente")
                    os.system("sleep 5")
                    os.system("clear")

            if (option == 6):

                try:
                    tree.smallerKey(root)
                except UnboundLocalError:
                    print("Arvore não existente")
                    os.system("sleep 5")
                    os.system("clear")

            if (option == 7):

                try:
                    tree.biggerKey(root)
                except UnboundLocalError:
                    print("Arvore não existente")
                    os.system("sleep 5")
                    os.system("clear")

            if (option == 449849849):

                key = int(input("Insira o valor do nó: "))

                try:
                    tree.deleteNode(root, node)
                except UnboundLocalError:
                    print("Arvore não existente")
                    os.system("sleep 5")
                    os.system("clear")

Menu()
