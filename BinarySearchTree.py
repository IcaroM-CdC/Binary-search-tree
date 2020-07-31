import os

class CreateNode:
    def __init__(self, key = None):
        
        self.key = key
        self.right = None
        self.left = None


class CreateTree:
    def __init__(self):
        pass

    # Exibindo a arvore de forma ordenada

    def sortTree (self ,root):
        if (not root):
            return

        self.sortTree(root.right)
        print(root.key)
        self.sortTree(root.left)

    # Inserindo um node
    
    def insertNode (self, root, node):
        if (root is None):
            root = node
        
        elif (root.key < node.key):
            if (root.right is None):
                root.right = node
            
            else:
                self.insertNode(root.right, node)

        elif (root.key > node.key):
            if (root.left is None):
                root.left = node
            
            else:
                self.insertNode(root.left, node)

    # Buscando um node

    def searchNode(self, root, key):

        # Caso a chave procurada não está presente
        if (root is None):
            return None

        # Caso a chave esteja na raiz
        if (root.key == key):
            return root

        # Caso a chave procurada seja maior que a raiz
        if (root.key < key):
            return self.searchNode(root.right, key)
        
        # Caso a chave procurada seja menor que a raiz
        if (root.key > key):
            return self.searchNode(root.left, key)

    # Mostra o resultado da busca de um nó
    def showSearchResult(self, root, key):
        result = self.searchNode(root, key)

        if (result):
            print("Busca pela chave {}: sucesso".format(key))
        else:
            print("Busca pela chave {}: fracasso".format(key))

    # Mostra os resultados de uma busca de multiplos nós
    def showMultipleSearchResults(self, root, keyArray):
        for key in keyArray:
            result = self.searchNode(root, key)

            if (result):
                print("Busca pela chave {}: sucesso".format(key))
            else:
                print("Busca pela chave {}: fracasso".format(key))

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
            print("9 -> Sair")
            print("********************************************")
            

            option = int(input())
            os.system("clear") or None

            tree = CreateTree()

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

            if (option == 5):

                try:
                    tree.sortTree(root)
                except UnboundLocalError:
                    print("Arvore não existente")
                    os.system("sleep 5")

Menu()
