# Podstawy Python

**Python** – język programowania wysokiego poziomu ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek standardowych, którego ideą przewodnią jest czytelność i klarowność kodu źródłowego.
[Wikipedia](https://pl.wikipedia.org/wiki/Python)

## Funkcja Print()
Będziemy często używać tej funkcji żeby wyświetlać dane.
Funkcja wywołuje się poprzez wpisanie **print(dane do wyświetlenia)**
		
```python
		print(5) 
		>>wypisze 5
	
		print(5+2)
		>>wypisze 7
```
	
## Zmienne w python
W Pythonie zmienne definują się przez wpisanie imia zmiennej

> [imię zmiennej] = [jakaś wartość]

Żeby zdefiniować pustą zmienną trzeba przypisać jej wartość **None**
```python
	moja_zmienna = None
    zmienna_a =  5 
    zmienna_b =  3.7 
    zmienna_c = 'python'
```

Interpretator Python sam definuję typ zmiennej, więc 
**zmienna_a** będzie miała typ **int**,
**zmienna_b** będzie miała typ **float**,
**zmienna_c** będzie miała typ **string**

## Ciągi (array)
Definicja nowego pustego ciągu:
```python
    ciag = []
   ```
Definicja ciągu, wypełnionego jakimiś danymi: 
```python	
    inny_ciag = [1,2,3]
    print(inny_ciag)
    >>[1, 2, 3]
 ```

Żeby  zrobić jakąś operację nad elementem ciągu trzeba użyć operator indexu:
```python
    inny_ciag[0] = 3
```
Po tej operacji w ciągu zmieni się tylko zerowy element i dane będą mieli taki wygląd: 

```python
	print(inny_ciag)
    >>[3, 2, 3]
```
Żeby dodać element do ciągu trzeba użyć operator **.append()**
```python
	inny_ciag.append(9)
```
Po tej operacji w ciągu na końcu doda się jeden element i dane będą mieli taki wygląd:
```python
	print(inny_ciag)
    >>[3, 2, 3, 9]
```
     
## Operacje arytmetyczne
Najczęściej używane operacje:

Dodawanie
```python
	nowa_zmienna = stara_zmienna + 2
	
	nowa_zmienna = nowa_zmienna  + 2 #doda do tej zmiennej wartość 2
	
	#To samo można napisać używając operator +=
	nowa_zmienna+=2
```
> Usuwanie: - (minus)
> Dzielenie: / (slash)
> Mnożenie: * (gwiazdka)

## Pętle

Pętla `for` "przebiega" przez podany ciąg liczb, możemy ją zrealizować z użyciem funkcji `range`.  


```python
	pierwsze = [2,3,5,7]
	for pierwsza in pierwsze:
	    print (pierwsza)

	>>> 2 3 5 7
```

Funkcja `range()` 
```python
	# Wypisze liczby 0 1 2 3 4
	for x in range(5):
	    print (x)

	# Wypisze 3 4 5
	for x in range(3,6):
	    print (x)
```



Pętla `while` wykonuje się dopóki pewien warunek logiczny jest spełniony. Przykład:
```python
	# Wypisze 0 1 2 3 4

	licznik = 0
	while licznik < 5:
	    print (licznik),
	    licznik += 1  # Ma to taki sam efekt jak licznik = licznik + 1
```

## Operatory logiczne
Python posiada specjalny typ danych logicznych, który jest używany w instrukcjach warunkowych i pętlach. Wartości logiczne  `True`  albo  `False`  są najczęściej zwracane, kiedy porównujemy ze sobą dwie wartości.

```python
	x = 2
	print (x == 2) # wypisze True
	print (x != 2) # wypisze False
	print (x == 3) # wypisze False
	print (x < 3)  # wypisze True
```

### Operator `IF`
Używamy operator `if` żeby program wypełniał się w zależności od warunków wejściowych/obliczonych
```python
	x = 2
	if x == 2:
	    print ("x wynosi dwa!")
	else:
	    print ("x jest rozne od dwoch.")
```
Podany kod wypisze `x wynosi dwa!` ponieważ spełnia się warunek `x == 2` co równi się `True`.

### Operator `and` i `or` 
Operatory logiczne `and` i `or` (pol. "i" i "lub") pozwalają na budowanie kompletnych zdań logicznych, na przykład:
```python
	imie = "Jan"
	wiek = 23
	if imie == "Jan" and wiek == 23:
	    print ("Nazywasz sie Jan i masz 23 lata.")

	if imie == "Jan" or imie == "Robert":
	    print ("Nazywasz sie Jan lub Robert")
```

## Funkcje

Używany funkcję żeby zmiejszyć ilość kodu i zrobić go więcej czytelnym.

W Pythonie bloki kodu (w tym również funkcje) są wyróżniane za pomocą wcięć w następujący sposób: naglowek_kodu:
```python
naglowek_bloku: 
    1. linia bloku 
    2. linia bloku 
```
Najczęściej nagłówek bloku ma następującą budowę

```python
	slowo_koluczowe_bloku nazwa_bloku(argument1, argument2, ...)
```
Funkcje są definiowane z użyciem słowa kluczowego `def`, po którym umieszcza się nazwę funkcji, a potem nawiasy. Jeżeli funkcja nie wymaga informacji z zewnątrz nawiasy pozostawiamy puste.
```python
	def przywitanie():
	    print ("Pozdrowienia z mojej funckji!")

	def przywitanie_imienne(imie, zyczenia):
	    print ("Witaj" + imie + ". Zycze Tobie " + zyczenia)

	przywitanie() # Wypisze "Pozdrowienia z mojej funckji!"
	przywitanie_imienne("Jacek", "zdrowia") # Wypisze immienne zyczenia
```

### Jak wywoływać funkcje w Pythonie?

Po prostu napisz nazwę funkcji razem z argumentami w nawiasach, jak widać w przykładach poniżej:

```python
	def dzielenie(dzielna, dzielnik):
	    if(dzielnik == 0):
	        return # zakoncz funkcje nic nie zwracajac
	    else:
	        return dzielna / dzielnik

	def przywitanie():
	    print ("Pozdrowienia z mojej funckji!")

	def przywitanie_imienne(imie, zyczenia):
	    print ("Witaj", imie, ". Zycze ci", zyczenia)

	# brak argumentow i zwracanej wartosci
	przywitanie()

	# brak zwracanej wartosci, ale sa juz argumenty
	przywitanie_imienne("Jacek", "zdrowia")

	# jak przypisac zmiennej wartosc zwrocona przez funkcje
	x = dzielenie(9, 3)
	print (x)
```


## Klasy i obiekty

Obiety są połączeniem zmiennych i funkcji w jedną strukturalną całość. Obiekty biorą swoje zmienne i funkcje z klas. Klasy są podstawowym schematem, według których tworzone są obiekty.

Poniżej znajduje się bardzo prosty przykład klasy:

```python
	class MojaKlasa:
		zmienna = "blah"
		def funkcja(self):
			print ("To jest wiadomość wewnątrz klasy.")
```

Nieco później wyjaśnimy, dlaczego powinieneś dołączać "self" jako parametr. Aby stworzyć obiekt będący realizacją klasy wystarczy przypisać nazwie zmiennej wartość wyrażenia  `nazwa_klasy()`.

```python
	class MojaKlasa:
	    zmienna = "blah"

	mojobiekt = MojaKlasa()

```
Teraz zmienna "mojobiekt" przechowuje obiekt klasy  `MojaKlasa`, który zawiera zmienne i funkcje, które zostały zdefiniowane w środku klasy  `MojaKlasa`.

### Dostęp do zmiennych w obiektach

Aby dostać się do zmiennej wewnątrz nowo utworzonego obiektu  `MojaKlasa`  należy to zrobić tak:

```python
mojobiekt.zmienna
```
Tak więc na przykład możesz wypisać napis "ple": class MojaKlasa: zmienna = "blah"

```python
	mojobiekt = MojaKlasa()
	mojobiekt.zmienna = "ple"
	print (mojobiekt.zmienna)
	# Wypisze ple
```

Możesz wielokrotnie tworzyć obiekty należące do tej samej klasy (mające te same zdefiniowane zmienne i funkcje). Jednakże, każdy obiekt zawiera niezależną kopię zmiennej zdefiniowane w klasie. Na przykład jeśli zdefiniujemy inny obiekt klasy  `MojaKlasa`  i zmienimy wspomnianą wyżej zmienną:

```python
	class MojaKlasa:
	    zmienna = "blah"

	mojobiekt = MojaKlasa()
	mojobiekt.zmienna = "ple"
	mojobiekt2 = MojaKlasa()
	mojobiekt2.zmienna = "ploteczka"

	print (mojobiekt.zmienna) # ple
	print (mojobiekt2.zmienna) # ploteczka

```
### Dostęp do funkcji obiektu

Aby dostać się do funkcji wewnątrz obiektu, należy użyć podobnej notacji jak w przypadku zmiennych:

```python
nazwa_obiektu.nazwa_funkcji()
```
### Ćwiczenie

Mamy klasę zdefiniowaną dla pojazdów –  `Pojazd`. Stwórz dwa nowe obiekty tej klasy:  `Auto1`  i  `Auto2`.  `Auto1`  powinno mieć kolor "czerwony", rodzaj "kabriolet", wartość 60000 i nazwę "Ferrari".  `Auto2`  powinien mieć kolor "niebieski", rodzaj "autobus", wartość 10000 i nazwę "Ikarus".