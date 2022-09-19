#Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# человек против бота:
from random import randint

def input_dat(name):
    x = int(input(f"{name}, how much sweets do you want to take?:  "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, please enter the quantity between 1 and 28:  "))
    return x


def p_print(name, k, counter, value):
    print(f"{name} made a decision, he took {k} sweets, now he had {counter}. {value} sweets left.")

player1 = input("Please enter your name: ")
player2 = "Bot"
value = int(input("How much sweets are on table: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"{player1} - your turn")
else:
    print(f"{player2} - your turn")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = randint(1,29)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"{player1} - Won!")
else:
    print(f"{player2} - Won!")