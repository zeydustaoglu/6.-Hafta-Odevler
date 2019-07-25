# ODEV 2: XOX Oyunu
# # 		Kitapta yer alan XOX oyunu iki kisinin karsilikli oynayabilecegi sekilde duzenlenmis. Sizden bu oyunu
# # 		kullanicinin bilgisayara karsi oynayabilecegi versiyonunu yapmanizi istiyoruz. Ayrica gelistireceginiz
# # 		algoritma sayesinde bilgisayarin tamamen rastgele hamleler yapmasindan ziyade mantikli hamleler yapmasini
# # 		saglamanizi istiyoruz. Ornegin bilgisayarin "O" hamlesini yaptigini varsayalim:
# # 					X O _
# # 					_ X _
# # 					_ _ _
# #
# # 		seklinde olusan bir durumda hamle sirasi bilgisayarda ve bilgisayar kaybetmemek icin sag-alt koseye "O"
# # 		koymalidir.
# #
# #
# # 		Farkli bir ihtimal:
# # 					O X X
# # 					O _ X
# # 					_ _ _
# #
# # 		boyle bir durumda da hamle sirasi bilgisayarda ve bilgisayar kazanma hamlesi olarak sol-alt koseye "O" koyarak
# # 		oyunu bitirmelidir.

import random

tahta = [["___", "___", "___"],
["___", "___", "___"],
["___", "___", "___"]]
print("\n"*15)
for i in tahta:
    print("\t".expandtabs(30), *i, end="\n"*2)

kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
[[0, 1], [1, 1], [2, 1]],
[[0, 2], [1, 2], [2, 2]],
[[0, 0], [0, 1], [0, 2]],
[[1, 0], [1, 1], [1, 2]],
[[2, 0], [2, 1], [2, 2]],
[[0, 0], [1, 1], [2, 2]],
[[0, 2], [1, 1], [2, 0]]]

x_durumu = []
o_durumu = []

sıra = 1
while True:
    if sıra % 2 == 0:
        print("sira pcde")
        işaret = "X".center(3)
        x = str(random.randint(0, 2)).ljust(30)
        y = str(random.randint(0, 2)).ljust(30)
    else:
        print("sira kullanicida")
        işaret = "O".center(3)
        x = input("Sira O da yukarıdan aşağıya [0, 1, 2]: ".ljust(30))
        y = input("Sira O da soldan sağa [0, 1, 2]: ".ljust(30))

    print()
    print("İŞARET: {}\n".format(işaret))

    if x == "q":
        break

    if y == "q":
        break

    x = int(x)
    y = int(y)

    print("\n" * 15)
    print("x alindi {} y alindi {}".format(x,y))

    if tahta[x][y] == "___":
        print("x eklendi {} y eklendi {}".format(x, y))
        tahta[x][y] = işaret

        if işaret == "X".center(3):
            x_durumu += [[x, y]]
            print("xin durumu : ", x_durumu)
        elif işaret == "O".center(3):
            o_durumu += [[x, y]]
            print("O nun durumu : ", o_durumu)
        sıra += 1
    else:
         print("\nORASI DOLU! TEKRAR DENEYİN\n")

    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n" * 2)

    for i in kazanma_ölçütleri:
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu]

        if len(o) == len(i):
            print("O KAZANDI!")
            quit()
        if len(x) == len(i):
            print("X KAZANDI!")
            quit()