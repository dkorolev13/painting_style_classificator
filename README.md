# @PaintingStyleClassificatorBot

Telegram бот, который определяет художественный стиль, в котором написана картина.
Основан на ResNet-50.

## Алгоритм использования
* Отправь боту изображение картины и бот вернет ТОП-3 предсказания художественного стиля

## Сборка бота на локальном компьютере
* Скачать файлы с репозитория
* Добавить токен бота, как Environment Variable в своей ОС
* Установить Docker и docker-compose
* Собрать и запустить контейнеры <code>docker-compose up --build</code>

Нейросеть написана и обучена в Google Colab с использованием fastai 1.0.61 на основании статьи https://medium.com/yottabytes/painting-style-classification-with-7-lines-of-code-6e7e81b3579

Данные для обучения нейросети взяты с https://www.kaggle.com/c/painter-by-numbers/
