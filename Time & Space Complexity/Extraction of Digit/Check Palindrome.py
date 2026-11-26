

#This programe is check palindrome..for string...
def Check_palindrome(Word):
  
  new_word = Word[::-1]



  if new_word == Word:
        print("Yes , this word is palindrome.")
  else:
        print("Nope, this word isn't palindrome.")

input_word = input("Enter your word :")

Check_palindrome(input_word)


#for digit..

def Check_palinrome(no):

    n = no
    reverse_digit = 0

    while n > 0 :
 
        last_digit = n % 10
        reverse_digit = reverse_digit * 10 + last_digit
        n = n//10
    if no == reverse_digit:
        print("yes, this is palindrome.")
    else:
        print("Nope, is not palindrome")


no = int(input("Enter your Digit :"))
Check_palinrome(no)