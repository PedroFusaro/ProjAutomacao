import pyautogui
import time
import pandas as pd


pyautogui.PAUSE = 0.5 # pausa de 1 segundo entre cada ação

# passo 1: entrar no sistema da empresa 
site = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login' # site a ser aberto

pyautogui.press('win') # abrir nova aba
pyautogui.write('chrome') # escrever chrome
pyautogui.press('enter') # pressionar enter para abrir o navegador
pyautogui.write(site) # escrever o link
pyautogui.press('enter') # pressionar enter para abrir o site

time.sleep(2)# esperar 2 segundos para o site carregar

# passo 2: fazer o login
pyautogui.press('tab') # pressionar tab para ir para o campo de login
pyautogui.write('admin') # escrever o login
pyautogui.press('tab') # pressionar tab para ir para o campo de senha
pyautogui.write('admin') # escrever a senha
pyautogui.press('enter') # pressionar enter para fazer o login

time.sleep(2) # esperar 2 segundos para o sistema carregar


# passo 3: importar a base de dados
tabela = pd.read_csv('produtos.csv') # importar a base de dados


# passo 4: repitir para todos os produtos
for linha in tabela.index: # para cada linha da tabela
    codigo = tabela.loc[linha, 'codigo'] # pegar o código do produto
    marca = tabela.loc[linha, 'marca'] # pegar a marca do produto
    tipo = tabela.loc[linha, 'tipo'] # pegar o tipo do produto
    categoria = tabela.loc[linha, 'categoria'] # pegar a categoria do produto
    preco = tabela.loc[linha, 'preco_unitario'] # pegar o preço do produto
    custo = tabela.loc[linha, 'custo'] # pegar o custo do produto
    obs = tabela.loc[linha, 'obs'] # pegar a observação do produto

    pyautogui.click(x=2721, y=261) # pressionar tab para ir para o campo de código
    pyautogui.write(codigo) # escrever o código do produto
    pyautogui.press('tab') # pressionar tab para ir para o campo de tipo
    pyautogui.write(marca) # escrever o tipo do produto
    pyautogui.press('tab') # pressionar tab para ir para o campo de marca
    pyautogui.write(tipo) # escrever a marca do produto
    pyautogui.press('tab') # pressionar tab para ir para o campo de categoria
    pyautogui.write(str(categoria)) # escrever a categoria do produto
    pyautogui.press('tab') # pressionar tab para ir para o campo de preço
    pyautogui.write(str(preco)) # escrever o preço do produto
    pyautogui.press('tab') # pressionar tab para ir para o campo de custo
    pyautogui.write(str(custo)) # escrever o custo do produto
    pyautogui.press('tab') # pressionar tab para ir para o campo de observação
    if str(obs) != "nan":
        pyautogui.write(obs) # escrever a observação do produto
    pyautogui.press('enter') # pressionar enter para cadastrar o produto
    pyautogui.press('tab') # pressionar tab para ir para o campo de código
    pyautogui.press('home') # subir para o início da linha