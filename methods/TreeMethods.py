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

    # Inserindo um no  
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
    def deleteNode(self, node, key):

        if (node == None):
            return node

        elif (node.key > key):
            node.left = self.deleteNode(node.left, key)

        elif (node.key < key):
            node.right = self.deleteNode(node.right, key)

        else:
            if (node.left == None and node.right == None):
                return None
            
            elif (node.left == None):
                return node.right

            elif (node.right == None):
                return node.left

            else:

                # Procura o menor número maior que o nó atual(Sucessor)
                substitute = self.smallerKey(node.right)

                # O nó atual passa a ter o valor do seu substituto
                node.key = substitute

                # O substituto é removido do seu local de origem 
                node.right = self.deleteNode(node.right, substitute)
                
        return node

    # Buscando um nó
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
 
        return node.key

    def smallerKey(self, root):
        node = root

        while (node.left is not None):
            node = node.left
            
        return node.key
