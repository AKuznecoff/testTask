# testTask
# Требования
- docker
- docker-compose
# Запуск
sudo docker-compose up --build
# Как использовать
Приложение запускается на порту 5000.
Для взаимодействия с приложением необходимо отправить POST запрос с json-сообщением.
В ответ приложение также отправить json-сообщение.
### Формат json-сообщений для взаимодействия
для вызова ping:
```
{
    "description":
	{
	    "operation":"ping"
	}
}
```

для вызова add:
```
{
    "addition":
	{
	    "uuid":<uuid>
	}
    "description":
	{
	    "operation":"add",
	    "sum":<сумма>
	}
}
```
для вызова substract:
```
{
    "addition":
	{
	    "uuid":<uuid>
	}
    "description":
	{
	    "operation":"substract",
	    "sum":<сумма>
	}
}
```
для вызова status:
```
{
    "addition":
	{
	    "uuid":<uuid>
	}
    "description":
	{
	    "operation":"status"
	}
}
```
