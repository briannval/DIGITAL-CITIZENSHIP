# CATATAN / NOTE !
# SET OUTPUT TO FULL SCREEN !

import random
import time
import replit
import datetime
import pandas as pd
from colorama import Fore


activeprogram = 1
userinfo = []
#DISPLAY FUNCTIONS
def datadisplay(a,b,c,d):
  replit.clear()
  print(Fore.BLUE+"="*70)
  print(Fore.RED+"Data of citizens")
  print(df.iloc[a:b,c:d])
  print()
  print("Enter to keep going")
  print(Fore.BLUE+"="*70)

def personaldatacollection():
  #Personal Class
  #NAME
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"We will now begin the digital citizenship survey")
  print("What is your name?")
  print(Fore.BLUE+"="*50)
  a = input()
  userinfo.append(a)
  replit.clear()
  #AGE
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"What is your age?")
  print(Fore.BLUE+"="*50)
  a = int(input())
  userinfo.append(a)
  replit.clear()
  #GENDER
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"What is your gender? (M/F)")
  print(Fore.BLUE+"="*50)
  a = input()
  userinfo.append(a.upper())
  replit.clear()

  #Health class
  #HEIGHT
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"What is your height? (cm)")
  print(Fore.BLUE+"="*50)
  a = (int(input()))/100
  userinfo.append(a)
  replit.clear()
  #WEIGHT
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"What is your weight? (kg)")
  print(Fore.BLUE+"="*50)
  a = int(input())
  userinfo.append(a)
  replit.clear()
  #HEARTRATE
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"What is your heart rate? (bpm)")
  print(Fore.BLUE+"="*50)
  a = int(input())
  userinfo.append(a)
  replit.clear()

  #Education class
  #SCHOOL
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"What is the school/institute you go to?")
  print(Fore.BLUE+"="*50)
  a = input()
  userinfo.append(a)
  replit.clear()
  #SCHOOLLOCATION
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Where is your school/institute located?")
  print("Jakarta-Bogor-Depok-Tangerang-Bekasi")
  print(Fore.BLUE+"="*50)
  a = input()
  userinfo.append(a)
  replit.clear()
  #STUDYTIME
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"How many hours do you study a day?")
  print(Fore.BLUE+"="*50)
  a = int(input())
  userinfo.append(a)
  replit.clear()

  #Commerce class
  #WEBSITE
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Choose one of three")
  print("Shopee-BliBli-Tokopedia")
  print(Fore.BLUE+"="*50)
  a = input()
  userinfo.append(a)
  replit.clear()
  #TIMESPENT
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"How long do you spend shopping? (hours)")
  print(Fore.BLUE+"="*50)
  a = int(input())
  userinfo.append(a)
  replit.clear()
  #ONLINEORNOT
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Do you prefer shopping online? (Y/N)")
  print(Fore.BLUE+"="*50)
  a = input()
  userinfo.append(a.upper())
  replit.clear()

  #Booking class
  #WEBSITE
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Choose one of these movie genres")
  print("Action-Drama-Comedy-Horror-Thriller-Romance-Adventure-Mystery")
  print(Fore.BLUE+"="*50)
  a = input()
  userinfo.append(a)
  replit.clear()
  #AIRLINE
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Choose one of these airlines")
  print("Qatar-Cathay-Japan-ANA-Emirates-Garuda-British-Asia-Lion")
  print(Fore.BLUE+"="*50)
  a = input()
  userinfo.append(a)
  replit.clear()





def initdisplay(text):
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Hello, welcome to the digital companion app!")
  print("Your path to become a digital citizen")
  print("PLEASE VIEW CONSOLE IN FULL SCREEN")
  print()
  print()
  print(Fore.RED+text)
  x = datetime.datetime.now()
  print(" "*25+Fore.WHITE+x.strftime("%c"))
  print(Fore.BLUE+"="*50)
  input()
  replit.clear()
def loading(num):
  for i in range(num):
    print(Fore.BLUE+"="*50)
    print(Fore.WHITE+"Loading "+"."*i)
    print(Fore.RED+"Please wait for "+str(num-i)+" seconds")
    print(Fore.BLUE+"="*50)
    time.sleep(1)
    replit.clear()
def welcome(name):
  print(Fore.BLUE+"="*70)
  print(Fore.GREEN+name+Fore.WHITE+", welcome, you are officially a digital citizen!")
  print("Please select one of the few things to do below")
  print("1. Explore trends of citizens")
  print("2. Test your digital citizenship knowledge")
  print("3. Play a game")
  print("4. Exit")
  print()
  x = datetime.datetime.now()
  print(" "*25+x.strftime("%c"))
  print(Fore.BLUE+"="*70)
  choice = int(input())
  replit.clear()
  return choice
def sectors():
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Please select one of the sectors")
  print("1. Health")
  print("2. Education")
  print("3. Commerce")
  print("4. Booking")
  print()
  x = datetime.datetime.now()
  print(" "*25+x.strftime("%c"))
  print(Fore.BLUE+"="*50)
  choice = int(input())
  replit.clear()
  return choice

