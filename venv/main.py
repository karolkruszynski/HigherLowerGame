# Initial Commit

# imports
import art
import game_data
import random

checked_a_num = 0
checked_b_num = 0

# Logo printing
def logo():
    print(art.logo)

# Draw a number for A data
def number_lottery_a():
    global checked_a_num
    data_lenght = len(game_data.data)
    # compare_a_number = random.randint(0,data_lenght-1)
    compare_a_number = random.randint(0,3)
    print(compare_a_number)
    checked_a_num = compare_a_number
    return compare_a_number

# Draw a number for B data
def number_lottery_b():
    global checked_b_num
    data_lenght = len(game_data.data)
    # compare_b_number = random.randint(0, data_lenght-1)
    compare_b_number = random.randint(0,3)
    print(compare_b_number)
    checked_b_num = compare_b_number
    return compare_b_number

def number_lottery_double_checking(compare_a_number,compare_b_number):
    if compare_a_number == compare_b_number:
        print("a==b")
        checking_main_loop()
    else:
        player_game_loop()
    # else:
    #     data_a_export(compare_a_number)
    #     data_b_export(compare_b_number)

def data_a_export(compare_a_number):
    data_hold_a = []
    '''index data_hold maeaning 0-name 1-followrs number 2-job 3-country'''
    for i in game_data.data[compare_a_number].values():
        # print(i)
        data_hold_a.append(i)
    print(data_hold_a[1])
    return data_hold_a

def data_b_export(compare_b_number):
    data_hold_b = []
    '''index data_hold maeaning 0-name 1-followrs number 2-job 3-country'''
    for i in game_data.data[compare_b_number].values():
        # print(i)
        data_hold_b.append(i)
    print(data_hold_b[1])
    return data_hold_b
        # print(game_data.data[0].values())

def player_choose(data_hold_a,data_hold_b):
    player_answer = str(input(" Who has more followers? Type 'A' or 'B':" )).lower()
    if player_answer == "a":
        player_answer = 1
    elif player_answer == "b":
        player_answer = 2
    else:
        print("Please select A or B.")

    data_hold_a_follows = data_hold_a[1]
    data_hold_b_follows = data_hold_b[1]

    print(f"followersi dla A {data_hold_a[1]}")
    print(f"followersi dla B {data_hold_b[1]}")


    if data_hold_a_follows > data_hold_b_follows and player_answer == 1:
        print("You have right")
        continue_game_if_win(data_hold_a_follows,data_hold_b_follows,data_hold_a,data_hold_b)
        return data_hold_a_follows
        return data_hold_b_follows
    elif data_hold_a_follows < data_hold_b_follows and player_answer == 2:
        print("You have right")
        continue_game_if_win(data_hold_a_follows,data_hold_b_follows,data_hold_a,data_hold_b)
        return data_hold_a_follows
        return data_hold_b_follows
    else:
        print("You Guess wrong!")

def continue_game_if_win(data_hold_a_follows,data_hold_b_follows,data_hold_a,data_hold_b):
    global checked_a_num
    # print(data_hold_a_follows)
    # print(data_hold_b_follows)
    # print(data_hold_a)
    # print(data_hold_b)
    if data_hold_a_follows < data_hold_b_follows:
        data_hold_a_follows = data_hold_b_follows
        data_hold_a = data_hold_b
    # print(data_hold_a_follows)
    print(f"stała a {checked_a_num}")
    compare_a_number = checked_a_num
    print(f"compare a to num {compare_a_number}")
    compare_b_number = number_lottery_b()
    print(f"compare b new number {compare_b_number}")
    data_hold_b = data_b_export(checked_b_num)
    print(data_hold_b)
    print(data_hold_b[1])
    while data_hold_a[1] == data_hold_b[1]:
        print(f"compare b new number przed while {compare_b_number}")
        compare_b_number = number_lottery_b()
        print(f"while {compare_b_number}")
        data_hold_b = data_b_export(checked_b_num)
    player_choose(data_hold_a, data_hold_b)

def checking_main_loop():
    compare_a_number = number_lottery_a()
    compare_b_number = number_lottery_b()
    number_lottery_double_checking(compare_a_number,compare_b_number)
    return checked_b_num

def player_game_loop():
    data_hold_a = data_a_export(checked_a_num)
    data_hold_b = data_b_export(checked_b_num)
    player_choose(data_hold_a,data_hold_b)

checking_main_loop()