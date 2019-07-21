# Мониторинг сайтов

## Описание

Скрипт проверяет состояние сайта. Ответ 200 и доменное имя проплачено как минимум на 1 месяц вперед

## Требования

*Python3*

## Как запустить

Склонировать репозиторий и установить зависимости из requirements.txt:

```sh
git clone https://github.com/Safintim/17_sites_monitoring.git
cd 17_sites_monitoring
pip install -r requirements.txt
```
Запустить скрипт

```sh
python check_sites_health.py <path_to_file>
```

## Примеры запуска скрипта

```sh
python seek_dev_nighters.py urls.txt

ОШИБКА https://devma1n.org/1
HTTPSConnectionPool(host='devma1n.org', port=443): Max retries exceeded with url: /1 (Caused by NewConnectionError('<urllib3.co
nnection.VerifiedHTTPSConnection object at 0x7fbbf4701e10>: Failed to establish a new connection: [Errno -2] Name or service no
t known',))
ON  Проплачено https://vk.com/
ON  Проплачено https://stackoverflow.com/
ON  Проплачено https://github.com/
ON  Проплачено https://medium.com/

```

## Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