#THIS IS THE QUIZ CODE
class Quiz:
  scoring = [(200,"A"),(200,"B"),(200,"C"),(300,"D"),(300,"D"),(300,"C"),(400,"B"),(400,"A"),(400,"A"),(400,"A")]
  easynumbers = [0,1,2]
  mediumnumbers = [0,1,3,4,5,6]
  hardnumbers = [0,1,2,3,4,5,6,7,8,9]
  questions = [("What does a good digital citizen not do?","Insult","Respect","Protect","Educate"),("What is not an element in digital citizenship?","Literacy","Boredom","Health","Access"),("How can a child be a good digital citizen?","Gadget from birth","Having 3 different phones","Responsible act from child and parent","Sharing all their personal information"),("Which is a component of digital citizenship?","Privacy & Security","Media Balance & Well-Being","Digital Footprint & Identity","All of the above"),("Which citizenship component is power of words included in?","Media Balance & Well-Being","Privacy & Security","Digital Footprint & Identity","Cyberbullying, Digital Drama & Hate Speech"),("Where can you find trusted information about computer science?","A person who followed you on IG","An unsolicited website","Coding Bee Academy","All of the above"),("What is the gap between a digital and non-digital citizen called?","Social isolation","Digital divide","Economic stagnation","E-democracy"),("Six out of ten American teachers used digital citizenship curriculum, this was brought up by?","Common Sense Media","Federal Trade Commission","MySpace","Google G Suites"),("How many percent of teenagers use computers?","Over 90 percent","80-90 percent","75-80 percent","50 percent"),("Which organization stated that digital citizenship platform will be beneficial to Indonesia?","BSSN","Cloud Computing Indonesia","MAFINDO","Drone Empirit")]
  timer = 10
  defaulttimer = 0
  defaultnumbers = []
  rules = [("easy",5,"no addition of score",3),("medium",4,"a minus of 100 points",6),("hard",2,"a minus of 150 points",10)]
  score = 0
  useranswer = ""
  
  def __init__(self,name):
    Quiz.timer = 10
    Quiz.score = 0
    print(Fore.BLUE+"="*50)
    print("Welcome to the digital citizenship quiz!")
    print("")
    print(Fore.RED+"Choose from level 1-3...")
    print(Fore.BLUE+"="*50)
    level = int(input())
    self.player = name
    self.level = level
    replit.clear()

  def setrules(self):
    Quiz.defaulttimer = Quiz.rules[self.level-1][1]
    if self.level == 1:
      Quiz.defaultnumbers = Quiz.easynumbers
    elif self.level == 2:
      Quiz.defaultnumbers = Quiz.mediumnumbers
    elif self.level == 3:
      Quiz.defaultnumbers = Quiz.hardnumbers
    print(Fore.BLUE+"="*70)
    print(Fore.WHITE+"RULES")
    print("You have chosen "+Fore.GREEN+f"{Quiz.rules[self.level-1][0]} "+Fore.WHITE+"difficulty")
    print(Fore.WHITE+"In this level, you will have "+Fore.GREEN+f"{Quiz.defaulttimer} "+Fore.WHITE+"seconds to view the question")
    print("Make sure to only answer after the timer runs out")
    print("An incorrect answer will result you in "+Fore.GREEN+f"{Quiz.rules[self.level-1][2]}")
    print(Fore.WHITE+"You will have to answer "+Fore.GREEN+f"{Quiz.rules[self.level-1][3]}"+Fore.WHITE+" questions in this level")
    print("Please answer is uppercase only")
    print(Fore.RED+"Press enter to start")
    print(Fore.BLUE+"="*70)
    input()
    replit.clear()

  def resultstatement(self):
    print(Fore.BLUE+"="*50)
    print(Fore.GREEN+f"{self.player}"+Fore.WHITE+", you got "+Fore.GREEN+f"{Quiz.score} "+Fore.WHITE+"points in level "+Fore.GREEN+f"{self.level}.")
    print("Thanks for taking the quiz!")
    print(Fore.BLUE+"="*50)
    input()
    replit.clear()
  

  def readystatement(self):
    print(Fore.BLUE+"="*50)
    print(Fore.GREEN+f"{self.player}"+Fore.WHITE+", you have chosen level "+Fore.GREEN+f"{self.level}"+Fore.RED+", press enter")
    print(Fore.BLUE+"="*50)
    input()
    replit.clear()

  def loading(self):
    for i in range(3):
      print(Fore.BLUE+"="*50)
      print(Fore.WHITE+"Loading "+"."*i)
      print(Fore.RED+"Please wait for "+str(3-i)+" seconds")
      print(Fore.BLUE+"="*50)
      time.sleep(1)
      replit.clear()


  def qna(self):
    for nums in Quiz.defaultnumbers:
      Quiz.timer = Quiz.defaulttimer
      Quiz.useranswer = ""
      while Quiz.timer > -1:
        print(Fore.BLUE+"="*50)
        print(Fore.WHITE+Quiz.questions[nums][0])
        print(f"A. {Quiz.questions[nums][1]}")
        print(f"B. {Quiz.questions[nums][2]}")
        print(f"C. {Quiz.questions[nums][3]}")
        print(f"D. {Quiz.questions[nums][4]}")
        print()
        print(Fore.WHITE+"You have "+Fore.GREEN+f"{Quiz.timer} "+Fore.WHITE+"seconds.")
        print(Fore.BLUE+"="*50)
        time.sleep(1)
        Quiz.timer-=1
        replit.clear()
      print(Fore.BLUE+"="*50)
      print(Fore.WHITE+"What is your answer?")
      print(Fore.BLUE+"="*50)
      Quiz.useranswer = input()
      replit.clear()
      if Quiz.useranswer == Quiz.scoring[nums][1]:
          Quiz.score += Quiz.scoring[nums][0]
      elif Quiz.useranswer != Quiz.scoring[nums][1] and self.level == 2:
        Quiz.score -= 100
      elif Quiz.useranswer != Quiz.scoring[nums][1] and self.level == 3:
        Quiz.score -= 150
      for i in range(3):
        print(Fore.BLUE+"="*50)
        print(Fore.WHITE+"Current score: "+Fore.GREEN+f"{Quiz.score} "+Fore.WHITE+"points")
        print("Proceeding in "+str(3-i))
        print(Fore.BLUE+"="*50)
        time.sleep(1)
        replit.clear()
        

