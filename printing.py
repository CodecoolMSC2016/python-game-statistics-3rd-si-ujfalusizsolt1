import reports


def main():
    running = True
    while running:
        print("1. How many games are in the file? \n2. Is there a game from a given year? \n3. Which was the latest gam"
              "e? \n4. How many games do we have by genre? \n5. What is the line number of the given game (by title)?")
        question_number = input("Please choose the number of your question: ")

        if question_number == '1':
            print("There are {0} games in the file.".format(reports.count_games('game_stat.txt')))
        elif question_number == '2':
            year = int(input("From which year? "))
            if reports.decide('game_stat.txt', year):
                print("Yes.")
            else:
                print("No.")
        elif question_number == '3':
            print("The latest game is {0}.".format(reports.get_latest('game_stat.txt')))
        elif question_number == '4':
            genre = input("Which genre? ")
            print("We have {0} games by this genre. ".format(reports.count_by_genre('game_stat.txt', genre)))
        elif question_number == '5':
            title = input("Which game? ")
            if reports.get_line_number_by_title('game_stat.txt', title) == ValueError:
                print("We don't have this game.")
            else:
                print("This game's line number is {0}.".format(
                    reports.get_line_number_by_title('game_stat.txt', title)))
        else:
            running = False

    return

main()
