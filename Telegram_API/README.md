
# Telegram API dla Python

## Instalacja
	
```
$ pip install python-telegram-bot --upgrade
```

## Konfiguracja

Zamiast `'TOKEN'` trzeba wpisać swój własny token dostępu, poproś [BotFather](https://t.me/botfather) żeby otrzymać swój `'TOKEN'`, 
[jak otrzymać swój TOKEN](https://core.telegram.org/bots#6-botfather)

## Funkcja Print()
Będziemy często używać tej funkcji żeby wyświetlać dane.
Funkcja wywołuje się poprzez wpisanie **print(dane do wyświetlenia)**
		
```python
print(5) 
>>wypisze 5
	
print(5+2)
>>wypisze 7
```
	
## Uruchomienie
Uruchom [skrypt](https://github.com/awitwicki/Programming/blob/master/Telegram_API/przyklad.py) i wyślij do bota wiadomość `/hello` 
, odpowiedzią będzie
> Hello {Username}

### Definuj swoje funkcje 

I dodawaj ich do `updater.dispatcher.add_handler(CommandHandler('tekstowa_nazwa_funkcji', imie_funkcji))`
