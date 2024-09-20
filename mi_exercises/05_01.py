data_points = [(1, 1), (0, 0), (1, 0), (2, 1)]
weights = [(0, 1, -1), (1, 1, 0)]
ys = [2, 0, 3, 2]

def calculate_yhat(weights, xs):
    x1, x2 = xs
    w0, w1, w2 = weights
    v = w0 + w1 * x1 + w2 * x2
    return v

def calculate_yhat_format(weights, xs):
    x1, x2 = xs
    w0, w1, w2 = weights
    v = w0 + w1 * x1 + w2 * x2
    print(f"{w0} + {w1} * {x1} + {w2} * {x2} &= {v} \\\\")

def calculate_sqerror(y, yhat):
    v = (y - yhat) * (y - yhat)
    return v

def calculate_sqerror_format(y, yhat):
    v = (y - yhat) * (y - yhat)
    print(f"({y} - {yhat}) * ({y} - {yhat}) &= {v} \\\\")

y_hats_total = []

for w in weights:
    y_hats = []
    for d in data_points:
        y_hats.append(calculate_yhat(w, d))
    y_hats_total.append(y_hats)

mses = []

for y_hats in y_hats_total:
    mse = 0
    for y, y_hat in zip(ys, y_hats):
        mse += calculate_sqerror(y, y_hat)
    mse = mse / len(ys)
    mses.append(mse)












