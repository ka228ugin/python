from scapy.all import *
import hashlib
import time
import json

# Функция для отправки пакета с данными
def send_packet():
    secret = "Hack"

    data = {
        "Name": "Ivan",
        "Surname": "Ivanov",
        "Patronymic": "Ivanovich",
        "Pasport Series": "7623",
        "Pasport Number": "228335",
        "IdAssistnet": "927",
        "HashValue": hashlib.md5(secret.encode()).hexdigest()
    }

    # Преобразуем словарь в JSON строку
    data_str = json.dumps(data)

    #print(data_str)

    # Формируем пакет с данными и отправляем на адрес 10.10.3.1
    packet = IP(dst="10.10.3.1")/UDP()/Raw(load=f"Informations: {data_str}".encode())
    send(packet, verbose=False)

# Отправляем пакет каждые 5 секунд
while True:
    send_packet()
    print('packet send')
    time.sleep(5)
