import pyautogui # type: ignore
import time

pyautogui.PAUSE = 0.3
pyautogui.press("win")  
pyautogui.write("FireFox")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)


pyautogui.click(x=725, y=374)
pyautogui.write("loginempressa@login.net")
pyautogui.press("tab")
pyautogui.write("@a031a")
pyautogui.press("enter")

time.sleep(1.5)

import pandas as pd

tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = str(tabela.loc[linha, "categoria"])
    preço = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    
    pyautogui.click(x=696, y=248)
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(marca)
    pyautogui.press("tab")
    pyautogui.write(tipo)
    pyautogui.press("tab")
    pyautogui.write(categoria)
    pyautogui.press("tab")
    pyautogui.write(str(preço))
    pyautogui.press("tab")
    pyautogui.write(str(custo))  
    pyautogui.press("tab")


    obs = str(tabela.loc[linha, "obs"])
    if obs !="nan":
        pyautogui.write(obs)    


    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("home")
