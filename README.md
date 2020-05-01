# blog_kodland

<b>Описание проекта:</b>

У сайта есть две страницы:
<ul>
<li>Главная страница, со списком последних 10 статей</li>
<li>Страница для добавления поста с формой, доступна по URL /add_article</li>
</ul>
<b>Недостатки в работе:</b>
<ul>
<li>Проект не доделан в части верстки!</li>
<li>При верстке сайта не используется materialize</li>
</ul> 

Запуск проекта (через docker-compose):
```
git clone https://github.com/metro6/blog_kodland.git
cd blog_kodland
```
Создайте файл с настройками Django
```
cp blog_kodland/src/custom_settings/custom_settings.py.example blog_kodland/src/custom_settings/custom_settings.py
```

Запустите проект
```
(sudo) make build
(sudo) make up
```

Или остановите его
```
(sudo) make down
```

После запуска, проект будет доступен по адресу "http://you_domain_or_ip:8001"

В проекте используется:
- docker-compose
- nginx
- gunicorn
- django
- DRF
- postgresql

Можно так же запустить проект как мы обычно привыкли при работе с Docker
```bash
(sudo) docker-compose build
(sudo) docker-compose up
```

Если нужно запустить проект без docker, вы знаете как это сделать :)