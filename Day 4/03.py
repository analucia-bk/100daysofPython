row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
coluna = int(position[0])
linha = int(position[1])
map[linha-1][coluna-1] = "X"
print(f"{row1}\n{row2}\n{row3}")