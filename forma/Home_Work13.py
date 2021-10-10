#1 Подключитесь к API НБУ,получите текущий курс валют и запишите его в TXT файл в таком формате:
# "[дата создания запроса]"
# n. [название валюты n] to UAH:[значение курса к валюте n]

import requests

url = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
response = requests.get(url)
sum = f'{response.json()[0]["exchangedate"]}\n'
print(response.json())

number = 0
for item in response.json():
    number += 1
    sum += f'{number}.{item["cc"]} to UAH: {item["rate"]}\n'

with open("currency10.txt", "w") as file:
    file.write(sum)

#2 В вашем репозитории создайте отдельную ветку HW15 от ветки master, реализуйте дз в ней и выполните мержветки.