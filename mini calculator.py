BL = '\033[30m'
B = '\033[94m'
C = '\033[96m'
D = '\033[36m'
G = '\033[92m'
P = '\033[95m'
R = '\033[91m'
Y= '\033[93m'
logo = f"""
{ P}
╔═╗╔═╗─────╔═══╗──╔╗──────╔╗───╔╗
║║╚╝║║─────║╔═╗║──║║──────║║──╔╝╚╗
║╔╗╔╗╠╦═╗╔╗║║─╚╬══╣║╔══╦╗╔╣║╔═╩╗╔╬══╦═╗
║║║║║╠╣╔╗╬╣║║─╔╣╔╗║║║╔═╣║║║║║╔╗║║║╔╗║╔╝
║║║║║║║║║║║║╚═╝║╔╗║╚╣╚═╣╚╝║╚╣╔╗║╚╣╚╝║║
╚╝╚╝╚╩╩╝╚╩╝╚═══╩╝╚╩═╩══╩══╩═╩╝╚╩═╩══╩╝
{R} MADE BY MAAHI 
"""
print (logo)
a=B+"Your answer is :"

first = input (G+" enter first number : ") 
operator = input (G+"enter operator (+,-,*,/,%) :")
second = input ( G+"enter second number :")
first = int(first)
second =int(second)
if operator == "+":
    print(a+str(first+second))
elif  operator == "-":
     print(a+str(first-second))   
elif operator == "*":
     print(a+str(first*second) ) 
elif operator == "/":
     print(a+str(first/second))
elif operator == "%":
     print(a+str(first%second))  
else:
    print( "invalid operation")  
      
