import reports


def main():
    output = open('output.txt', 'w')
    output.write(str(reports.count_games('game_stat.txt')))
    output.write('\n')
    output.write(str(reports.decide('game_stat.txt', 2000)))
    output.write('\n')
    output.write(reports.get_latest('game_stat.txt'))
    output.write('\n')
    output.write(str(reports.count_by_genre('game_stat.txt', 'RPG')))
    output.write('\n')
    output.write(str(reports.get_line_number_by_title('game_stat.txt', 'Crysis')))

    return

main()
