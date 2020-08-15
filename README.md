## Arvore binária de pesquisa
    Uma árvore binária de pesquisa, em ingles binary search tree(BST), é uma estrutura de
    dados baseada em nós, onde todos os nós da subárvore esquerda possuem um valor numérico
    inferior ao nó raiz e todos os nós da subárvore direita possuem um valor superior ao nó
    raiz (esta é a forma padrão, podendo as subárvores serem invertidas, dependendo da 
    aplicação).
 

### Elementos

    - Nós - são todos os itens guardados na árvore
    - Raiz - é o nó do topo da árvore
    - Filhos - são os nós que vem depois dos outros nós
    - Pais - são os nós que vem antes dos outros nós
    - Folhas - são os nós que não têm filhos, são os últimos nós da árvore

### Percusos

    Em uma árvore binária de busca podem-se fazer os três percursos que se fazem para qualquer árvore 
    binária (percursos em inordem, pré-ordem e pós-ordem). É interessante notar que, quando se faz um
    percurso em ordem em uma árvore binária de busca, os valores dos nós aparecem em ordem crescente. A 
    operação "Percorre" tem como objetivo percorrer a árvore numa dada ordem, enumerando os seus nós. 
    Quando um nó é enumerado, diz-se que ele foi "visitado". 

    - Pré-ordem (ou profundidade):

        Visita a raiz
        Percorre a subárvore esquerda em pré-ordem
        Percorre a subárvore direita em pré-ordem

    - Ordem Simétrica:

        Percorre a subárvore esquerda em ordem simétrica
        Visita a raiz
        Percorre a subárvore direita em ordem simétrica

    - Pós-ordem:

        Percorre a subárvore esquerda em pós-ordem
        Percorre a subárvore direita em pós-ordem
        Visita a raiz