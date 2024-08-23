# API для базы с автомобилеями
## Инструкция по запуску 
### Инструкция с помощью docker-compose
#### 1. Находясь в директории с файлами docker-compose.yaml прописываем
<code>docker-compose up --build</code>
#### 2. Переходим по http://localhost:3000/docs

### Инструкция через установку зависимосттей и запуск через uvicorn 
#### 1. Переходи в /src и устанавливаем все зависимости 
<code>pip install -r requirements.txt</code>
#### 2. Возвращаемся назад и пишем команду
<code>uvicorn src.main:app --port 3000 --reload</code>