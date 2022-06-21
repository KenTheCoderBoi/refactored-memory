from cryptography.fernet import Fernet
  
key = Fernet.generate_key()
fernet = Fernet(key)
option = int(input('''What speed do you want to test:  
  
1) Encrypt
  
2) Decrypt
  
Your Choice: '''))
  
  
if option == 1:  
    message = input('''Type message:  ''')
    encMessage = fernet.encrypt(message.encode())
    print("encrypted string: ", encMessage)
elif option == 2:
    encMessage = input('''Type message:  ''')
    decMessage = fernet.decrypt(encMessage).decode()
    print(decMessage)
    