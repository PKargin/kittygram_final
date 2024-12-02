Kittygram

Kittygram — это веб-приложение для публикаций домашних питомцев (Котиков :3), тут Вы можете поделиться своим любимцем/любимицей и их достижениями!

Стек технологий
Django PostgreSQL React Nginx Docker GitHub Actions

Проект включает следующие компоненты:

- Backend: Разработан на Django и использует PostgreSQL для хранения данных.

- Frontend: SPA-приложение на React, предоставляет пользовательский интерфейс.

- Gateway: Nginx используется для проксирования запросов между клиентом и сервером.

- Docker: Используется для контейнеризации всех компонентов приложения.

1. Установка и настройка

Клонируйте репозиторий:

git clone <URL-репозитория>
cd <папка-репозитория>

Настройте переменные окружения: Создайте файл .env в корневой директории проекта и добавьте настройки для PostgreSQL:

- DB_NAME=kittygram_db
- DB_USER=kittygram_user
- DB_PASSWORD=your_password
- DB_HOST=db
- DB_PORT=5432

2. Запустите Docker Compose:

- docker-compose up --build

Это запустит все контейнеры (backend, frontend, db, и gateway) и поднимет приложение.

3. Автоматизация и развертывание

Проект настроен для автоматического тестирования и развертывания с помощью GitHub Actions:

- Проверка кода на соответствие PEP8.
- Запуск тестов для фронтенда и бэкенда.
- Сборка Docker образов и отправка их на Docker Hub.
- Обновление образов на сервере и перезапуск приложения.
- Сборка статики и выполнение миграций.
- Уведомления о завершении деплоя в Telegram.

4. Работа с проектом

Запуск тестов:

docker-compose exec backend pytest
docker-compose exec frontend npm test

Переход к интерфейсу приложения: После запуска контейнеров, приложение доступно по https://kittygram-nophp.zapto.org

5. Обновление статики:

docker-compose exec backend python manage.py collectstatic

Миграции:

docker-compose exec backend python manage.py migrate
