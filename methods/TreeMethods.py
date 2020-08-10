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

    def deleteNode(self, root, node):
        if (node):

            # Caso exista algum filho
            if (node.right):
                newNode = node.right

                node = None
                
                self.insertNode(root, newNode)
                print("Nó deletado com sucesso!!!")

            # Caso existem dois filhos    
            if (node.right and node.left):
                newNodeRight = node.right
                newNodeLeft = node.left

                node = None

                self.insertNode(root, newNodeRight)
                self.insertNode(root, newNodeLeft)

            # Caso não existam filhos
            else:
                node = None

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
