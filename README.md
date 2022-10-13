# metashop
 
Тестовое задание для Meta Sharks:

есть два сценария запуска проекта, через 
1) docker с postgres
2) через virtual environment с sqlite3
---

Как запустить через Docker:

через Docker-compose: в папке infra выполнить комманду:

~ docker-compose up

проект соберется и запустится по адресу http://127.0.0.1

далее нужно сделать миграции для базы данных, выполняем комманду в другом терминале

~ docker exec -it infra_backend_1 python manage.py migrate

далее собираем статику для .css

~ docker exec -it infra_backend_1 python manage.py collectstatic

далее создаем админа для (настройки уведомлений через телеграм)

~ docker exec -it infra_backend_1 python manage.py createsuperuser

дальше нужно ввести данные админа, обычно для тестов это username: admin, password: admin

проект успешно запущен по адресу http://127.0.0.1

админка по адресу http://127.0.0.1/admin

---

как запустить через виртуальное окружение (linux, macos):
1) в корневой папке создать виртуальное окружение:

~ python3 -m venv venv

2) активировать его:

~ source venv/bin/activate

3) установить библиотеки:

~ pip install -r requirements.txt

4) запустить проект:

~ python manage.py runserver 0.0.0.0:8000

готово:
на локальном сайте http://127.0.0.1:8000/ проект запущен успешно

при проблемах с запуском написать в телеграм @oruchkin

---

Весь проект это API вымышленного магазина, документация к API лежит в excel файле

"MetaShop_documentation.xlsx"

так же для удобства она залита в онлайн:

https://docs.google.com/spreadsheets/d/1Z6O848xlZhOt70wczVjJXTntl4Z5aEl0s5rK7ppsuYU/

---
