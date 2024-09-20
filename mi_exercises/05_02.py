import math

# age, make, owner, kilometers, doors, acceptable
r1 = {
    "age": True, 
    "make": 0, 
    "owner": 1, 
    "kilometers": True, 
    "doors": 3, 
    "acceptable": True
}
r2 = {
    "age": False, 
    "make": 0, 
    "owner": 3, 
    "kilometers": True, 
    "doors": 3, 
    "acceptable": False
}
r3 = {
    "age": False, 
    "make": 1, 
    "owner": 1, 
    "kilometers": False, 
    "doors": 3, 
    "acceptable": False
}
r4 = {
    "age": False, 
    "make": 0, 
    "owner": 3, 
    "kilometers": True, 
    "doors": 5, 
    "acceptable": True
}
r5 = {
    "age": False, 
    "make": 1, 
    "owner": 2, 
    "kilometers": False, 
    "doors": 5, 
    "acceptable": True
}

table = [r1, r2, r3, r4, r5]

domains = {
    "age": {True, False},
    "make": {1, 2},
    "owner": {1, 2, 3},
    "kilometers": {True, False},
    "doors": {3, 5},
    "acceptable": {True, False}
}

def count_occurences_given(table, column, value, evidence):
    count = 0
    for r in table:
        evidence_holds = True

        for e in evidence:
            col, val = e
            if r[col] != val:
                evidence_holds = False
                break

        if not evidence_holds:
            continue

        if r[column] == value:
            count += 1
    return count

def calculate_propability_distribution(table, domains, column):
    p = []
    total = len(table)

    for possibility in domains[column]:
        count = count_occurences_given(table, column, possibility, [])
        p.append(count / total)

    return p


def calc_entropy(table, domains, column):
    p = calculate_propability_distribution(table, domains, column)
    sum = 0
    for prop in p:
        v = 0
        try:
            v = prop * math.log2(prop)
        except:
            v = 0
        sum += v
    return -sum

def calc_total_entropy(table, domains):
    result = {}
    for k in domains.keys():
        result[k] = calc_entropy(table, domains, k)
    return result

def calculate_entropy(p, show=False):
    sum = 0
    flag = True
    s = f"Entropy({p}) = "
    for prop in p:
        if flag:
            s += f"-{prop} * log_2({prop})"
            flag = False
        else:
            s += f" - {prop} * log_2({prop})"
        v = 0
        try:
            v = prop * math.log2(prop)
        except:
            v = 0
        sum += v
    s += f" = {-sum}"
    if show:
        print(s)
    return -sum
