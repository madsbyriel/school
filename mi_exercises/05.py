import math
import numpy as np

# Exercise 1
def calculate_mse(y_deltas):
    arr = []
    for col in y_deltas:
        sum = 0
        for el in col:
            sum += el * el
        arr.append(sum / len(col))
    return arr


def exercise1():
    points = np.array([
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 0],
        [1, 2, 1],
    ], dtype=np.double)

    target = np.array([
        [2], [0], [3], [2]
    ], dtype=np.double)

    weights = np.array([
        [0, 1],     #w0
        [1, 1],     #w1
        [-1, 0]     #w2
    ])

    # Predictions (column_i is the predictions with weights_i)
    yhats = points @ weights
    y_delta = target - yhats

    mses = calculate_mse(y_delta.T)
    print(mses)


# Exercise 2
def count_occurences(data, domain_name, v):
    return count_occurences_given(data, [(domain_name, v)])

def count_occurences_given(data, givens):
    occurences = 0
    for point in data:
        flag = True
        for given_name, given_value in givens:
            if point[given_name] != given_value:
                flag = False
                break
        if flag:
            occurences += 1

    return occurences
    

def calculate_p(data, domain, domain_name):
    occurences = [count_occurences(data, domain_name, el) for el in domain]
    return [c / len(data) for c in occurences]

def calculate_entropy_elem(ps):
    acc = []
    for p in ps:
        v = 0
        try:
            v = p * math.log2(p)
        except:
            v = 0
        acc.append(v)

    return -sum(acc)

def calculate_entropy_total(data, domains):
    ps = [(name, calculate_p(data, domains[name], name)) for name in domains.keys()]
    ps = [(name, calculate_entropy_elem(p)) for name, p in ps]

    entropies = {}
    for name, entropy in ps:
        entropies[name] = entropy

    return entropies

def calculate_expected_entropy_elem(data, domain, domain_name, givens):
    occurences = count_occurences_given(data, [("age", age_lt5)])
    print(occurences)



domains = {
    "age": {True, False},
    "make": {True, False},
    "owners": {1, 2, 3},
    "kilometers": {True, False},
    "doors": {3, 5},
    "acceptable": {True, False},
}

age_lt5 = True
age_gte5 = False
mazda = True
toyota = False
kilogt150k = True
kilolte150k = False

data = [
    {
        "age": age_lt5,
        "make": mazda,
        "owners": 1,
        "kilometers": kilogt150k,
        "doors": 3,
        "acceptable": True,
    },
    {
        "age": age_gte5,
        "make": mazda,
        "owners": 3,
        "kilometers": kilogt150k,
        "doors": 3,
        "acceptable": False,
    },
    {
        "age": age_gte5,
        "make": toyota,
        "owners": 1,
        "kilometers": kilolte150k,
        "doors": 3,
        "acceptable": False,
    },
    {
        "age": age_gte5,
        "make": mazda,
        "owners": 3,
        "kilometers": kilogt150k,
        "doors": 5,
        "acceptable": True,
    },
    {
        "age": age_gte5,
        "make": toyota,
        "owners": 2,
        "kilometers": kilogt150k,
        "doors": 5,
        "acceptable": True,
    },
]

print(count_occurences_given(data, [("owners", 2)]))