#THIS IS THE PERSONAL CODE
class Personal:
  state = ()

  def __init__(self,data):
    self.name = data[0]
    self.age = data[1]
    if data[2] == "M":
      self.gender = "Male"
    elif data[2] == "F":
      self.gender = "Female"
    self.height = data[3]
    self.weight = data[4]
    self.heartrate = data[5]
    self.school = data[6]
    self.location = data[7]
    self.hoursstudy = data[8]
    self.favshopping = data[9]
    self.hoursshopping = data[10]
    self.preferonline = data[11]
    self.favgenre = data[12]
    self.favairline = data[13]

  def generalstatement(self):
    print(Fore.BLUE+"="*70)
    print(Fore.WHITE+f"Your name is "+Fore.GREEN+f"{self.name}"+Fore.WHITE+", currently "+Fore.GREEN+f"{self.age} "+Fore.WHITE+"years old, and you are a "+Fore.GREEN+f"{self.gender}.")
    print(Fore.WHITE+"Which digital data trend do you want to see?")
    print("1. All data")
    print("2. Health data")
    print("3. Education data")
    print("4. Commerce data")
    print("5. Preferences survey")
    print("6. Back to menu")
    print(Fore.BLUE+"="*70) 

  def healthcalc(self):
    number = int(self.weight /(self.height**2))
    if number < 18.5:
      condition = "underweight"
    elif number < 25:
      condition = "fit"
    elif number < 30:
      condition = "overweight"
    elif number < 35:
      condition = "obese"
    elif number >= 35:
      condition = "extremely obese"
    if self.heartrate < 35:
      condition2 = "unusually low"
    elif self.heartrate < 50:
      condition2 = "normal if you are athletic"
    elif self.heartrate < 90:
      condition2 = "normal for most people"
    elif self.heartrate < 100:
      condition2 = "in high risk territory"
    elif self.heartrate >= 100:
      condition2 = "in extremely high danger"
    Personal.state = (number,condition,condition2)

  def healthstatement(self):
    print(Fore.BLUE+"="*70)
    print(Fore.GREEN+f"{self.name}"+Fore.WHITE+", you are "+Fore.GREEN+f"{self.height} "+Fore.WHITE+"m tall, and weigh "+Fore.GREEN+f"{self.weight}"+Fore.WHITE+" kg.")
    print(Fore.WHITE+"You have a calculated BMI of "+Fore.GREEN+f"{Personal.state[0]}"+Fore.WHITE+", which is "+Fore.GREEN+f"{Personal.state[1]}.")
    print(Fore.WHITE+"Your regular heart rate is "+Fore.GREEN+f"{self.heartrate} "+Fore.WHITE+"bpm, which is "+Fore.GREEN+f"{Personal.state[2]}")
    print(Fore.BLUE+"="*70)

  def educationstatement(self):
    print(Fore.BLUE+"="*70)
    print(Fore.WHITE+"You are currently studying in "+Fore.GREEN+f"{self.school}.")
    print(Fore.WHITE+"It is located in "+Fore.GREEN+f"{self.location}.")
    print(Fore.WHITE+"You study for "+Fore.GREEN+f"{self.hoursstudy} "+Fore.WHITE+"hours per day.")
    print(Fore.BLUE+"="*70) 

  def commercestatement(self):
    if self.preferonline == "Y": 
      print(Fore.BLUE+"="*50)
      print(Fore.WHITE+"You prefer "+Fore.GREEN+f"{self.favshopping} "+Fore.WHITE+"as a shopping site.")
      print(Fore.WHITE+"You spend "+Fore.GREEN+f"{self.hoursshopping} "+Fore.WHITE+"shopping online.")
      print(Fore.WHITE+"Yes, you do like shopping online.")
      print(Fore.BLUE+"="*50)
    elif self.preferonline == "N":
      print(Fore.BLUE+"="*50)
      print(Fore.WHITE+"You prefer "+Fore.GREEN+f"{self.favshopping} "+Fore.WHITE+"as a shopping site.")
      print(Fore.WHITE+"You spend "+Fore.GREEN+f"{self.hoursshopping} "+Fore.WHITE+"shopping online.")
      print(Fore.WHITE+"No, you dislike shopping online.")
      print(Fore.BLUE+"="*50)

  def preferencestatement(self):
    print(Fore.BLUE+"="*70)
    print(Fore.WHITE+"You have a favourite movie genre of "+Fore.GREEN+f"{self.favgenre}.")
    print(Fore.WHITE+"You have a favourite airline of "+Fore.GREEN+f"{self.favairline}.")
    print(Fore.BLUE+"="*70)

  def appendtodf(self):
    all = [self.name,self.age,self.gender,self.height,self.weight,self.heartrate,self.school,self.location,self.hoursstudy,self.favshopping,self.hoursshopping,self.preferonline,self.favgenre,self.favairline,Personal.state[0],Personal.state[1],Personal.state[2]]
    return(all)

