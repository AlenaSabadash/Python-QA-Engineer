# Анализ логов веб-сервера Apache

## Установка:

```
$ pip install -r requirements.txt
```

## Как пользоваться анализатором логов?

*Анализ всех лог-файлов в текуще директории:*

```
python3 main.py -l "*.log"
```

*Анализ конкретного лог-файла*

```
python3 main.py -l "access.log"
```

*Анализ всех лог-файлов по указанному пути*

```
python3 main.py -p /home/<username>/apache/logs -l "*.log"
```

*Анализ конкретного лог-файла по указанному пути*

```
python3 main.py -p /home/<username>/apache/logs -l "access.log"
```