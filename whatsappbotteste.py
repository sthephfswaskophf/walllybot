#williammarques
#https://github.com/swaskophf

#bibliotecas necessarias, caso nao tenha instalada em sua maquina basta executar os comandos (pip instal....)
from selenium import webdriver  #pip install selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager
import time

#Abre o Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') #abre o site Whatsapp Web
time.sleep(10) #da um sleep de 15 segundos, tempo para scannear o QRCODE

#Contatos/Grupos - Informar o nome(s) de Grupos ou Contatos que serao enviadas as mensagens
contatos = [
'contato 1', 'contato 2'
]

#Mensagem - Mensagem que sera enviada
mensagem = 'Tem boa notícia chegando no seu WhatsApp. Estamos iniciando a semana da regularização de dívidas! E aí, que tal ver o que podemos fazer por você? Confira as condições especiais de pagamento. '
mensagem2 = 'Responda essa mensagem e vamos conversar! Luana Muller - *Rama Advogados Associados*, representante do Canal Judicial do Banco Santander - *4007.2279*'


def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(1)
    campo_pesquisa.clear()
   
#Funcao que envia a mensagem
def enviar_mensagem(mensagem,mensagem2):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(2)
    campo_mensagem[1].send_keys(str(mensagem) + str(mensagem2))
    campo_mensagem[1].send_keys(Keys.ENTER)


#Percorre todos os contatos/Grupos e envia as mensagens
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem,mensagem2) 
    time.sleep(2)
