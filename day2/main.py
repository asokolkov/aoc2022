def main():
    value = {'X': 1, 'Y': 2, 'Z': 3}
    points = {
        'A': {'X': 3, 'Y': 6, 'Z': 0},
        'B': {'X': 0, 'Y': 3, 'Z': 6},
        'C': {'X': 6, 'Y': 0, 'Z': 3}
    }
    
    with open('input.txt', 'r') as f:
        pairs = [a.split() for a in f.readlines()]
        print(sum(map(lambda x: points[x[0]][x[1]] + value[x[1]], pairs)))


if __name__ == '__main__':
    main()
