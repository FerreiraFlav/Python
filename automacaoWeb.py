
#https://www.youtube.com/watch?v=ydV-gfqR4Uo


from selenium import webdriver # Selenium vai importar o webdriver que sera responsavel por criar o navegador.
from selenium.webdriver.chrome.service import Service # aqui esta sendo importado os serviços do webdriver
from webdriver_manager.chrome import ChromeDriverManager # aqui esta sendo importado os driver do Google Chrome
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

#abaixo esta sendo criado o navegador e importando os serviços do Google Chrome
service = Service(ChromeDriverManager().install())# fazendo instalação do ChromeDriver na variavel service
nav = webdriver.Chrome(service=service)#criando o navegador no Chrome, se fosse outro navegador utilizar outros comandos.

nav.get("https://web.whatsapp.com")# minha variavel navegador esta abrindo no Chrome o site do whatsapp web
time.sleep(60)
#nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()#é um cod que esta por traz de todos os elementos dos sites

mensagem = "Eu estive aqui outras vez, mas só quis avisar agora, have a nice day" # mensagem a ser exibida pros contatos
#abaixo vou criar uma lista de contatos, podendo ser numero isolados ou ate mesmo grupos no whatsapp
lista_contatos = ["Backup Flávio", "Franklin", "Mae Zap", "Flavio Br", "Foto family", "Condomínio"]

#print(len(lista_contatos))# usando o comando "len" eu conto os itens da variavel que eu quero, no caso a lista de contatos
#nav.implicitly_wait(10)

nav.find_element('XPath', '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()#é um cod que esta por traz de todos os elementos dos sites
time.sleep(99999999)
nav.quit()

#nav.implicitly_wait(10)# trecho de codigo necessario para navegador não fechar
#import time# trecho de codigo necessario para navegador não fechar
#time.sleep(9999999)# trecho de codigo necessario para navegador não fechar
#nav.quit()# trecho de codigo necessario para navegador não fechar