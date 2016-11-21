import reports


def main():
    output = open('output.txt', 'w')
    output.write(reports.get_most_played('game_stat.txt'))
    output.write('\n')
    output.write(str(reports.sum_sold('game_stat.txt')))
    output.write('\n')
    output.write(str(reports.get_selling_avg('game_stat.txt')))
    output.write('\n')
    output.write(str(reports.count_longest_title('game_stat.txt')))
    output.write('\n')
    output.write(str(reports.get_date_avg('game_stat.txt')))
    output.write('\n')
    for data in reports.get_game('game_stat.txt', 'Terraria'):
        output.write(str(data))
        output.write('\t')

    return

main()
