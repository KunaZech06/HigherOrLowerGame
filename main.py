from art import logo
from art import vs
from game_data import data as question
import random
from replit import clear

play = True

#Function to produce question
def randomQuestion():
  number = random.randint(0, len(question)-1)
  qn = question[number]
  return qn

# Initialize questionOne and questionTwo
questionOne = randomQuestion()
questionTwo = randomQuestion()

if questionOne ==  questionTwo:
  questionOne = randomQuestion()
  questionTwo = randomQuestion()
  
score = 0

def game(questionOne, questionTwo, score):
    global play
    nameOne = questionOne["name"]
    countryOne = questionOne["country"]
    descriptionOne = questionOne["description"]
    followersOne = questionOne["follower_count"]
    
    nameTwo = questionTwo["name"]
    countryTwo = questionTwo["country"]
    descriptionTwo = questionTwo["description"]
    followersTwo = questionTwo["follower_count"]

    print(logo)
    print(f"Compare A: {nameOne}, {descriptionOne}, from {countryOne}.")
    print(vs)
    print(f"Compare B: {nameTwo}, {descriptionTwo}, from {countryTwo}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    #compare followers first
    if followersOne > followersTwo:
      answer = "a"
    else:
      answer = "b"

    if choice == answer:
      clear()
      score += 1
      print(f"You're right! Current score: {score}.")
      questionOne = questionTwo
      questionTwo = randomQuestion()
    else:
      clear()
      print(f"You're wrong! GAME OVER. Final score: {score}.")
      play = False

    return questionOne, questionTwo, score # Return the updated questions for the next round

while play:
  questionOne, questionTwo, score = game(questionOne, questionTwo, score)  # Call the function with the current questions and update them after each round
