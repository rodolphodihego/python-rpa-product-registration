# bibliotecas
import pyautogui# biblioteca para automação de mouse e teclado
# pyautogui.click clica com o mouse
# pyautogui.write escreve com o teclado
# pyautogui.press aperta uma tecla do teclado
# pyautogui.hotkey aperta uma combinação de teclas do teclado
import time # biblioteca para trabalhar com tempo
import pandas # biblioteca para trabalhar com tabelas e arquivos excel/csv

pyautogui.PAUSE = 0,3 # tempo de espera entre cada ação do pyautogui
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # link do site da empresa


# passo a passo do seu programa
# 01 : entrar no sistema da empresa 
#abrindo o navegador e acessando o site
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
#pyautogui.hotkey("command", "space") # mac 


# fazer uma pausa para o site carregar
time.sleep(1) # esperando 3 segundos

# 02 : fazer login no sistema
pyautogui.click(x=980, y=466) # clicar no campo de email
pyautogui.write("rodolphope2019@gmail.com") # escrever o email
pyautogui.press("tab") # apertar a tecla tab
pyautogui.write("Rodolpho2019") # escrever a senha
pyautogui.press("enter") # apertar a tecla enter
pyautogui.sleep(3)


# 03 : acessar o banco de dados

tabela = pandas.read_csv("Produtos.csv") # lendo a tabela de produtos

for linha in tabela.index: # para cada linha na tabela
    
    # 04 : cadastrar 1  
    pyautogui.click(x=1117, y=320)
    codigo = tabela.loc[linha, "codigo"] # pegar o código do produto na tabela
    pyautogui.write(str(codigo)) # escrever o código do produto
    pyautogui.press("tab")
    # Marcar novo produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo de produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    # preço
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    # observações
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    
    pyautogui.press("enter") # salvar
    #voltar para o início da linha
    pyautogui.scroll(5000)


# 05 : repetir o passo 04 ate acabar os produtos



