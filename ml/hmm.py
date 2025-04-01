def find_prob(V, A, B):
    alpha = [[0 for _ in range(len(V))] for _ in range(len(A))]
    for w in range(len(A)):
        if w == 0:
            alpha[w][0] = 1
        else:
            alpha[w][0] = 0

    for t in range(1, len(V)):
        for w in range(len(A)):
            summation = 0
            for i in range(len(A)):
                summation += alpha[i][t-1] * A[i][w]
            alpha[w][t] = B[w][V[t]] * summation
    
    final_prob = sum(alpha[w][len(V)-1] for w in range(len(A)))
    
    return final_prob

V = [1, 2, 3, 4, 0]
A = [[1, 0, 0, 0], [0.2, 0.3, 0.1, 0.4], [0.2, 0.5, 0.2, 0.1], [0.7, 0.1, 0.1, 0.1]]
B = [[1, 0, 0, 0, 0], [0, 0.3, 0.4, 0.1, 0.2], [0, 0.1, 0.1, 0.7, 0.1], [0, 0.5, 0.2, 0.1, 0.2]]

print(find_prob(V, A, B))
