import math

def count(data, targets):
    o = 0
    for d in data:
        flag = True
        for t in targets:
            name, v = t
            if d[name] != v:
                flag = False
                break
        if not flag:
            continue
        o += 1
    return o

def get_domains(data):
    domains = {}

    for key in data[0].keys():
        dset = set()
        for d in data:
            dset.add(d[key])
        domains[key] = dset

    return domains

# P(T | G)
def calc_table(data, domains, given_name, target_name):
    table = {}
    for g in domains[given_name]:
        ps = [(p, count(data, [(given_name, g), (target_name, p)])) for p in domains[target_name]]
        s = sum([c for _, c in ps])
        props = {}
        for k, p in ps:
            props[k] = p / s
        table[g] = props
    return table


def exercise1():
    op = 0
    draw = 1
    me = 2
    data = [
        { "BH": op, "MH": "no", "FC": 3, "SC": 1 },
        { "BH": op, "MH": "1a", "FC": 2, "SC": 1 },
        { "BH": draw, "MH": "2v", "FC": 1, "SC": 1 },
        { "BH": me, "MH": "2a", "FC": 1, "SC": 1 },
        { "BH": draw, "MH": "fl", "FC": 1, "SC": 1 },
        { "BH": me, "MH": "st", "FC": 3, "SC": 2 },
        { "BH": me, "MH": "3v", "FC": 1, "SC": 1 },
        { "BH": me, "MH": "sfl", "FC": 1, "SC": 0 },
        { "BH": op, "MH": "no", "FC": 0, "SC": 0 },
        { "BH": op, "MH": "1a", "FC": 3, "SC": 2 },
        { "BH": draw, "MH": "2v", "FC": 2, "SC": 1 },
        { "BH": me, "MH": "2v", "FC": 3, "SC": 2 },
        { "BH": op, "MH": "2v", "FC": 1, "SC": 1 },
        { "BH": op, "MH": "2v", "FC": 3, "SC": 0 },
        { "BH": me, "MH": "2v", "FC": 3, "SC": 2 },
        { "BH": draw, "MH": "no", "FC": 3, "SC": 2 },
        { "BH": draw, "MH": "2v", "FC": 1, "SC": 1 },
        { "BH": op, "MH": "fl", "FC": 1, "SC": 1 },
        { "BH": op, "MH": "no", "FC": 3, "SC": 2 },
        { "BH": me, "MH": "1a", "FC": 3, "SC": 2 }
    ]
    domains = get_domains(data)


    op_p = calc_table(data, domains, "BH", "MH")[0]["1a"]
    draw_p = calc_table(data, domains, "BH", "MH")[1]["1a"]
    me_p = calc_table(data, domains, "BH", "MH")[2]["1a"]

    op_p *= calc_table(data, domains, "BH", "FC")[0][1]
    draw_p *= calc_table(data, domains, "BH", "FC")[1][1]
    me_p *= calc_table(data, domains, "BH", "FC")[2][1]

    op_p *= calc_table(data, domains, "BH", "SC")[0][1]
    draw_p *= calc_table(data, domains, "BH", "SC")[1][1]
    me_p *= calc_table(data, domains, "BH", "SC")[2][1]

    print(op_p, draw_p, me_p)


high = 0
medium = 1
low = 2
yes = 0
no = 1
married = 0
divorced = 1
unmarried = 2
data = [
    {"income": high, "houseowner": yes, "marital": married, "payback": yes },
    {"income": high, "houseowner": yes, "marital": unmarried, "payback": yes },
    {"income": medium, "houseowner": no, "marital": divorced, "payback": no },
    {"income": low, "houseowner": yes, "marital": married, "payback": no },
    {"income": low, "houseowner": no, "marital": unmarried, "payback": no },
]

def income_dif(a, b):
    return abs(a - b)

def married_dif(a, b):
    return 0 if a == b else 1

def houseowner_dif(a, b):
    return 0 if a == b else 1

def dist(a, b):
    return income_dif(a["income"], b["income"]) + married_dif(a["marital"], b["marital"]) + houseowner_dif(a["houseowner"], b["houseowner"])

def myKey(e):
    return e["dist"]

def nnk(data, point, k):
    distances = [{"point": a, "dist": dist(point, a)} for a in data]
    for d in distances:
        print(d["dist"])
    distances.sort(key=myKey)
    return distances[:k]

point = {"income": high, "houseowner": no, "marital": divorced}

closest = nnk(data, point, 3)

for e in closest:
    print(e)























