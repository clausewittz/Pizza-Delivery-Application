print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill=0
cheese=1
pepperoni_m_l=3
pepperoni=2

# S - M - L and Y - N choices must be written capital.

if size == "S":
  print('size = "S"')
  s_pizza=15
  bill = s_pizza
  if add_pepperoni == "Y":
    bill = bill + pepperoni
  else:
    pass

  if extra_cheese == "Y":
    bill = bill + cheese
    print(f"Your final bill is {bill}")
  else:
    print(f"Your finall bill is {bill}")

  

elif size == "M":
  print('size = "M"')
  m_pizza=20
  bill = m_pizza
  if add_pepperoni == "Y":
    bill = bill + pepperoni_m_l
  else:
    pass
  
  if extra_cheese == "Y":
    bill = bill + cheese
    print(f"Your final bill is {bill}")
  else:
    print(f"Your final bill is {bill}")

  

elif size == "L":
  print('size = "L"')
  l_pizza=25
  bill = l_pizza
  if add_pepperoni == "Y":
    bill = bill + pepperoni_m_l
  else:
    pass

  if extra_cheese == "Y":
    bill = bill + cheese
    print(f"Your final bill is {bill}")
  else:
    print(f"Your final bill is {bill}")

else:
  print(f"There is no {size} pizza size.")
  print("You can only pick S, M or L.")
