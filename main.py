import copy
import Interface as t
import turtle

tamanho_tabuleiro = 8   # definindo um tamanho inicial
movimentosLivres = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)) # movimentos que o cavalo pode fazer
def converteIndice(tabXadrez, tamanho_tabuleiro):   # converte o indice de letras para indice de numeros
    tabXadrez = tabXadrez.strip().lower()
    x = ord(tabXadrez[0]) - ord('a')
    y = tamanho_tabuleiro - int(tabXadrez[1:])
    return (x, y)

def moveCavalo(tabuleiro, P, tamanho_tabuleiro):
    Px, Py = P
    movimentosPossiveis = set((Px + x, Py + y) for x, y in movimentosLivres)    # insere em um dicionário
    movimentosPossiveis = set((x, y)
                              for x, y in movimentosPossiveis  # verifica em cada posicao dos movimentos
                              if 0 <= x < tamanho_tabuleiro     # se o movimento irá ultrapassar alguma barreira
                              and 0 <= y < tamanho_tabuleiro
                              and not tabuleiro[(x, y)])
    return movimentosPossiveis


def acessaPosicao(tabuleiro, P, tamanho_tabuleiro):
    acessados = []  # posições ja acessadas
    tab = copy.deepcopy(tabuleiro)  # copia os exatos indices e chaves do tabuleiro para um tab auxiliar
    for pos in moveCavalo(tabuleiro, P, tamanho_tabuleiro): # para cada posição possível acessada
        tab[pos] = -1
        acessados.append((len(moveCavalo(tab, pos, tamanho_tabuleiro)), pos))   # coloca nos acessados a proxima posicao sendo a quantidade de casas a ser percorrida
        tab[pos] = 0
    return acessados    # retorna as posicoes acessadas


def knights_tour(inicio, tamanho_tabuleiro, debug=False):
    tabuleiro = {(x, y): 0 for x in range(tamanho_tabuleiro) for y in range(tamanho_tabuleiro)}
    move = 1
    P = converteIndice(inicio, tamanho_tabuleiro)
    tabuleiro[P] = move
    move += 1

    while move <= len(tabuleiro):
        P = min(acessaPosicao(tabuleiro, P, tamanho_tabuleiro))[1]  # a posição é trocada quando descoberta uma nova posição que possui um caminho mais curto, seguindo a heuristica de Warnsdorff
        tabuleiro[P] = move # coloca para a proxima posição descoberta
        move += 1   # avança 1 no numero de posições visitadas

    return tabuleiro



if __name__ == '__main__':

    tabuleiro = knights_tour(turtle.textinput("Posição inicial","Exemplo(linhaXcoluna): a1, b5, h8"), 8)
    dicio = {}

    '''
    Gerando interface gráfica
    '''

    t.drawCreditos("Desenvolvido por:", -280, -320, 16)
    t.drawCreditos("Lucas J. Cunha", -105, -320, 16)
    t.drawCreditos("Luiz Zimmermann", -105, -350, 16)
    t.drawCreditos("Knight’s Tour Algorithm", -165, 300, 24)

    t.tabuleiro(-280, -280, 70, 8, "white", "#996633")
    for key,value in tabuleiro.items():
        dicio[value]=key

    for x in sorted(dicio.keys()):
        pos = dicio[x]
        if x == 64:
            t.quadrado ((-280 + 70 * pos[0]),(-280 + 70 * pos[1]),70,"red")
            t.drawPos(x,pos[0], pos[1])
        if x == 1:
            t.quadrado((-280 + 70 * pos[0]) , (-280 + 70 * pos[1]), 70, "green")
            t.drawPos(x,pos[0], pos[1])
        else:
            t.drawPos(x, pos[0], pos[1])

    for x in sorted(dicio.keys()):
        pos = dicio[x]
        t.drawPath(pos[0], pos[1])

    turtle.done()
