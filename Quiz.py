l1=[["how much time it takes the sun's rays to fall on earth?"],
    ["Who was Peter Parker?"],
    ["What gun is known to be the most reliable in the army?"],
    ["What is ohm's law?"],
    ["what does captain America says in climax of Avengers-Endgame"]]

print("WELCOME TO THE QUIZ GAME")
print()

print("---------------------")
print("LETS SEE HOW GOOD YOU ARE!!!!")

print()

print("Question 1")
is_playng=True

while is_playng:
    score=0
    print(l1[0][0])
    answer=input("Enter your answer: ")
    
    if answer=="8 minutes and 20 seconds":
        print("Correct")
        score+=1
    else:
        print("Wrong answer. Better luck next time")
    print()

print("-----------------------")

    print("Question 2")
    print(l1[1][0])
    answer=input("Enter your answer: ").title()
    
    if answer=="Spider Man":
        print("Correct")
        score+=1
    else:
        print("Wrong answer. Better luck next time")
    print()

print("-----------------------")

    print("Question 3")
    print(l1[2][0])
    answer=input("Enter your answer: ")
    
    if answer=="AK-47":
        print("Correct")
        score+=1
    else:
        print("Wrong answer. Better luck next time")
    print()

print("-----------------------")

    print("Question 4")
    print(l1[3][0])
    answer=input("Enter your answer: ")
    
    if answer=="V=IR":
        print("Correct")
        score+=1
            
    else:
        print("Wrong answer. Better luck next time")
        print()

print("-----------------------")

print("Question 5")
    print(l1[4][0])
    answer=input("Enter your answer: ")
    
    if answer=="I can do this all day":
        print("Correct")
        score+=1
        
    else:   
        print("Wrong Answer")
    is_playng=False 

print(f"CONGRATS!!! You have scored {score} points")
print("-------Thank You for playing the game!----------")
