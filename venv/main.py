# Initial Commit
# imports
import art
import game_data
import random

# Logo printing
def logo():
    print(art.logo)

# 
def number_lottery_a():
    data_lenght = len(game_data.data)
    # compare_a_number = random.randint(0,data_lenght-1)
    compare_a_number = random.randint(0,3)
    print(compare_a_number)
    return compare_a_number
def number_lottery_b():
    data_lenght = len(game_data.data)
    # compare_b_number = random.randint(0, data_lenght-1)
    compare_b_number = random.randint(0,3)
    print(compare_b_number)
    return compare_b_number

def number_lottery_double_checking(compare_a_number,compare_b_number):
    if compare_b_number == compare_a_number:
        print("a==b")
        checking_main_loop()
def checking_main_loop():
    compare_a_number = number_lottery_a()
    compare_b_number = number_lottery_b()
    number_lottery_double_checking(compare_a_number,compare_b_number)
checking_main_loop()
# data_hold_a = []
# data_hold_b = []
# for i in game_data.data[0].values():
#     print(i)
#     data_hold_a.append(i)
# print(data_hold_a[1])
# print(game_data.data[0].values())