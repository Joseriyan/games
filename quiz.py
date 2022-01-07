score = 0
score = int(score)

print("QUIZ")
question1 = "what is the nationl of india?"
options1 = "a.hindi\nb. Tamil\nc.  telugu\n"
print(question1)
print(options1)
while True:
    response1 = input("Hit 'a','b','c' for your answer\n")
    if response1 == "b":
        score = score + 1
    
        break
    else:print("Incorrect")
print("Your current score is " + str(score) + " out of 5")

question2 = "Who is the first president of india?"
options2 = "a.rajendra prasad\nd. radhakrishnan\nc. nehru\n"
print(question2)
print(options2)
while True:
    response2 = input("Hit 'a','b','c' for your answer\n")
    if response2 == "c":
        score = score + 1
        break
    else:print("Incorrect")
print("Your current score is " + str(score) + " out of 5")

question3 = "When the second world war started?"
options3 = "a.1939\nb. 1940\nc.  1941\n"
print(question3)
print(options3)
while True:
    response3 = input("Hit 'a','b','c'  for your answer\n")
    if response3 == "a":
        score = score + 1
        break
    else:print("Incorrect")
    
print("Your current score is " + str(score) + " out of 5")

question4 = "When is the statue of liberty was constructed?"
options4 = "a.1875\nb. 1876\nc. 1877\n"
print(question4)
print(options4)
while True:
    response4 = input("Hit 'a','b','c' for your answer\n")
    if response4 == "a":
        score = score + 1
        break
    else:print("Incorrect")
  
print("Your current score is " + str(score) + " out of 5")

question5 = "what is the height of the burj khalifa?"
options5 = "a.828\nb.  300m\nc.  829\n"
print(question5)
print(options5)
while True:
    response5 = input("Hit 'a','b'' for your answer\n")
    if response5 == "a":
        score = score + 1
        break
    else:print("Incorrect")
    
print("Your current score is " + str(score) + " out of 5")

print("Your total score is " + str(score) + " out of 5")
print("finished {}, game over!")
