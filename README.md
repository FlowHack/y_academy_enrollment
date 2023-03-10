# Вступительное задание в Летнюю Школу Бэкенд Разработки Яндекса 2022

## ***Технологии**
```
Python 3.8.5
Django 4.0.5
Django REST Framework 3.13.1
Gunicorn 20.1.0
```

## ***Описание***
Выполненное вступительное задание в Летнюю школу Бэкенда Яндекс 2022

## ***Запуск***
Запустите Docker
```
docker-compose up
```
Скопируйте ID нужного контейнера
```
docker ps | grep "y_academy_enrollment_web" | cut -d' ' -f1
```
Войдите в него
```
docker exec -it e84264e7527b sh
```
Соберите статику
```
python manage.py collectstatic
```
Теперь можно отправлять запросы по адресу 
```
http://ваш-IP/
```
