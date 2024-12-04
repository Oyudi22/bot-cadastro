#-*- coding:utf-8 -*-
import pyautogui
from time import sleep

with open('nome.txt', 'r', encoding="UTF-8") as file:
    for linha in file:
        nome = linha.split(',')[0]
        nome2 = linha.split(',')[1]
        sobrenome = linha.split(',')[2]
        cpf = linha.split(',')[3]
        senha = 12345678

        pyautogui.click(2298,289,duration=2)
        pyautogui.click(2541,284,duration=2)
        #sleep(2)

        sleep(5) #Escreve o nome
        pyautogui.click(2541,284,duration=5)
        pyautogui.typewrite(nome)
        
        #Sobrenome
        pyautogui.click(2933,284,duration=3) 
        pyautogui.typewrite(f"{nome2} {sobrenome}")
        
        #Digita o e-mail
        pyautogui.click(2432,351,duration=3) 
        pyautogui.hotkey('ctrl','a')
        pyautogui.press('backspace')
        pyautogui.write(f"{nome.lower()}{sobrenome.lower()}")
        pyautogui.write(f".e{cpf}")
        
        #Seleciona o estágio
        pyautogui.click(2569,529,duration=2)
        pyautogui.click(2851,537,duration=2)
        pyautogui.click(2722,618,duration=2)
        pyautogui.click(2819,641,duration=2)
        pyautogui.click(3061,963,duration=2)

        #Escreve a senha
        pyautogui.click(2398,814,duration=2)
        pyautogui.click(2482,866,duration=2)
        pyautogui.write(f"{senha}")
        pyautogui.click(2670,865,duration=2)

        #Cadastra
        pyautogui.click(3224,1012,duration=1)

        sleep(5)

        #Seleciona o e-mail
        pyautogui.click(2801,341,duration=2)
        
        pyautogui.doubleClick(2801,341,duration=2)
        pyautogui.hotkey('shift', 'end')
        sleep(2)

        #Copia e cola
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(109,342,duration=1) #Alterar sempre
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'v')

        #Dá enter e recomeça
        pyautogui.click(3192,719,duration=1)
        pyautogui.click(2049,121,duration=1)
        sleep(4)