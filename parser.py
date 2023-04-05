from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
def parse():
    url = 'https://omgtu.ru/general_information/faculties/' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    block = soup.findAll('div', class_='main__content') # находим контейнер с нужным классом
    description = ''# ВАЖНО:description строковая переменная для хранения названий факультетов
    for data in block: # проходим циклом по содержимому контейнера
        description = data.find("ul").text.strip() # Находим тег <ul> в текущем блоке и извлекаем название факультета
        description = '\n'.join(filter(None, description.split("\n")))# Удаляем пустые строки в тексте и объединяем все строки в одну с помощью символа переноса строки
    with open("res.txt", "w") as file:# Открываем файл "res.txt" в режиме записи и записываем в него полученный текст
        file.write(description)