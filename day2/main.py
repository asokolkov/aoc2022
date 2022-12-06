from utils.files import read_file


def solve1():
    value = {'X': 1, 'Y': 2, 'Z': 3}
    points = {
        'A': {'X': 3, 'Y': 6, 'Z': 0},
        'B': {'X': 0, 'Y': 3, 'Z': 6},
        'C': {'X': 6, 'Y': 0, 'Z': 3}
    }

    pairs = [row.split() for row in read_file('day2')]
    print(sum(map(lambda x: points[x[0]][x[1]] + value[x[1]], pairs)))
    

def score_round(info):
    value = {'A': 1, 'B': 2, 'C': 3}
    win_conditions = {'A': 'B', 'B': 'C', 'C': 'A'}
    lose_conditions = {'A': 'C', 'B': 'A', 'C': 'B'}

    opponent_move = info[0]
    move = info[1]
    score = 3 + value[opponent_move]

    if move == 'X':
        score = value[lose_conditions[opponent_move]]
    elif move == 'Z':
        score = 6 + value[win_conditions[opponent_move]]

    return score


def solve2():
    print(sum(map(lambda x: score_round(x.split()), read_file('day2'))))


def main():
    solve1()
    solve2()


if __name__ == '__main__':
    main()
