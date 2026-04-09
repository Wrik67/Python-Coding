def minecraft():
    score = 0
    print("Answer 5 questions about Minecraft.")
    q1 = str(input("Question no 1: What is the powerful mob in minecraft- \n\tA)Ender Dragon \n\tB)Warden \n\tC)Wither\nEnter your choice from A/B/C: "))
    if q1.lower() == 'b':
        print("Correct! Let's go to next question.")
        score +=10
    else:
        print("Your answer is incorrect. Correct answer is b) Warden.")
        score -=5
        
    q2 = str(input("Question no 2: What is the powerful entity in minecraft- \n\tA)The Null \n\tB)Herobrine, \n\tC)Entity303: "))
    if q2.lower() == 'b':
        print("Correct! Let's go to next question.")
        score +=10
    else:
        print("Your answer is incorrect. Correct answer is b) Herobrine.")
        score -=5

    q3 = str(input("Question no 3: What is the name of the pillagers base in minecraft- \n\tA)Pillager tower \n\tB)Ocean monument \n\tC)village: "))
    if q3.lower() == 'a':
        print("Correct! Let's go to next question.")
        score +=10
    else:
        print("Your answer is incorrect. Correct answer is a) Pillager tower.")
        score -=5
 
    q4 = str(input("Question no 4: Which mob attak players with bow and arrow in minecraft- \n\tA)Zombie \n\tB)Spider \n\tC)Skeleton: "))
    if q4.lower() == 'c':
        print("Correct! Let's go to next question.")
        score -=10
    else:
        print("Your answer is incorrect. Correct answer is c) Skeleton.")
        score -=5
       
    q5 = str(input("Question no 5: Which mob attak players by teleporting in minecraft-  \n\tA)Creeper \n\tB)Enderman \n\tC)Zombie: "))
    if q5 == 'Enderman':
        print("Congants! You pass the 5 questions.")
        score +=10
    else:
        print("Your answer is incorrect. Correct answer is b) Herobrine.")
        score -=5

    return score

def roblox():
    print("Answer 5 questions about Roblox.")
    a1 = str(input("Question no 1: What is the cerrency of roblox- \n\tA)Euro \n\tB)Robux \n\tC)Dollar: "))
    if a1.lower() == 'b':
        print("Correct! Let's go to next question.")
        score +=10
    else:
        print("Your answer is incorrect. Correct answer is b) Robux.")
        score -=5
        
    a2 = str(input("Question no 2: Is roblox is free to download?- \n\tA)Maybe, \n\tB)No, \n\tC)Yes: "))
    if a2.lower() == 'c':
        print("Correct! Let's go to next question.")
        score +=10
    else:
        print("Your answer is incorrect. Correct answer is c) Yes.")
        score -=5
        
    a3 = str(input("Question no 3: Who is the CEO of Roblox- \n\tA)David Basuki, \n\tB)Bobby Kotick, \n\tC)Mojang: "))
    if a3.lower() == 'a':
        print("Correct! Let's go to next question.")
        score +=10
    else:
        print("Your answer is incorrect. Correct answer is a) David Basuki.")
        score -=5
        
    a4 = str(input("Question no 4: Is roblox a multiplayer game?- \n\tA)Yes, \n\tB)Maybe, \n\tC)No: "))
    if a4 == 'a':
        print("Correct! Let's go to next question.")
        score +=10
    else:
        print("Your answer is incorrect. Correct answer is a) Yes.")
        score -=5
        
    a5 = str(input("Question no 5: What is the latest roblox logo color- \n\tA)Black and White, \n\tB)Blue and White, \n\tC)Pink and White: "))
    if a5.lower() == 'b':
        print("Congants! You pass the 5 questions.")
        score +=10
    else:
        print("Your answer is incorrect. Correct answer is b)Blue and White")
        score -=5

    return score

g = str(input("Which game You like the most Roblox or Minecraft: "))

if g == 'Roblox':
    result = roblox()
    print("Your score is: ", result)

elif g.lower() == 'minecraft':
    result = minecraft()
    print("Your score is: ", result)
else:
    print("Invalid Input. Please enter a valid input.")
