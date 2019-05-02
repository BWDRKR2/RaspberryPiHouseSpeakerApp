
import re 


user_input = input("Enter a password : ")
is_valid = True

if (len(user_input)<6 or len(user_input)>12):
	is_valid = False

elif not re.search("[A-Z]",user_input):
		is_valid = False

elif not re.search("[a-z]",user_input):
		is_valid = False

elif not re.search("[1-9]",user_input):
		is_valid = False

elif not re.search("[~!@#$%^&*]",user_input):
		is_valid = False

elif re.search("[\s]",user_input):
		is_valid = False
    


if(is_valid):
  	error = "Password is valid"
else:
	error = "Password lenght must be 6 to 12 charcaters, Must contain a upper case character, Must contain a lower case character, Must cointain a number, Must coantain a special character [~!@#$%^&*], Must not contaion a blank "
 	

