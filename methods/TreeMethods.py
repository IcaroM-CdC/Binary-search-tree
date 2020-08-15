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
    
    def insertNode(self, root, node):
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

    # Deletando o nó

###################### EM CONSTRUÇÃO ##########################

    def deleteNode(self, node, key):
        if (node == True):

            # Caso exista algum filho
            if (node.right == None):
                return node.left

                print("Nó deletado com sucesso!!!")

            elif (node.left == None):
                return node.right

                print("Nó deletado com sucesso!!!")

            # Caso existem dois filhos    
            elif (node.right and node.left):
                if (node.key == key):
                    pass

                elif (node.key > key):
                    pass

                elif (node.key < key):
                    pass


            # Caso não existam filhos
            else:
                node = None

                print("Nó deletado com sucesso!!!")

#################################################################

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

    def biggerKey(self, root):
        node = root

        while (node.right is not None):
            node = node.right

        print(node.key)

    def smallerKey(self, root):
        node = root

        while (node.left is not None):
            node = node.left
            
        print(node.key)
