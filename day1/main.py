from utils.files import read_file


def get_elves_calories():
    elf_calories = []
    current_elf = 0

    for i in read_file('day1'):
        number = i.strip()
        if number:
            if current_elf > len(elf_calories) - 1:
                elf_calories.append(0)
            elf_calories[current_elf] += int(number)
        else:
            current_elf += 1

    return sorted(elf_calories, reverse=True)


def main():
    top_elves_amount = 3
    elf_calories = get_elves_calories()
    print(sum(elf_calories[:top_elves_amount]))


if __name__ == '__main__':
    main()
