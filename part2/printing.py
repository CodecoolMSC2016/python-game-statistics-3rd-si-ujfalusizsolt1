import reports


def main():
    running = True
    while running:
        print("1. What is the title of the most played game?\n2. How many copies have been sold total?\n3. What is the"
              "average selling?\n4. How many characters long is the longest title?\n5. What is the average of the relea"
              "se dates?\n6. What properties has a game?")
        question_number = input("Please choose the number of your question: ")

        if question_number == '1':
            print("The most played game is {0}.".format(reports.get_most_played('game_stat.txt')))
        elif question_number == '2':
            print("{0} million copies were sold in total.".format(reports.sum_sold('game_stat.txt')))
        elif question_number == '3':
            print("The average selling is {0}.".format(reports.get_selling_avg('game_stat.txt')))
        elif question_number == '4':
            print("The longest title is {0} characters long.".format(reports.count_longest_title('game_stat.txt')))
        elif question_number == '5':
            print("The average of the release dates is {0}.".format(reports.get_date_avg('game_stat.txt')))
        elif question_number == '6':
            game = input("Which game's properties are you interested in?\n")
            print("Total copies sold(million): {0}\nRelease date: {1}\nGenre: {2}\nPublisher: {3}".format(
                reports.get_game('game_stat.txt', game)[1], reports.get_game('game_stat.txt', game)[2],
                reports.get_game('game_stat.txt', game)[3], reports.get_game('game_stat.txt', game)[4]
            ))
        else:
            running = False

    return

main()
