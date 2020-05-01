# blog_kodland

<h1>Описание проекта:</h1>

У сайта есть две страницы:
<ul>
    <li>Главная страница, со списком последних 10 статей, доступна по URL: <i>/</i></li>
    <li>Страница для добавления поста с формой, доступна по URL <i>/add_article</i></li>
</ul>


<h3>Недостатки в работе:</h3>
<ul>
    <li>Проект не доделан в части верстки!</li>
    <li>При верстке сайта не используется materialize</li>
</ul> 

<h3>Все запросы к API можно потрогать с помощью swagger: <i>/api/swagger</i></h3>

<h3>Запуск проекта (через docker-compose):</h3>
Клонируем репозиторий
```
git clone https://github.com/metro6/blog_kodland.git
cd blog_kodland
```
Создаем файл с настройками Django
```
cp blog_kodland/src/custom_settings/custom_settings.py.example blog_kodland/src/custom_settings/custom_settings.py
```
Запускаем проект
```
(sudo) make build
(sudo) make up
```
Или остановите его
```
(sudo) make down
```

После запуска, проект будет доступен по адресу "http://you_domain_or_ip:8001"

<h3>В проекте используется:</h3>
<ul>
    <li>django</li>
    <li>DRF</li>
    <li>postgresql + django-ORM</li>
    <li>Препроцессор PUG для верстки и Stilus для CSS</li>
    <li>jQuery</li>
    <li>docker-compose</li>
    <li>nginx</li>
    <li>gunicorn</li>
<li>swagger</li>
</ul>


<h3>P.S.:</h3>
Можно так же запустить проект как мы обычно привыкли при работе с Docker
```bash
(sudo) docker-compose build
(sudo) docker-compose up
(sudo) docker-compose down
```
Если нужно запустить проект без docker, вы знаете как это сделать :)