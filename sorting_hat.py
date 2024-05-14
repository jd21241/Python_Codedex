print("Welcome to Hogwarts!")
print("Please take a seat and answer a few questions to determine your house.")
x = 0
gry = 0
rc = 0
hp = 0
sly = 0
print("Q1) Do you like Dawn or Dusk?")
print("    1) Dawn")
print("    2) Dusk")
x = int(input("Please enter 1 or 2 here "))
if x == 1:
    gry += 1
    rc += 1
elif x == 2:
    hp += 1
    sly += 1
else:
    print("Wrong input")
x = 0
print("Q2) When I'm dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
x = int(input("Please enter 1, 2, 3, or 4 here "))
if x == 1:
   hp += 2
elif x == 2:
    sly += 2
elif x == 3:
    rc += 2
elif x == 4:
    gry += 2
else:
   print("Wrong Input.")
x = 0
print("Q3) What kind of instrument most pleases your ear")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
x = int(input("Please enter 1, 2, 3, or 4 here "))
if x == 1:
  sly += 4
elif x == 2:
    hp += 4
elif x == 3:
    rc += 4
elif x == 4:
    gry += 4
else:
    print("Wrong Input.")
variables = {'Hufflepuff': hp, 'Slytherin': sly, 'Ravenclaw': rc, 'Gryffindor': gry}
max_points_var = max(variables, key=variables.get)
print(f"Your house is {max_points_var}.")