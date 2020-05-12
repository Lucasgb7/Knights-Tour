
N = 8
legalMoves_X = [2,1,-1,-2,-2,-1, 1, 2]
legalMoves_Y = [1,2, 2, 1,-1,-2,-2,-1]


def valid(x,y,path):
    if(x>=0 and y>=0 and x < N and y < N and path[(y*N + x) -1] == -1): #verifica se não passa dos limites e se já não foi visitado
        return True
    return False

def moves(pos,path):

    closer = []
    if pos%8 == 0:
        i=8
        j = pos // 8 -1
    else:
        i = (pos%8)
        j = (pos // 8)

    for offset in range(len(legalMoves_X)):
        newX = i+legalMoves_X[offset]
        newY = j+legalMoves_Y[offset]
        if(valid(newX,newY,path)):
            closer.append(newY*N+newX)

    return closer


def DFS(depth,path,posInic,limit):
    path[posInic-1] = depth

    if depth < limit:
        closerNodes = moves(posInic, path)#visinhos validos
        i = 0
        done = False
        while i < len(closerNodes) and not done:
            if path[closerNodes[i]-1] == -1:
                done = DFS(depth+1, path, closerNodes[i],limit)
            i = i+1
        if not done:
            path[posInic-1] = -1
    else:
        done = True
    return done


def click(x,y):

    vet = [-1 for i in range(N ** 2)]  ##Inicializa um vetor de 64 posições com -1
    pos=1
    if(not DFS(1,vet, pos, 64)):
        print("Não há solução!!")
    else:
        i = 0
        while (i < 64):
            print(i+1,vet[i])
            i = i+1


if __name__ == '__main__':

    click(0,0)
    input("Y?")