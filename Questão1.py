# -*- coding: UTF-8 -*-
def max_subvector(V, DP):
    j = 1
    for i in V:
        if i % 2 == 0:   # É par
            DP[j] = max(1 + DP[j - 1], DP[j - 1])
        else:
            DP[j] = DP[j - 1]
        j += 1
    return DP[-1]


if __name__ == '__main__':
    # Queremos achar o maior número de subvetores (trechos consecutivos) formados por um número par
    # em que o vetor pode ser decomposto.
    vetor = [1, 3, 9, 0, 7, 6, 5, 3, 9, 2]
    M = [0] * (len(vetor) + 1)
    print(max_subvector(vetor, M))