class GuessNumber:
  def __init__(self,name):
    self.name = name
    self.num = 0
    self.win = 0
    print(Fore.BLUE+"="*50)
    print(Fore.WHITE+"Welcome to the number guessing game, "+Fore.GREEN+f"{self.name}.")
    print(Fore.RED+"Please select the range of numbers.")
    print("1. 100")
    print("2. 1000")
    print("3. 10000")
    print(Fore.BLUE+"="*50)
    a = int(input())
    if a == 1:
      self.number = random.randint(1,100)
    elif a == 2:
      self.number = random.randint(1,1000)
    elif a == 3:
      self.number = random.randint(1,10000)
    replit.clear()
    print(Fore.BLUE+"="*50)
    print(Fore.RED+"Choose how many times you want to guess the number between 1 and "+Fore.GREEN+f"{self.number}")
    print(Fore.WHITE+"1. 10")
    print("2. 15")
    print("3. 20")
    print(Fore.BLUE+"="*50)
    a = int(input())
    if a == 1:
      self.chance = 10
    elif a == 2:
      self.chance = 15
    elif a == 3:
      self.chance = 20
    replit.clear()
    print(Fore.BLUE+"="*50)
    print(Fore.WHITE+"Splendid, let's begin!")
    print(Fore.RED+"Click enter to continue")
    print(Fore.BLUE+"="*50)
    input()
    replit.clear()
  
  def initloading(self):
    for i in range(4):
      print(Fore.BLUE+"="*50)
      print(Fore.WHITE+"Calculating numbers."+"."*i)
      print(Fore.BLUE+"="*50)
      time.sleep(1)
      replit.clear()
  
  def endloading(self):
    for i in range(4):
      print(Fore.BLUE+"="*50)
      print(Fore.WHITE+"Wrapping it up."+"."*i)
      print(Fore.BLUE+"="*50)
      time.sleep(1)
      replit.clear()

  def cycle(self):
    self.num = 0
    self.win = 0
    for i in range(self.chance):
      print(Fore.BLUE+"="*50)
      print(Fore.RED+"Guess a number")
      print(Fore.WHITE+"Chances left: "+Fore.GREEN+f"{self.chance-i}")
      print(Fore.BLUE+"="*50)
      self.num = int(input())
      replit.clear()
      if self.number > self.num:
        print(Fore.BLUE+"="*50)
        print(Fore.WHITE+"The correct number is GREATER than "+Fore.GREEN+f"{self.num}.")
        print(Fore.RED+"Press enter")
        print(Fore.BLUE+"="*50)
        input()
      elif self.number < self.num:
        print(Fore.BLUE+"="*50)
        print(Fore.WHITE+"The correct number is SMALLER than "+Fore.GREEN+f"{self.num}.")
        print(Fore.RED+"Press enter")
        print(Fore.BLUE+"="*50)
        input()
      elif self.number == self.num:
        self.win = 1
        break
      replit.clear()

  def results(self):
    if self.win == 1:
      print(Fore.BLUE+"="*50)
      print(Fore.GREEN+f"{self.name}"+Fore.WHITE+", you won! Congratulations! The number is "+Fore.GREEN+f"{self.number}.")
      print(Fore.WHITE+"Thanks for playing!")
      print(Fore.RED+"Press enter to continue")
      print(Fore.BLUE+"="*50)
    elif self.win == 0:
      print(Fore.BLUE+"="*50)
      print(Fore.GREEN+f"{self.name}"+Fore.WHITE+", your final guess was "+Fore.GREEN+f"{self.num}.")
      print(Fore.WHITE+"The correct number is "+Fore.GREEN+f"{self.number}.")
      print(Fore.WHITE+"Thanks for playing!")
      print(Fore.RED+"Press enter to continue")
      print(Fore.BLUE+"="*50)

def healthdata(df,bmi,bmicondition,heartrate,heartratecondition):

  print(Fore.BLUE+"="*70)
  print(Fore.WHITE+"Your current BMI condition is "+Fore.GREEN+f"{bmicondition}")
  a = df["BMICondition"].value_counts()[bmicondition]
  print(Fore.GREEN+f"{a} "+Fore.WHITE+"people have the same condition")
  print(Fore.BLUE+"="*70)
  input()
  replit.clear()

  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Your current BMI is "+Fore.GREEN+f"{bmi}")
  a = df["BMI"].mean()
  print(Fore.WHITE+"The average BMI is "+Fore.GREEN+f"{int(a)}")
  print(Fore.BLUE+"="*50)
  input()
  replit.clear()

  print(Fore.BLUE+"="*70)
  print(Fore.WHITE+"Your current heart rate condition is "+Fore.GREEN+f"{heartratecondition}")
  a = df["HeartRateCondition"].value_counts()[heartratecondition]
  print(Fore.GREEN+f"{a} "+Fore.WHITE+"people have the same condition")
  print(Fore.BLUE+"="*70)
  input()
  replit.clear()

  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Your current heart rate is "+Fore.GREEN+f"{heartrate}")
  a = df["HeartRate"].mean()
  print(Fore.WHITE+"The average heart rate is "+Fore.GREEN+f"{int(a)}")
  print(Fore.BLUE+"="*50)
  input()
  replit.clear()

