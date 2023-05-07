import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'bankproject', password = 'Micro$oftIsCool')
cursor = connection.cursor()
program = True
def numCheck(num):
  num_is_int = False
  #Try the input as a number
  try:
    int(num)
    #If the input is a number put num_is_int as True
    num_is_int = True
  except ValueError:
    print("\nTry again using a whole number ")
    # If the input isn't a number put num_is_int as False
    num_is_int = False
  # Return num_is_int
  return num_is_int
print('Hello, welcome to Express H&M Bank of Austin ')


def createAccount():
  userFirstInput = input("Please enter your first name ")
  userLastInput = input("Please enter your last name ")
  user = userFirstInput + " " + userLastInput
  passMatch = False

    # Print pins rules
  print(f"\nHello {user}, insert a pin that is at least 4 digits long: \n")
    # while the pins don't match
  while not passMatch:
        # ask for a pin
    userInputPin = input("\nPin: ")
        # If pin is less than 4 don't accept pin
    if numCheck(userInputPin):
      if len(userInputPin) >= 4:
              # Ask user to confirm the pin
        userPinConfirm = input("Confirm pin: ")

              # Check if the pins are same
        if userInputPin == userPinConfirm:
          print("Pins match.")
                  # Make passMatch into true to make the while statement end
          passMatch = True
        else:
          print("Pins do not match. \nTry Again")
          passMatch = False
    else:
      print("Pin is too short try again ")
      passMatch = False
  userPin = userInputPin

createAccount()

amount = 0
while program == True:

    

  print(' 1.Deposit\n 2.Withdraw\n 3.modify account\n 4.Check Balance\n 5.Delete Account\n 6.Exit')
  options = input("Type a number corresponding to the use (1-6) ")
  if '1' in options:
    addedMoney = input("How much would you like to deposit ")
    newAmount = int(amount) + int(addedMoney)
    amount = newAmount
    print(f"You deposited {addedMoney}, and your new total is {newAmount}")
  elif '2' in options:
    moneyTaken = input("How much would you like to withdraw ")
    newAmount = int(amount) - int(moneyTaken)
    amount = newAmount
    print(f"You withdrew {moneyTaken}, and your new total is {newAmount}")
  elif '3' in options:
    createAccount()
  elif '4' in options:
    print(amount)
  elif '5' in options:
    delete = input("Are you sure? You will not be able to get this account back ")
    if delete == 'yes':
      print('Alright, it is your choice T-T ')
      exit()
    else :
      print("Glad you decided to stay with us! ")
  elif '6' in options:
    exit()
  else:
    print('Sorry, I am not able to comprehend that, please try again ')

def addAccount( userPin, userFirstInput, userLastInput, amount):
    addData = (f"INSERT INTO `bank`.`bank_info` (`Account_Pin`, `First_Name`, `Last_Name`, `balance`) VALUES ({userPin}, '{userFirstInput}', '{userLastInput}', '{amount}', '0)")
    cursor.execute(addData)
    connection.commit()
cursor.close()

connection.close()
