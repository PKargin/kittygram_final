<!DOCTYPE html>
<h1>Проект Киттиграм - это социальная сеть для любителей котиков!</h1>
<br>

<h4><b>Kittygram</b> — это веб-приложение для публикаций домашних питомцев (Котиков :3), тут Вы можете поделиться своим любимцем/любимицей и их достижениями!</h4>
<br>

<h4><b>Стек технологий:</b></h4>

- Django<br> 
- PostgreSQL<br> 
- React<br> 
- Nginx<br> 
- Docker<br> 
- GitHub<br> 
- Actions<br>

<h4><b>Проект включает следующие компоненты:</b></h4>

- Backend: Разработан на Django и использует PostgreSQL для хранения данных;<br>
- Frontend: SPA-приложение на React, предоставляет пользовательский интерфейс;<br>
- Gateway: Nginx используется для проксирования запросов между клиентом и сервером;<br>
- Docker: Используется для контейнеризации всех компонентов приложения.<br>

<h4>1. Установка и настройка</h4>

Клонируйте репозиторий:

git clone https://github.com/Chiken-Kitchen/kittygram_final<br>
<br>
cd kittygram_final<br>
<br>
Настройте переменные окружения: Создайте файл .env в корневой директории проекта и добавьте настройки для PostgreSQL:<br>
<br>
- DB_NAME = kittygram_db<br>
- DB_USER = kittygram_user<br>
- DB_PASSWORD = your_password<br>
- DB_HOST = 127.0.0.1<br>
- DB_PORT = 5432<br>

<h4>2. Запустите Docker Compose:</h4>

- docker-compose up --build<br>
<br>
Это запустит все контейнеры (backend, frontend, db, и gateway) и поднимет приложение.

<h4>3. Автоматизация и развертывание</h4>

Проект настроен для автоматического тестирования и развертывания с помощью GitHub Actions:<br>
<br>
- Проверка кода на соответствие PEP8;<br>
- Запуск тестов для фронтенда и бэкенда;<br>
- Сборка Docker образов и отправка их на Docker Hub;<br>
- Обновление образов на сервере и перезапуск приложения;<br>
- Сборка статики и выполнение миграций;<br>
- Уведомления о завершении деплоя в Telegram.<br>

<h4>4. Работа с проектом</h4>

Запуск тестов:<br>
<br>
docker-compose exec backend pytest<br>
docker-compose exec frontend npm test<br>
<br>
Переход к интерфейсу приложения: После запуска контейнеров, приложение доступно по ссылке <a href='https://kittygram-nophp.zapto.org'>Kittygram</a>

<h4>5. Обновление статики:</h4>

- docker-compose exec backend python manage.py collectstatic

<h4>Миграции:</h4>

- docker-compose exec backend python manage.py migrate