def educationdata(df,school,schoollocation,hoursstudy):

  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Your current school is "+Fore.GREEN+f"{school}")
  print(Fore.WHITE+"Here are the list of students registered per school")
  print(df["School"].value_counts())
  print(Fore.BLUE+"="*50)
  input()
  replit.clear()

  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Your current school location is "+Fore.GREEN+f"{schoollocation}")
  print(Fore.WHITE+"Here is a list of different school locations")
  print(df["SchoolLocation"].value_counts())
  print(Fore.BLUE+"="*50)
  input()
  replit.clear()


  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Your current studying hours is "+Fore.GREEN+f"{hoursstudy}")
  a = df["HoursStudy"].mean()
  print(Fore.WHITE+"The average studying hours is "+Fore.GREEN+f"{int(a)}")
  print(Fore.BLUE+"="*50)
  input()
  replit.clear()

def commercedata(df,favshopping,hoursshopping,preferonline):

  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Your favourite shopping website is "+Fore.GREEN+f"{favshopping}")
  print(Fore.WHITE+"Here are the list of comparison among those 3")
  print(df["FavShopping"].value_counts())
  print(Fore.BLUE+"="*50)
  input()
  replit.clear()

  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"You take "+Fore.GREEN+f"{hoursshopping} "+Fore.WHITE+"hours to shop everyday")
  a = df["HoursShopping"].mean()
  print(Fore.WHITE+"The average shopping time is "+Fore.GREEN+f"{int(a)} "+Fore.WHITE+"hours")
  print(Fore.BLUE+"="*50)
  input()
  replit.clear()


  print(Fore.BLUE+"="*50)
  if preferonline == "Y":
    print(Fore.WHITE+"You prefer shopping online")
    a = df["PreferOnline"].value_counts()["Y"]
    print(Fore.GREEN+f"{a} "+Fore.WHITE+"people agree with you")
  elif preferonline == "N":
    print(Fore.WHITE+"You don't prefer shopping online")
    a = df["PreferOnline"].value_counts()["N"]
    print(Fore.GREEN+f"{a} "+Fore.WHITE+"people agree with you")
  print(Fore.BLUE+"="*50)
  input()
  replit.clear()  

def preferencedata(df,favgenre,favairline):
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Your favourite movie genre is "+Fore.GREEN+f"{favgenre}")
  print(Fore.WHITE+"Here is a list of comparison in amount")
  print(df["FavGenre"].value_counts())
  print(Fore.BLUE+"="*50)
  input()
  replit.clear()

  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"Your favourite airline is "+Fore.GREEN+f"{favairline}")
  print(Fore.WHITE+"Here is a list of comparison in amount")
  print(df["FavAirline"].value_counts())
  print(Fore.BLUE+"="*50)
  input()
  replit.clear()

def gamechoice():
  print(Fore.BLUE+"="*50)
  print(Fore.WHITE+"What game do you want to play?")
  print("1. Guess the number")
  print("2. Hangman")
  print("3. Tic Tac Toe")
  print(Fore.RED+"Choose 1-3")
  print(Fore.BLUE+"="*50)

class Hangman:
  wordlist1 = ["Animals",["G","I","R","A","F","F","E"],["P","A","N","D","A"],["R","A","B","B","I","T"],["C","H","A","M","E","L","I","O","N"]]
  wordlist2 = ["Cities",["C","A","L","I","F","O","R","N","I","A"],["H","A","N","E","D","A"],["S","U","L","A","W","E","S","I"],["L","O","N","D","O","N"]]
  wordlist3 = ["Food",["B","R","E","A","D"],["N","O","O","D","L","E","S"],["P","I","Z","Z","A"],["B","A","G","U","E","T","T","E"]]
  guessed = []
  printstring = ""
  wordlist = []
  genre = ""
  correctword = ""
  usedletters = ""
  lives = 10
  
  def __init__(self,name):
    self.name = name

  def homepage(self):
    print(Fore.BLUE+"="*50)
    print(Fore.WHITE+"Welcome, "+Fore.GREEN+f"{self.name}"+Fore.WHITE+", to the hangman game!")
    print("Words and genres will be randomized")
    print()
    print(Fore.RED+"Press enter to continue")
    print(Fore.BLUE+"="*50)
    input()
    replit.clear()

  
  def validity(self):
    for i in range(len(self.wordlist)):
      self.correctword += self.wordlist[i]

  def gamestart(self):
    a = random.randint(1,3)
    b = random.randint(1,4)
    c = ""
    if a == 1:
      c = self.wordlist1[b]
      self.genre = self.wordlist1[0]
    elif a == 2:
      c = self.wordlist2[b]
      self.genre = self.wordlist2[0]
    elif a == 3:
      c = self.wordlist3[b]
      self.genre = self.wordlist3[0]
    self.wordlist = c
    for i in range(len(self.wordlist)):
      self.guessed.append("_")

  def game(self):
    wincondition = []
    for i in range(len(self.guessed)):
      wincondition.append("_")
    while self.lives > 0:
      if self.wordlist != wincondition:
        print(Fore.BLUE+"="*50)
        print(Fore.WHITE+"Genre: "+self.genre)
        print("LIVES LEFT:"+str(self.lives))
        self.concatguessed()
        print("Used letters"+self.usedletters)
        print(Fore.BLUE+"="*50)
        a = input().upper()
        replit.clear()
        if a in self.wordlist:
          count = self.wordlist.count(a)
          for i in range(count):
            index = self.wordlist.index(a)
            self.guessed[index] = self.wordlist[index]
            self.wordlist[index] = "_"
        else:
          self.lives -= 1
          self.usedletters += f" {a}"
      else:
        break
  
  def loading(self):
    for i in range(3):
      print(Fore.BLUE+"="*50)
      print(Fore.WHITE+"Calculating"+"."*i)
      print(Fore.BLUE+"="*50)
      time.sleep(1)
      replit.clear()

  
  def concatguessed(self):
    self.printstring = ""
    for i in range (len(self.guessed)):
      self.printstring += (self.guessed[i]+" ")
    print(self.printstring)

  def finalresult(self):
    replit.clear()
    if self.lives == 0:
      print(Fore.BLUE+"="*50)
      print(Fore.WHITE+"The correct word is "+self.correctword)
      print(Fore.RED+"Press enter to continue")
      print(Fore.BLUE+"="*50)
      input()
      replit.clear()
    elif self.lives != 0:
      print(Fore.BLUE+"="*50)
      print(Fore.WHITE+"You won!")
      print(Fore.RED+"Press enter to continue")
      print(Fore.BLUE+"="*50)
      input()
      replit.clear()

