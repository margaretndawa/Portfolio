from msvcrt import kbhit
from re import L


weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit == "K" or "k":
   topounds = weight * 2.21
   print("Weight in Lbs: " + str(topounds))
elif unit == "L" or "l":
   tokilos = weight * 0.45
   print("Weight in Kgs: " + str(tokilos))
else:
    print("Invalid input")