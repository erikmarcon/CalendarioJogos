#Imports
from selenium import webdriver
import pandas as pd

#Estrutura de Partidas
partidas = pd.DataFrame(columns = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'All Day Event'])

#Carregar o navegador
driver = webdriver.Chrome('/usr/local/share/chromedriver')

#Acessar a página
driver.get('https://www.scoreboard.com/br/equipe/athletico-pr/UoAxb1Tq/calendario/')

#Buscar todos os IDs de partida
ids = driver.find_elements_by_xpath("//*[starts-with(@id,'g_')]")
matches_ids = []

#IDs de partida numa lista
for i in ids:
    matches_ids.append(i.get_attribute('id'))

#Para cada ID único montar a estrutura de partidas
for x in matches_ids:

    date_element = driver.find_elements_by_xpath('//*[@id="' + x +'"]/td[2]')[0]
    hometeam_element = driver.find_elements_by_xpath('//*[@id="' + x +'"]/td[3]/span')[0]
    awayteam_element = driver.find_elements_by_xpath('//*[@id="' + x +'"]/td[4]/span')[0]

    data = date_element.text
    time_casa = hometeam_element.text
    time_visitante = awayteam_element.text

    data_int = int(data[7:9])
    data_fim = data_int + 2
    data_fim = str(data_fim)

    partidas.loc[len(partidas)] = [time_casa+" vs "+time_visitante, data[0:2]+"/"+data[3:5]+"/2019", data[7:12], data[0:2]+"/"+data[3:5]+"/2019", data_fim+":00", False]

#print(partidas)

#Criar arquivo CSV
partidas.to_csv('/Users/erikmarcon/Documents/Python/Projeto Calendario Jogos/Calendario Athletico.csv')