class Tictactoe:
  gridlay = [["1","2","3"],["4","5","6"],["7","8","9"]]
  numlay = [["1","2","3"],["4","5","6"],["7","8","9"]]
  wincondition = 0
  def __init__(self,name):
    self.name = name

  def computerload(self):
    for i in range(3):
      print(Fore.BLUE+"="*50)
      print(Fore.WHITE+"Computer selecting a move"+"."*i)
      print(Fore.BLUE+"="*50)
      time.sleep(1)
      replit.clear()

  def grid(self,gridlay):
    print(Fore.WHITE+"     |     |")
    print("  "+Fore.GREEN+gridlay[0][0]+Fore.WHITE+"  |  "+Fore.GREEN+gridlay[0][1]+Fore.WHITE+"  |  "+Fore.GREEN+gridlay[0][2])
    print(Fore.WHITE+'_____|_____|_____')
 
    print(Fore.WHITE+"     |     |")
    print("  "+Fore.GREEN+gridlay[1][0]+Fore.WHITE+"  |  "+Fore.GREEN+gridlay[1][1]+Fore.WHITE+"  |  "+Fore.GREEN+gridlay[1][2])
    print(Fore.WHITE+'_____|_____|_____')
 
    print(Fore.WHITE+"     |     |")
    print("  "+Fore.GREEN+gridlay[2][0]+Fore.WHITE+"  |  "+Fore.GREEN+gridlay[2][1]+Fore.WHITE+"  |  "+Fore.GREEN+gridlay[2][2])
    print(Fore.WHITE+"     |     |")
  def order(self):
    print(Fore.BLUE+"="*50)
    print(Fore.RED+"Do you want to go first? (Y/N)")
    print(Fore.BLUE+"="*50)
    a = input()
    replit.clear()
    if a == "N":
      self.computerselects()
      self.computerload()
  def printlay(self):
    self.grid(self.gridlay)
    print(Fore.RED+"Choose the available numbers")
  def printnum(self):
    print(Fore.BLUE+"="*50)
    print(Fore.WHITE+"RULES!")
    print("THE LAYOUT WILL BE LIKE THIS")
    self.grid(self.numlay)
    print(Fore.RED+"Press enter if you understand")
    print(Fore.BLUE+"="*50)
    input()
    replit.clear()
  def computerselects(self):
    filled = 0
    while filled == 0:
      a = random.randint(0,2)
      b = random.randint(0,2)
      if self.gridlay[a][b] != "X" and self.gridlay[a][b] != "O":
        self.gridlay[a][b] = "X"
        filled = 1
        replit.clear()
  def userselects(self):
    print(Fore.BLUE+"="*50)
    self.printlay()
    print(Fore.BLUE+"="*50)
    filled = 0
    a = int(input())
    while filled == 0:
      replit.clear()
      if a <= 3 and a > 0:
        b = a-1
        a = 0
        if self.gridlay[a][b] != "X" and self.gridlay[a][b] != "O":
          self.gridlay[a][b] = "O"
          filled = 1
          replit.clear()
        else:
          replit.clear()
          print(Fore.BLUE+"="*50)
          self.printlay()
          print(Fore.RED+"SELECT AN EMPTY SPOT!")
          print(Fore.BLUE+"="*50)
          a = int(input())
      elif a <= 6:
        b = a-4
        a = 1
        if self.gridlay[a][b] != "X" and self.gridlay[a][b] != "O":
          self.gridlay[a][b] = "O"
          filled = 1
          replit.clear()
        else:
          replit.clear()
          print(Fore.BLUE+"="*50)
          self.printlay()
          print(Fore.RED+"SELECT AN EMPTY SPOT!")
          print(Fore.BLUE+"="*50)
          a = int(input())
      elif a <= 9:
        b = a-7
        a = 2
        if self.gridlay[a][b] != "X" and self.gridlay[a][b] != "O":
          self.gridlay[a][b] = "O"
          filled = 1
          replit.clear()
        else:
          replit.clear()
          print(Fore.BLUE+"="*50)
          self.printlay()
          print(Fore.RED+"SELECT AN EMPTY SPOT!")
          print(Fore.BLUE+"="*50)
          a = int(input())
      else:
        replit.clear()
        print(Fore.BLUE+"="*50)
        self.printlay()
        print(Fore.RED+"SELECT A VALID NUMBER!")
        print(Fore.BLUE+"="*50)
        a = int(input())
  
  def playeroneselects(self):
    print(Fore.BLUE+"="*50)
    self.printlay()
    print(Fore.WHITE+"PLAYER 1'S TURN")
    print(Fore.BLUE+"="*50)
    filled = 0
    a = int(input())
    while filled == 0:
      replit.clear()
      if a <= 3 and a > 0:
        b = a-1
        a = 0
        if self.gridlay[a][b] != "X" and self.gridlay[a][b] != "O":
          self.gridlay[a][b] = "O"
          filled = 1
          replit.clear()
        else:
          replit.clear()
          print(Fore.BLUE+"="*50)
          self.printlay()
          print(Fore.RED+"SELECT AN EMPTY SPOT!")
          print(Fore.BLUE+"="*50)
          a = int(input())
      elif a <= 6:
        b = a-4
        a = 1
        if self.gridlay[a][b] != "X" and self.gridlay[a][b] != "O":
          self.gridlay[a][b] = "O"
          filled = 1
          replit.clear()
        else:
          replit.clear()
          print(Fore.BLUE+"="*50)
          self.printlay()
          print(Fore.RED+"SELECT AN EMPTY SPOT!")
          print(Fore.BLUE+"="*50)
          a = int(input())
      elif a <= 9:
        b = a-7
        a = 2
        if self.gridlay[a][b] != "X" and self.gridlay[a][b] != "O":
          self.gridlay[a][b] = "O"
          filled = 1
          replit.clear()
        else:
          replit.clear()
          print(Fore.BLUE+"="*50)
          self.printlay()
          print(Fore.RED+"SELECT AN EMPTY SPOT!")
          print(Fore.BLUE+"="*50)
          a = int(input())
      else:
        replit.clear()
        print(Fore.BLUE+"="*50)
        self.printlay()
        print(Fore.RED+"SELECT A VALID NUMBER!")
        print(Fore.BLUE+"="*50)
        a = int(input())

  def playertwoselects(self):
    print(Fore.BLUE+"="*50)
    self.printlay()
    print(Fore.WHITE+"PLAYER 2'S TURN")
    print(Fore.BLUE+"="*50)
    filled = 0
    a = int(input())
    while filled == 0:
      replit.clear()
      if a <= 3 and a > 0:
        b = a-1
        a = 0
        if self.gridlay[a][b] != "X" and self.gridlay[a][b] != "O":
          self.gridlay[a][b] = "X"
          filled = 1
          replit.clear()
        else:
          replit.clear()
          print(Fore.BLUE+"="*50)
          self.printlay()
          print(Fore.RED+"SELECT AN EMPTY SPOT!")
          print(Fore.BLUE+"="*50)
          a = int(input())
      elif a <= 6:
        b = a-4
        a = 1
        if self.gridlay[a][b] != "X" and self.gridlay[a][b] != "O":
          self.gridlay[a][b] = "X"
          filled = 1
          replit.clear()
        else:
          replit.clear()
          print(Fore.BLUE+"="*50)
          self.printlay()
          print(Fore.RED+"SELECT AN EMPTY SPOT!")
          print(Fore.BLUE+"="*50)
          a = int(input())
      elif a <= 9:
        b = a-7
        a = 2
        if self.gridlay[a][b] != "X" and self.gridlay[a][b] != "O":
          self.gridlay[a][b] = "X"
          filled = 1
          replit.clear()
        else:
          replit.clear()
          print(Fore.BLUE+"="*50)
          self.printlay()
          print(Fore.RED+"SELECT AN EMPTY SPOT!")
          print(Fore.BLUE+"="*50)
          a = int(input())
      else:
        replit.clear()
        print(Fore.BLUE+"="*50)
        self.printlay()
        print(Fore.RED+"SELECT A VALID NUMBER!")
        print(Fore.BLUE+"="*50)
        a = int(input())      

  def homescreen(self):
    print(Fore.BLUE+"="*50)
    print(Fore.WHITE+"Welcome, "+Fore.GREEN+f"{self.name}"+Fore.WHITE+", to tic tac toe!")
    print(Fore.RED+"Please select 1 or 2")
    print(Fore.WHITE+"1. Vs A.I.")
    print("2. Multi Player")
    print(Fore.BLUE+"="*50)

  def validatewin(self):
    if self.gridlay[0][0] == self.gridlay[0][1] and self.gridlay[0][1] == self.gridlay[0][2]:
      self.wincondition = self.gridlay[0][0]
    elif self.gridlay[1][0] == self.gridlay[1][1] and self.gridlay[1][1] == self.gridlay[1][2]:
      self.wincondition = self.gridlay[1][0]
    elif self.gridlay[2][0] == self.gridlay[2][1] and self.gridlay[2][1] == self.gridlay[2][2]:
      self.wincondition = self.gridlay[2][0]
    elif self.gridlay[0][0] == self.gridlay[1][0] and self.gridlay[1][0] == self.gridlay[2][0]:
      self.wincondition = self.gridlay[0][0]
    elif self.gridlay[0][1] == self.gridlay[1][1] and self.gridlay[1][1] == self.gridlay[2][1]:
      self.wincondition = self.gridlay[0][1]
    elif self.gridlay[0][2] == self.gridlay[1][2] and self.gridlay[1][2] == self.gridlay[2][2]:
      self.wincondition = self.gridlay[0][2]
    elif self.gridlay[0][0] == self.gridlay[1][1] and self.gridlay[1][1] == self.gridlay[2][2]:
      self.wincondition = self.gridlay[0][0]
    elif self.gridlay[0][2] == self.gridlay[1][1] and self.gridlay[1][1] == self.gridlay[2][0]:
      self.wincondition = self.gridlay[0][2]

  def checkwin(self,x):
    if x == "O":
      print(Fore.BLUE+"="*50)
      print(Fore.WHITE+"You won! Thanks for playing!")
      print(Fore.RED+"Press enter to continue")
      print(Fore.BLUE+"="*50)
      input()
    elif x == "X":
      print(Fore.BLUE+"="*50)
      print(Fore.WHITE+"The A.I won! Thanks for playing!")
      print(Fore.RED+"Press enter to continue")
      print(Fore.BLUE+"="*50)
      input()
  
  def mcheckwin(self,x):
    if x == "O":
      print(Fore.BLUE+"="*50)
      print(Fore.WHITE+"Player 1 won! Thanks for playing!")
      print(Fore.RED+"Press enter to continue")
      print(Fore.BLUE+"="*50)
      input()
    elif x == "X":
      print(Fore.BLUE+"="*50)
      print(Fore.WHITE+"Player 2 won! Thanks for playing!")
      print(Fore.RED+"Press enter to continue")
      print(Fore.BLUE+"="*50)
      input()

  def gameloop(self):
    self.homescreen()
    a = int(input())
    if a == 1:
      replit.clear()
      self.printnum()
      self.order()
      while True:
        self.userselects()
        self.validatewin()
        if self.wincondition != 0:
          break
        self.computerselects()
        self.computerload()
        self.validatewin()
        if self.wincondition != 0:
          break
      self.checkwin(self.wincondition)
    elif a == 2:
      replit.clear()
      self.printnum()
      while True:
        self.playeroneselects()
        self.validatewin()
        if self.wincondition != 0:
          break
        self.playertwoselects()
        self.validatewin()
        if self.wincondition != 0:
          break
      self.mcheckwin(self.wincondition)
    replit.clear()

