import math


def get_most_played(file_name):
    game_list = get_game_list(file_name)
    max = 0
    result = ''
    for sor in game_list:
        if float(sor[1]) > max:
            max = float(sor[1])
            result = sor[0]

    return(result)


def sum_sold(file_name):
    game_list = get_game_list(file_name)
    result = 0
    for sor in game_list:
        result += float(sor[1])

    return(result)


def get_selling_avg(file_name):
    game_list = get_game_list(file_name)
    result = sum_sold(file_name) / len(game_list)

    return(result)


def count_longest_title(file_name):
    game_list = get_game_list(file_name)
    result = 0
    for sor in game_list:
        if len(sor[0]) > result:
            result = len(sor[0])

    return(result)


def get_date_avg(file_name):
    game_list = get_game_list(file_name)
    result = 0
    for sor in game_list:
        result += int(sor[2])
    result = math.ceil(result / len(game_list))

    return(result)


def get_game(file_name, title):
    game_list = get_game_list(file_name)
    result = []
    game_index = -1
    for sor in game_list:
        if sor[0] == title:
            result = sor
    result[1] = float(result[1])
    result[2] = int(result[2])

    return(result)


def get_game_list(file_name):
    game_list = []
    source_file = open(file_name, "r")
    for line in source_file:
        game_list.append(line.strip().split('\t'))

    return(game_list)


def main():
    get_most_played('game_stat.txt')
    sum_sold('game_stat.txt')
    get_selling_avg('game_stat.txt')
    count_longest_title('game_stat.txt')
    get_date_avg('game_stat.txt')
    get_game('game_stat.txt', 'Terraria')

    return

main()
