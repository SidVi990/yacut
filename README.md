# Yacut сервис для укорачивания ссылок

## Описание:

Сервис позволяет сделать из длинной и неудобной сыылки лаконичную и красивую.

## Стек технологий:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить проект:

```
flask run
```

Весь функционал будет доступен по адресу `http://127.0.0.1:5000`

Для доступа к API используейте эндпоинты:

* `/api/id/` - для создания короткой 

* `/api/id/{short_id}/` - для получения полной ссылки

## Примеры запросов к API

* Выполните POST-запрос к `http://127.0.0.1:5000/api/id/` передав поле `url` и, при желании, свой вариант короткой ссылки в поле `custom_id`.

    API вернет полную укороченную ссылку и оригинальный url:

    ```
    {
        "short_link": "string",
        "url": "string"
    }
    ```

* Выполните GET-запрос к `http://127.0.0.1:5000/api/id/{short_id}/` для получения оригинальной ссылки:

    ```
    {
      "url": "string"
    }
    ```

## Автор

[Евгений Малый](https://github.com/SidVi990)

