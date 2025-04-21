from random import *
import copy


# обработка ввода координат
def najatie(x, y):
    global matr, n, game_over, bomb_coord
    count = 0
    if [x, y] in bomb_coord:
        matr[x][y] = "💥"
        game_over = True
        babah()
    else:
        for i in range(n):
            for j in range(n):
                if abs(x - i) + abs(y - j) == 1 or (
                    abs(x - i) == 1 and abs(y - j) == 1
                ):
                    if [i, j] in bomb_coord:
                        count += 1
        matr[x][y] = f" {count} "


# бабах всех бомю при попадании в бомбу
def babah():
    global matr, n, game_over, bomb_coord
    for i in range(n):
        for j in range(n):
            if [i, j] in bomb_coord:
                matr[i][j] = "💥"


# печать полей


def otobrajenie():
    global n, matr, game_over
    for i in range(n):
        print(f" {coords[i]} ".ljust(2), end="")
    print()
    for i in range(n):
        for j in range(n):
            if matr[i][j] == " 0 ":
                print("⬜ ".ljust(2), end="")
            else:
                print(str(matr[i][j]).ljust(2), end="")
        print(f" {coords[i]} ".ljust(2), end="")
        print()
    print()


def otobrajenie_polnoe():
    global n, matr, game_over
    for i in range(n):
        print(f" {coords[i]} ".ljust(2), end="")
    print()
    for i in range(n):
        for j in range(n):
            if matr[i][j] == " 0 ":
                print(str(matr[i][j]).ljust(2), end="")
                # print("⬜ ".ljust(2), end="")
            else:
                print(str(matr[i][j]).ljust(2), end="")
        print(f" {coords[i]} ".ljust(2), end="")
        print()
    print()
    for i in range(n):
        for j in range(n):
            print(str(pole_otobr[i][j]).ljust(2), end="")
        print()


def game_proc():
    global x, y, game_over
    najatie(x, y)
    otkr()
    otrk_sosedok()
    otobrajenie()


# счет количества 0 которые надо открыть
def schet():
    global matr, pole_otobr, n
    count = 0
    for i in range(n):
        for j in range(n):
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if (
                        0 <= x <= 7
                        and 0 <= y <= 7
                        and matr[x][y] == "🟩"
                        and pole_otobr[x][y] == " 0 "
                        and matr[i][j] == " 0 "
                    ):
                        count += 1
    return count == 0


def otrk_sosedok():
    global matr, pole_otobr, n
    spis = []
    for i in range(n):
        for j in range(n):
            if matr[i][j] == " 0 ":
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x <= 7 and 0 <= y <= 7 and matr[x][y] == "🟩":
                            spis.append([x, y])
    print("otrk_sosedok", spis)
    for i in spis:
        matr[i[0]][i[1]] = pole_otobr[i[0]][i[1]]


def otkr():
    global matr, pole_otobr, n
    while True:
        spis = []
        for i in range(n):
            for j in range(n):
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if (
                            0 <= x <= 7
                            and 0 <= y <= 7
                            and matr[x][y] == "🟩"
                            and pole_otobr[x][y] == " 0 "
                            and matr[i][j] == " 0 "
                        ):
                            spis.append([x, y])
        #        print(spis)
        for i in spis:
            matr[i[0]][i[1]] = " 0 "
        if schet():
            break


n = 8
# чистое поле
matr = [["🟩" for _ in range(n)] for _ in range(n)]
# создание бомб
colvo_lov = 8
bomb_coord = []
for i in range(colvo_lov):
    bomb_coord.append([randrange(0, n), randrange(0, n)])

coords = [int(i) for i in range(n)]
# создание поля отображения
counti = 0
pole_otobr = copy.deepcopy(matr)

for i in range(n):
    for j in range(n):
        if [i, j] in bomb_coord:
            pole_otobr[i][j] = "💣 "
        else:
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x <= 7 and 0 <= y <= 7 and [x, y] in bomb_coord:
                        counti += 1
            pole_otobr[i][j] = f" {counti} "
            counti = 0
# первый вывод
otobrajenie()
# индикатор конца игры
game_over = False
# сама игра
while True:
    if game_over == True:
        break
    vvod = input(
        "введите координаты в формате 2-х чисел от 1 до 8 без пробелов \n",
    )
    if vvod.isalnum() and len(vvod) == 2:
        x, y = [int(i) for i in list(vvod)]
        game_proc()

    else:
        break
