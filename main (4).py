import time
import os 
def welcome():
  print("""
  Welcome to the "Currency Coverter":
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣄⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠔⠚⠉⠀⠀⠈⠙⢦⣄⠀⠀⠀
  ⠀⠀⠀⠀⢀⣠⠴⢒⡽⢃⣛⣍⣉⡐⢠⠀⠀⠀⠀⠈⣻⣢⡀
  ⡠⣴⠖⠋⠁⠀⠀⠨⡑⠚⠓⡖⡀⠘⡠⢁⣀⠤⣒⡩⢕⡪⡇
  ⣿⡿⣢⣀⠀⠀⠀⠀⠈⠁⢒⣒⠦⢛⡊⢅⡂⢍⡒⠭⡒⠭⡇
  ⡿⣿⣿⣷⣧⣢⢤⡤⢖⡊⠥⡒⠬⡒⠬⣐⠬⣑⢨⡱⠎⠃⠁
  ⠻⣿⣿⣿⣿⣿⣗⠨⣑⠪⣑⠪⣕⣪⡱⠶⠓⠉⠀⠀⠀⠀⠀
  ⠀⠀⠙⠻⢿⣿⡇⢍⣲⡭⠶⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠙⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
  ________________________________________________________________________________________________⠀⠀⠀⠀⠀
  ⠀""")
  for i in money:
    print(f"{i} : {money[i]}")

money={
  "USD":1.0 ,
  "EUR":0.92 ,
  "SHK":3.77 ,
  'RON':4.59 ,
  'EGP':48.32 ,
  'YRY':33.01 ,
  'CNY':7.26 ,
  'GBP':0.78 ,
  'THB':35.95 ,
  'JOD':0.71 ,
  'SAR':3.75 ,
 }
def currency():
 
 welcome()
 
 convert_from=input("Choose a currency to convert from: ").upper()
 while True:
   amount_the_convert=float(input("Enter the amount: "))
   choice_3=input(f"\nYou enttered {amount_the_convert} {convert_from}. Confirm? (Y/N): ")
   if choice_3.lower()=="n":
     continue
   else:
    break
    
 convert_to=input("Choose a currency to convert to: ").upper()
 print("Analyzing your request...please wait.")
 time.sleep(2) 
 print(f"Checking for {convert_to}'s best rates available....please wait")
 time.sleep(2) 
 print(f"Getting a discount price for {convert_from}.....please wait")
 time.sleep(2)
 if convert_from not in money or convert_to not in money:
  print("Invalid currency . Conversion canceled.")
  time.sleep(2)
  os.system("clear")
  currency()
 time.sleep(2)
 os.system("clear")
 print(f"Preparing the deal from {convert_from} to {convert_to}....please wait\n")
 time.sleep(2)
 sum = money[convert_to]/money[convert_from]
 print(f"Exhange Rate: 1 {convert_from} = {round(sum,2)} {convert_to}")
 print(f"{amount_the_convert} {convert_from} is equal to {round (amount_the_convert * sum,2)} {convert_to}")
 choice_1 = input("Do you accept this transaction? (Y/N): ")
 if choice_1.lower()=="n":
     print ("Transaction Canceled.\n")
     choice_2=input("Do you want to perform another conversion? (Y/N)): ")
     if choice_2.upper()=="Y": 
      os.system("clear")
      currency()
     else:
      print("Good Luck.")
    
 else:
    print("Good Luck.")
currency()