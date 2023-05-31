# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? eg: 33  : ")
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])
# A variavel mapa tem uma lista com 3 itens, cada item seria outra lista que sao as rows, entao a variavel selected_row avisa QUAL ROW (ou seja, qual vertical) , se o usuario digitou 32, teremos row 3
selected_row = map[vertical -1]
# Agora que ja temos a ROW , ainda no 32, escolhemos a coluna 2
selected_row[horizontal - 1] = "X"




#Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")