#MAINCODE
replit.clear()
df = pd.read_csv("codeolympiad.csv")
df["Gender"].replace({"M":"Male","F":"Female"},inplace=True)
replit.clear()
initdisplay("Press enter to register...")
loading(3)
personaldatacollection()
loading(3)
initdisplay("Registration success! Press enter to continue...")
loading(5)
while activeprogram == 1:
  replit.clear()
  choice = welcome(userinfo[0])
  loading(2)
  if choice == 2:
    user = Quiz(userinfo[0])
    user.loading()
    user.readystatement()
    user.setrules()
    user.qna()
    user.resultstatement()
    user.loading()
  elif choice == 3:
    gamechoice()
    a = int(input())
    replit.clear()
    if a == 1:
      user = GuessNumber(userinfo[0])
      user.initloading()
      user.cycle()
      user.endloading()
      user.results()
    elif a == 2:
      user = Hangman(userinfo[0])
      user.homepage()
      user.gamestart()
      user.validity()
      user.loading()
      user.game()
      user.loading()
      user.finalresult()
    elif a == 3:
      user = Tictactoe(userinfo[0])
      user.gameloop()
  elif choice == 4:
    activeprogram = 0
  elif choice == 1:
    b = 1
    while b == 1:
      replit.clear()
      user = Personal(userinfo)
      user.generalstatement()
      a = int(input())
      if a == 2:
        replit.clear()
        user.healthcalc()
        user.healthstatement()
        input()
        replit.clear()
        healthdata(df,user.state[0],user.state[1],user.heartrate,user.state[2])
      elif a == 3:
        replit.clear()
        user.educationstatement()
        input()
        replit.clear()
        educationdata(df,user.school,user.location,user.hoursstudy)
      elif a == 4:
        replit.clear()
        user.commercestatement()
        input()
        replit.clear()
        commercedata(df,user.favshopping,user.hoursshopping,user.preferonline)
      elif a == 5:
        replit.clear()
        user.preferencestatement()
        input()
        replit.clear()
        preferencedata(df,user.favgenre,user.favairline)
      elif a == 1:
        replit.clear()
        datadisplay(0,5,0,6)
        input()
        datadisplay(5,10,0,6)
        input()
        datadisplay(10,15,0,6)
        input()
        datadisplay(15,20,0,6)
        input()
        datadisplay(20,25,0,6)
        input()
        datadisplay(25,30,0,6)
        input()
        datadisplay(30,35,0,6)
        input()
        datadisplay(35,40,0,6)
        input()
        datadisplay(40,45,0,6)
        input()
        datadisplay(45,48,0,6)
        input()   
      elif a == 6:
        b = 0 


