from math import floor


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines]
    mass = [int(x) for x in lines]

    total = sum([handle_mass(x) for x in mass])
    print(total)


def handle_mass(x):
    fuel =  floor(x / 3) - 2
    if fuel < 0:
        return 0
    else:
        return fuel + handle_mass(fuel)


if __name__ == '__main__':
    main()
