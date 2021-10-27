# Programmer: Sebastian Silguero
# Course: CS151, Dr. Rajeev
# Date: October 25th, 2021
# Programming Assignment: 3
# Program Inputs: Calculate which sport statistic
# Program Outputs: Result of the sport statistic chosen

# Function to calculate quarterback rating
def qb_rating(completions, passing_yards, td_passes, interceptions, attempts):
    passer = 100 * (5 * (completions / attempts - 0.3) + 0.25 * (passing_yards / attempts - 3) + 20 * (td_passes / attempts) + 2.375 - (25 * interceptions / attempts)) / 6
    return passer


# Function to calculate the total score of quidditch team
def quidditch(goals, catches):
    final_score = (goals * 10) + (catches * 30)
    return final_score


# Function to calculate a gymnasts final score
def gymnastics(dif_score):
    total = 0
    attempt = 1
    while attempt < 6:
        score = int(input("Enter the score from 0 to 10: "))
        total += score
        attempt += 1
    final_score2 = (total / 5) + dif_score
    return final_score2


# Main function
def main():
    print("Football, Quidditch, Gymnastics")
    calc_choice = input("Which statistic would you like to choose from: ")
    calc_choice = calc_choice.strip().lower()

    # If statements to choose between the three different sports
    if calc_choice == "football":
        completions = int(input("How many completions has the QB made: "))
        passing_yards = float(input("How many passing yards has the QB thrown: "))
        td_passes = int(input("How many touchdowns has the QB thrown: "))
        interceptions = int(input("How many interceptions has the QB thrown: "))
        attempts = int(input("How many throw attempts has the QB had: "))
        qbRating = round(qb_rating(completions, passing_yards, td_passes, interceptions, attempts), 2)
        print("The Quarterback rating is equal to ",
              round(qb_rating(completions, passing_yards, td_passes, interceptions, attempts), 2))
        if qbRating >= 158.3:
            print("The quarterback has a perfect passer rating")
    elif calc_choice == "quidditch":
        goals = int(input("How many goals were scored: "))
        catches = int(input("How many goals were caught: "))
        snitch = input("Has your team caught the snitch? ")
        snitch = snitch.strip().lower()
        if snitch == "yes":
            update_score = quidditch(goals, catches) + 30
            print("The final score of the team is ", update_score)
        elif snitch == "no":
            print("The final score of the team is ", quidditch(goals, catches))
    elif calc_choice == "gymnastics":
        dif_score = int(input("What is the difficulty of the current apparatus from 0 to 10: "))
        print("The total score of the apparatus is", round(gymnastics(dif_score), 2))
    else:
        print("Invalid choice")


main()