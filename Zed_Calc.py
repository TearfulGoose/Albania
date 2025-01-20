#Ehem, Yes I can simplifiy this, but erm, it works anyways and I can read it- I geniunly don't use Functions or def thingys because I'm so used to just making the stuff with the simpler tools xd

import time #Sleeping zzzz

def typing(TestV,timeS):
  for i in range(len(TestV)):
    print(TestV[i],end="",flush=True)
    time.sleep(timeS)

print("No")
#Variables saved outside to be reused.

numb1 = 0
numb2 = 0
XHasSaved = False
YHasSaved = False
ZHasSaved = False
SavedNumX = 0
SavedNumY = 0
SavedNumZ = 0


# TESTING IF GIVEN NUMBER IS GIVEN NUMBER (FAIL SAFE)
# While True is a loop
# Try:   -- Will test the function of the code
#. Break - We break the loop if the test was successful
# Except: -- If the try fails, it will land here
#. Continue -- Will repeat again to try  


while True:

  # Variables using inside the while true (Meaning it will refresh every restart)
  Operator = 0
  OperatorX = 0
  OperatorY = 0
  OperatorZ = 0
  XBeingUsed = False
  YBeingUsed = False
  ZBeingUsed = False
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("") #Dialog Disapearing thingy
  typing("Calculator",0.01)
  print("")

  while True:
    try:
      if XHasSaved == True:  #We will see if anything is saved in X.
        typing("Found Interger Saved, would you like to use it?",0.01)
        print("")
        typing("X = ",0.01)
        typing(str(SavedNumX),0.01)
        print("")
        typing("1. Yes",0.01)
        print("")
        typing("2. No", 0.01)
        print("")
        Use = int(input(""))

        if Use == 1:
          XBeingUsed = True #Will use for detection that we want to use this next line in the code.
          break
        elif Use == 2:
          XBeingUsed = False
          break
        else:
          typing("Invalid Answer, please try again.",0.01)
          continue

      break
    except ValueError:
      typing("Invalid Answer, please try again.",0.01)
      continue

  while True:
    try:

      if YHasSaved == True:  #We will see if anything is saved in Y.
        typing("Found Interger Saved, would you like to use it?",0.01)
        print("")
        typing("Y = ",0.01)
        typing(str(SavedNumY),0.01)
        print("")
        typing("1. Yes",0.01)
        print("")
        typing("2. No", 0.01)
        print("")
        Use = int(input("")) #Asking for number

        if Use == 1:
          YHasSaved = True #Will use for detection that we want to use this next line in the code.
          break
        elif Use == 2:
          YHasSaved = False
          break
        else:
          typing("Invalid Answer, please try again.",0.01) #If number is not between 1-2 then it will request for an input that is withen that. (This goes for all the other simular code.)
          continue

      break
    except ValueError:
      typing("Invalid Answer, please try again.",0.01) #If the Try fails, it will recall here and continue the loop until the Try succeeds.
      continue


  while True:
    try:
      if ZHasSaved == True:  #We will see if anything is saved in Z.
        typing("Found Interger Saved, would you like to use it?",0.01)
        print("")
        typing("Z = ",0.01)
        typing(str(SavedNumZ),0.01)
        print("")
        typing("1. Yes",0.01)
        print("")
        typing("2. No",0.01)
        Use = int(input("")) #Asking for number

        if Use == 1:
          ZBeingUsed = True #Will use for detection that we want to use this next line in the code.
          break
        elif Use == 2:
          ZBeingUsed = False
          break
        else:
          typing("Invalid Answer, please try again.",0.01)
          continue

      break
    except ValueError:
      typing("Invalid Answer, please try again.",0.01)
      continue


  if XBeingUsed == True:
    while True:
      try:
        typing("Detecting using X.",0.01)
        print("")
        typing("X = ",0.01)
        typing(str(SavedNumX),0.01)
        print("")
        typing("Please give an operator for X to be added into your main equation.",0.01)
        print("")

        typing("1. Addition",0.01)
        print("")
        typing("2. Subtraction",0.01)
        print("")
        typing("3. Multiplication",0.01)
        print("")
        typing("4. Division",0.01)
        print("")
        typing("5. Exponent",0.01)
        print("")
        ChoseOp = int(input("")) #Asking for number
        OperatorX = ChoseOp
        print("")
        if ChoseOp == 1:
          typing("You have chosen Addition",0.01)
        elif ChoseOp == 2:
          typing("You have chosen Subtraction",0.01)
        elif ChoseOp == 3:
          typing("You have chosen Multiplication",0.01)
        elif ChoseOp == 4:
          typing("You have chosen Division",0.01)
        elif ChoseOp == 5:
          typing("You have chosen Exponent",0.01)
        else:
          typing("Invalid input",0.01)
          continue
        break
      except ValueError:
        typing("Invalid Answer, please try again.",0.01)
        continue

  if YBeingUsed == True:
    while True:
      try:
        typing("Detecting using Y.",0.01)
        print("")
        typing("Y = ",0.01)
        typing(str(SavedNumY),0.01)
        print("")
        typing("Please give an operator for Y to be added into your main equation.",0.01)
        print("")

        typing("1. Addition",0.01)
        print("")
        typing("2. Subtraction",0.01)
        print("")
        typing("3. Multiplication",0.01)
        print("")
        typing("4. Division",0.01)
        print("")
        typing("5. Exponent",0.01)
        print("")
        ChoseOp = int(input("")) #Asking for number
        OperatorY = ChoseOp
        print("")
        if ChoseOp == 1:
          typing("You have chosen Addition",0.01)
        elif ChoseOp == 2:
          typing("You have chosen Subtraction",0.01)
        elif ChoseOp == 3:
          typing("You have chosen Multiplication",0.01)
        elif ChoseOp == 4:
          typing("You have chosen Division",0.01)
        elif ChoseOp == 5:
          typing("You have chosen Exponent",0.01)
        else:
          typing("Invalid input",0.01)
          continue
        break
      except ValueError:
        typing("Invalid Answer, please try again.",0.01)
        continue

  if ZBeingUsed == True:
    while True:
      try:
        typing("Detecting using Z.",0.01)
        print("")
        typing("Z = ",0.01)
        typing(str(SavedNumZ),0.01)
        print("")
        typing("Please give an operator for Z to be added into your main equation.",0.01)
        print("")

        typing("1. Addition",0.01)
        print("")
        typing("2. Subtraction",0.01)
        print("")
        typing("3. Multiplication",0.01)
        print("")
        typing("4. Division",0.01)
        print("")
        typing("5. Exponent",0.01)

        ChoseOp = int(input("")) #Asking for number
        OperatorZ = ChoseOp
        print("")
        if ChoseOp == 1:
          typing("You have chosen Addition",0.01)
        elif ChoseOp == 2:
          typing("You have chosen Subtraction",0.01)
        elif ChoseOp == 3:
          typing("You have chosen Multiplication",0.01)
        elif ChoseOp == 4:
          typing("You have chosen Division",0.01)
        elif ChoseOp == 5:
          typing("You have chosen Exponent",0.01)
        else:
          typing("Invalid input",0.01)
          continue
        break
      except ValueError:
        typing("Invalid Answer, please try again.",0.01)
        continue
  print("")
  typing("Going into Main Equation",0.01)
  typing("...",1)
  print("")
  print("")
  typing("Please choose an operator",0.01)
  print("")
  typing("1. Addition",0.01)
  print("")
  typing("2. Subtraction",0.01)
  print("")
  typing("3. Multiplication",0.01)
  print("")
  typing("4. Division",0.01)
  print("")
  typing("5. Exponent",0.01)

  while True:
    try:
      print("")
      ChosenOp = int(input("")) #Asking for number
      Operator = ChosenOp

      if ChosenOp == 1:
        typing("You have chosen Addition",0.01)
        break
      elif ChosenOp == 2:
        typing("You have chosen Subtraction",0.01)
        break
      elif ChosenOp == 3:
        typing("You have chosen Multiplication",0.01)
        break
      elif ChosenOp == 4:
        typing("You have chosen Division",0.01)
        break
      elif ChosenOp == 5:
        typing("You have chosen Exponent",0.01)
        break
      else:
        typing("Invalid input",0.01)
        continue
    except ValueError:
      continue
  print("")
  typing("Please inpute the first number.",0.01)
  print("")

  while True:
    try:
      ChosenOp = float(input("")) #Asking for float #
      numb1 = ChosenOp

      break
    except ValueError:
      print("")
      typing("The number seems to be invalid or is not a number, please input the first number:",0.01)
      print("")
      continue

  print("")
  typing("Please inpute the second number.",0.01)
  print("")

  while True:
    try:
      ChosenOp = float(input("")) #Asking for float #
      numb2 = ChosenOp

      break
    except ValueError:
      print("")
      typing("The number seems to be invalid or is not a number, please input the second number:",0.01)
      print("")
      continue



  print("")
  typing("Computing numbers",0.01)
  typing("...",1)
  print("")

  FinalNumber = 0 #had to use because there was a weird bug that kept changing the AnserOp? so I decided to use a different variable for the end.

  AnswerOp = 0 #Saving the final number to be fully added in the end.

  # Selve explained, if operator is one of the number chosen, then it will pring out those text

  if Operator == 1:
    typing(str(numb1),0.01)
    typing(" + ",0.01)
    typing(str(numb2),0.01)

    AnswerOp = numb1 + numb2
  elif Operator == 2:
    typing(str(numb1),0.01)
    typing(" - ",0.01)
    typing(str(numb2),0.01)

    AnswerOp = numb1 - numb2
  elif Operator == 3:
    typing(str(numb1),0.01)
    typing(" * ",0.01)
    typing(str(numb2),0.01)

    AnswerOp = numb1 * numb2
  elif Operator == 4:
    typing(str(numb1),0.01)
    typing(" / ",0.01)
    typing(str(numb2),0.01)

    AnswerOp = numb1 / numb2
  elif Operator == 5:
    typing(str(numb1),0.01)
    typing(" ^ ",0.01)
    typing(str(numb2),0.01)

    AnswerOp = numb1 ** numb2

  #If any of this bellow are being used, then it will add itself into the final anser, as well as text out itself.

  if XBeingUsed == True:
      if OperatorX == 1:
        typing(" + ",0.01)
        typing(str(SavedNumX),0.01)
        AnswerOp += SavedNumX
      elif OperatorX == 2:
        typing(" - ",0.01)
        typing(str(SavedNumX),0.01)
        AnswerOp -= SavedNumX
      elif OperatorX == 3:
        typing(" * ",0.01)
        typing(str(SavedNumX),0.01)
        AnswerOp *= SavedNumX
      elif OperatorX == 4:
        typing(" / ",0.01)
        typing(str(SavedNumX),0.01)
        AnswerOp /= SavedNumX
      elif OperatorX == 5:
        typing(" ^ ",0.01)
        typing(str(SavedNumX),0.01)
        AnswerOp **= SavedNumX

  if YBeingUsed == True:
    if OperatorY == 1:
      typing(" + ",0.01)
      typing(str(SavedNumY),0.01)
      AnswerOp += SavedNumY
    elif OperatorY == 2:
      typing(" - ",0.01)
      typing(str(SavedNumY),0.01)
      AnswerOp -= SavedNumY
    elif OperatorY == 3:
      typing(" * ",0.01)
      typing(str(SavedNumY),0.01)
      AnswerOp *= SavedNumY
    elif OperatorY == 4:
      typing(" / ",0.01)
      typing(str(SavedNumY),0.01)
      AnswerOp /= SavedNumY
    elif OperatorY == 5:
      typing(" ^ ",0.01)
      typing(str(SavedNumY),0.01)
      AnswerOp **= SavedNumY

  if ZBeingUsed == True:
    if OperatorZ == 1:
      typing(" + ",0.01)
      typing(str(SavedNumZ),0.01)
      AnswerOp += SavedNumZ
    elif OperatorZ == 2:
      typing(" - ",0.01)
      typing(str(SavedNumZ),0.01)
      AnswerOp -= SavedNumZ
    elif OperatorZ == 3:
      typing(" * ",0.01)
      typing(str(SavedNumZ),0.01)
      AnswerOp *= SavedNumZ
    elif OperatorZ == 4:
      typing(" / ",0.01)
      typing(str(SavedNumZ),0.01)
      AnswerOp /= SavedNumZ
    elif OperatorZ == 5:
      typing(" ^ ",0.01)
      typing(str(SavedNumZ),0.01)
      AnswerOp **= SavedNumZ


  typing(" = ",0.01)
  typing(str(AnswerOp),0.01)
  FinalNumber = AnswerOp #Transfering AnswerOp to Final number, in case AnswerOp somehow changes through out the code.
  

  print("")
  typing("Would you like to save this input?",0.01)
  print("")
  typing("1. Yes",0.01)
  print("")
  typing("2. No",0.01)
  print("")

  Yes = False
  while True:
    try:
      ChosenOp = int(input("")) #Asking Number
      if ChosenOp == 1:
        Yes = True 
        break
      elif ChosenOp == 2:
        Yes = False
        break
    except ValueError:
      print("")
      typing("The number seems to be invalid or is not a number, please input a number :",0.01)
      print("")
      continue

  if Yes == True:
    typing("Please choose a variable to save it in or replace.",0.01)
    print("")
    if XHasSaved == True: #Check if there is already something in X to allow the user to Overrun the variable if wanted.
      typing("1. X (Currently)", 0.01)
      typing(str(SavedNumX), 0.01)
    else:
      typing("1. X",0.01)
    print("")
    if YHasSaved == True: #Check if there is already something in Y to allow the user to Overrun the variable if wanted.
      typing("2. Y (Currently)", 0.01)
      typing(str(SavedNumY), 0.01)
    else:
      typing("2. Y",0.01)
    print("")
    if ZHasSaved == True: #Check if there is already something in Z to allow the user to Overrun the variable if wanted.
      typing("3. Z (Currently)", 0.01)
      typing(str(SavedNumZ), 0.01)
    else:
      typing("3. Z",0.01)
    print("")

    while True:
      try:
        ChosenOp = int(input("")) #Asking for number
        if ChosenOp == 1:
          SavedNumX = FinalNumber #Saving the Final number to The outside Variable
          typing("Variable Saved ",0.01)
          typing("X = ",0.01)
          typing(str(FinalNumber),0.01)
          XHasSaved = True #The Variable now has a number in it.
          break
        elif ChosenOp == 2:
          SavedNumY = FinalNumber #Saving the Final number to The outside Variable
          typing("Variable Saved ",0.01)
          typing("Y = ",0.01)
          typing(str(FinalNumber),0.01)
          YHasSaved = True #The Variable now has a number in it.
          break
        elif ChosenOp == 3:
          SavedNumZ = FinalNumber #Saving the Final number to The outside Variable
          typing("Variable Saved ",0.01)
          typing("Z = ",0.01)
          typing(str(FinalNumber),0.01)
          ZHasSaved = True #The Variable now has a number in it.
          break
        else:
          typing("Invalid input",0.01)
          continue

      except ValueError:
        print("")
        typing("The number seems to be invalid or is not a number, please input a number :",0.01)
        print("")
        continue
  #Then the code repeats.
