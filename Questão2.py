# -*- coding: UTF-8 -*-
def maxAlternante(DP, v):
    for i in range(len(v)):
        for j in range(i):
            if v[i] > v[j]:
                DP[i][0] = max(1 + DP[j][1], DP[i][0])
            else:
                DP[i][1] = max(1 + DP[j][0], DP[i][1])

    return max(DP[-1][0], DP[-1][1])


if __name__ == '__main__':
    # Uma sequência é dita alternante se for all i, os sinais de ai - ai + 1 e a i+1 - ai+2 são distintos.
    # Achar o tamanho da maior sequência alternante em um vetor.
    # Todos os elementos do vetor são distintos.
    # Abordagem baseada em PD

    vetor = [7, 5, 8, 6, 2, 1, 0, 3, 4, 9]
    M = [[0] * 2 for _ in range(len(vetor))]
    M[0][0] = M[0][1] = 1
    print(maxAlternante(M, vetor))
