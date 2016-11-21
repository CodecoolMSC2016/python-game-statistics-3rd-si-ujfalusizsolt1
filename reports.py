def count_games(file_name):
    game_list = get_game_list(file_name)
    result = len(game_list)

    return(result)


def decide(file_name, year):
    game_list = get_game_list(file_name)
    result = False
    for line in game_list:
        if int(line[2]) == year:
            result = True

    return(result)


def get_latest(file_name):
    game_list = get_game_list(file_name)
    latest = 0
    result = ''
    for line in game_list:
        if int(line[2]) > latest:
            latest = int(line[2])
            result = line[0]

    return(result)


def count_by_genre(file_name, genre):
    game_list = get_game_list(file_name)
    result = 0
    for line in game_list:
        if line[3] == genre:
            result += 1

    return(result)


def get_line_number_by_title(file_name, title):
    game_list = get_game_list(file_name)
    result = -1
    current_line = 0
    for line in game_list:
        current_line += 1
        if line[0] == title:
            result = current_line
    if result == -1:
        result = ValueError

    return(result)


def get_game_list(file_name):
    game_list = []
    source_file = open(file_name, "r")
    for line in source_file:
        game_list.append(line.strip().split('\t'))

    return(game_list)


def main():
    count_games('game_stat.txt')
    decide('game_stat.txt', 2004)
    get_latest('game_stat.txt')
    count_by_genre('game_stat.txt', 'RPG')
    get_line_number_by_title('game_stat.txt', 'Crysis')

    return

main()
