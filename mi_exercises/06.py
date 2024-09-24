import math
import numpy as np

def sigmoid_e(v):
    return 1 / (1 + math.pow(math.e, -v))

def sign(v):
    result = []
    for r in v:
        row = []
        for e in r:
            v = -1
            if e > 0:
                v = 1
            row.append(v)
        result.append(row)
    return np.array(result, dtype=np.double)

def sigmoid(v):
    result = []
    for r in v:
        row = []
        for e in r:
            v = sigmoid_e(e)
            row.append(v)
        result.append(row)
    return np.array(result, dtype=np.double)


# Exercise 2

def ex2():
    ex2data = [
        [1, 1, 5],
        [1, 0, 14]
    ]
    ex2weightslayer1 = [
        [0, 1.3, -0.3],
        [0, 1.7, 1.0],
    ]

    d = np.array(ex2data, dtype=np.double)
    w = np.array(ex2weightslayer1, dtype=np.double)

    r = d @ w.T
    r = sigmoid(r)
    w = np.array([
        [0.6],
        [-1.4]
    ])
    print(r @ w)

# Exercise 3

def compute_new_w(current_weights, data, error, learning_rate):
    new_weights = current_weights.T.copy()
    for d, e in zip(data, error):
        new_weights += d * e * learning_rate
    return new_weights.T

data = np.array([
    [1, 1, 1],
    [1, -1, 1],
    [1, 1, -1],
    [1, -1, -1],
], dtype=np.double)

weights = np.array([
    [0],
    [0],
    [0],
], dtype=np.double)

target = [
    [1],
    [-1],
    [1],
    [-1]
]

o = sign(data @ weights)
dif = target - o
print(dif)














