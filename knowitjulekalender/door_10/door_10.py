def formula(params, yrs):

    # yr 0:
    r = 125000
    u = 3500

    for yr in range(yrs):

        new_r = int(r + ((params['alfa'] * r * (params['r_max'] - r))/params['r_max']) - params['gamma'] * u * r)
        new_u = int(u + (params['gamma'] * u * r) / params['lambda'] - params['beta'] * u)
        r, u = new_r, new_u

    return r, u


def main():

    params = {
        'r_max': 10**6,
        'alfa': 0.2,
        'gamma': 0.000075,
        'lambda': 83,
        'beta': 0.1
    }

    print(formula(params, 10))


if __name__ == '__main__':
    main()
