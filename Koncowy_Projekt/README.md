
# Telegram Bot klassyfikator obrazków

## Konfiguracja

Zamiast `'TOKEN'` trzeba wpisać swój własny token dostępu, poproś [BotFather](https://t.me/botfather) żeby otrzymać swój `'TOKEN'`, 
[jak otrzymać swój TOKEN](https://core.telegram.org/bots#6-botfather)

## Uruchomienie

Uruchom skrypt [Telegram_Bot_Klassyfikator.py](https://github.com/awitwicki/Programming/blob/master/Koncowy_Projekt/Telegram_Bot_Klassyfikator.py)

Wyślij do bota zdjęcie białej liczby na czarnym tle.

![image](https://github.com/awitwicki/Programming/blob/master/Koncowy_Projekt/img/photo.jpg)

Najpierw wypisze się w konsoli:

```
Model restored from file: model/olp_model.ckpt
[[ 1.5880934  -3.3227477  -0.9568946  -0.08495197  0.17962937  2.7694426 -2.8008049   0.6884552   1.2097203   0.7300641 ]]
```

Po tym bot wyśle wiadomość, zawierającą klasę liczby na obrazku

![Image](https://github.com/awitwicki/Programming/blob/master/Koncowy_Projekt/img/example.PNG)
