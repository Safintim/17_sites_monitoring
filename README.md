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

OFF Ошибка https://devma1n.org/1
ON  Проплачено https://vk.com/
ON  Проплачено https://stackoverflow.com/
ON  Проплачено https://github.com/
ON  Проплачено https://medium.com/

```

## Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
