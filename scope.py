

# name = "Dave"
# count = 1


# def another():
#     color = "blue"
#     global count
#     count += 1
#     print(count)

#     def greeting(name):
#         nonlocal color
#         color = "red"
#         print(color)
#         print(name)

#     greeting("Dave")


# another()


def parent(person, coins):
    # coins =3 
    def play_game():
        nonlocal coins

        coins -=1
        if coins>1:
            print("\n" + person + " " + "has" +" " + str(coins) + " " + "coins left.")
        elif coins ==1:
            print("\n" + person + " " + "has" + " " + " " + str(coins) + " "+ "coin left.")
        else:
            print("\n" + person + "out of coin.")

    return play_game
akannie = parent("Akannie", 5)
omowunmi = parent("Omowunmi", 4)

akannie()
akannie()

omowunmi()
omowunmi()
omowunmi()

akannie()
