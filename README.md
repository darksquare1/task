
## About
Это веб-приложение для управления информацией об автомобилях.
Вы можете просматривать все автомобили, узнать информацию о конкретном, комментировать, удалять, редактировать, регистрироваться и авторизироваться. Кроме того, доступно api ко всему вышеперечисленному функционалу.
## Build

To build this project run

```bash
$ git clone https://github.com/darksquare1/task
$ cd task
$ python -m venv ./.venv
$ .venv/Scripts/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```



Документация для апи находится по адресу http://127.0.0.1:8000/api/schema/redoc/
