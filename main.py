import copy

tamanhoTabuleiro = 6
_movimentosLivres = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))
def chess2index(tab, tamTab=tamanhoTabuleiro):
    'Converte a notação algébrica do xadrez para formato de índice interno'
    tab = tab.strip().lower()
    x = ord(tab[0]) - ord('a')
    y = tamTab - int(tab[1:])
    return (x, y)


def boardstring(tab, tamTab=tamanhoTabuleiro):	# Transforma o tabuleiro para String, para printar
    r = range(tamTab)
    linhas = ''
    for y in r:
        linhas += '\n' + ','.join('%2i' % tab[(x, y)] if tab[(x, y)] else '  '
                                 for x in r)
    return linhas


def movimentaCavalo(tab, P, tamTab=tamanhoTabuleiro):	# Define onde o cavalo pode se movimentar
    Px, Py = P
    movimentosPossiveis = set((Px + x, Py + y) for x, y in _movimentosLivres)
    movimentosPossiveis = set((x, y)
                 for x, y in movimentosPossiveis
                 if 0 <= x < tamTab
                 and 0 <= y < tamTab
                 and not tab[(x, y)])
    return movimentosPossiveis


def accessibility(tab, P, tamTab=tamanhoTabuleiro):
    access = []
    brd = copy.deepcopy(tab)
    for pos in movimentaCavalo(tab, P, tamTab=tamTab):
        brd[pos] = -1
        access.append((len(movimentaCavalo(brd, pos, tamTab=tamTab)), pos))
        brd[pos] = 0
    return access


def passeiaCavalo(start, tamTab=tamanhoTabuleiro, _debug=False):
    tab = {(x, y): 0 for x in range(tamTab) for y in range(tamTab)}
    move = 1
    P = chess2index(start, tamTab)
    tab[P] = move
    move += 1
    if _debug:
        print(boardstring(tab, tamTab=tamTab))
    while move <= len(tab):
        P = min(accessibility(tab, P, tamTab))[1]
        tab[P] = move
        move += 1
        if _debug:
            print(boardstring(tab, tamTab=tamTab))
            input('\n%2i next: ' % move)
    return tab


if __name__ == '__main__':
    while 1:
        tamanhoTabuleiro = int(input('\nTamanho do tabuleiro (N²): '))
        if tamanhoTabuleiro < 5:
            continue
        inicio = input('Posição inicial (ex.: c3): ')
        tabuleiro = passeiaCavalo(inicio, tamanhoTabuleiro)
        print(boardstring(tabuleiro, tamTab=tamanhoTabuleiro))