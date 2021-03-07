# -*- coding: UTF-8 -*-
from copy import deepcopy


def maxSubarray(v):
    if len(v) == 2 or len(v) == 1:
        return v

    mid = len(v) // 2
    left = deepcopy(v[0: mid])
    right = deepcopy(v[mid + 1:])

    esq = maxSubarray(left)
    dir = maxSubarray(right)
    return maxAlternative(esq, dir)


def maxAlternative(e, d):
    if e[-1] < e[-2]:
        flag = True
    elif e[-1] > e[-2]:
        flag = False

    if e[-1] < d[0] and flag:
        result = e + d
    elif e[-1] > d[0] and not flag:
        result = e + d
    else:
        return e if len(e) > len(d) else d
    return result


if __name__ == '__main__':
    # Uma sequência é dita alternante se for all i, os sinais de ai - ai+1 e ai+1 - ai+2 são distintos.
    # Achar o tamanho do maior subarray alternante em um vetor.
    # Dessa forma, a ordem de escolha dos elementos IMPORTA
    # Todos os elementos do vetor são distintos.
    # Abordagem baseada em DC
    vetor = [4, 3, 2, 5, 8, 7, 1, 10, 11]
    if len(vetor) == 1:
        print(vetor[0])
    else:
        print(maxSubarray(vetor))
