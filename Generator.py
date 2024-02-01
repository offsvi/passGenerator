# import secrets
# import string

# intens = (string.ascii_letters + string.digits)

# senha = [secrets.choice(intens)
#          for i in range(15)]
# senha = ''.join(senha)
# print(senha) 

# Pressionar botão windows
# Ecrver Bloco de notas 
# Pressionar Enter

import pyautogui
import time 
#import secrets
#import string

pyautogui.press("win")
time.sleep()
pyautogui.write("Bloco de notas")
time.sleep(2)
pyautogui.press("enter")

