AUTORZY PROJEKTU HIEROGLIFY:

	Dzięgiel Katarzyna
	Szpor Magdalena
	Szymczuk Agnieszka

-----------------------------------------------
OPIS ZAWARTOŚCI:

Katalog "Program_hieroglify" zawiera:

1. Plik projekt.py, czyli główny kod napisany w języku python do rozpoznawania 	  hieroglifów i tłumaczenia ich na język polski.

2. 3 obrazy: chufu.jpg, kleopatra.jpg, ptolemeusz.jpg, które będą podlegały tłumaczeniu.

3. 14 wzorców, które są niezbędne do tłumaczenia powyższych obrazów.

4. Plik Readme.txt z pomocniczym opisem.

5. Raport "Raport_koncowy" w wersji pdf.

6. Plik "Makefile" w celu umożliwienia uruchamiania programu za pomocą komendy "make run".

7. Prezentacja do projektu.

-----------------------------------------------
OPIS PROGRAMU:

Program służy do rozpoznawania graficznych znaków - egipskich hieroglifów oraz tłumaczy znalezione słowa na język polski.

-----------------------------------------------
SPOSÓB URUCHAMIANIA:

W celu uruchomienia programu należy za pomocą terminala wejść do katalogu "Program_hieroglify". Tam znajduje się plik o nazwie "Makefile".
Po wpisaniu do terminalu komendy "make run" program się uruchamia i rozpoczyna się kompilacja.
Na początku wyświetlą się dwa obrazki. Na pierwszym z nich po lewej stronie znajduje się wzorzec, a po prawej obrazek, który jest tłumaczony, z zakreślonymi na czerwono znalezionymi obszarami. Drugi obrazek to mapa współczynników korelacji.
W momencie gdy zamknie się oba obrazki, to pojawią się nowe dwa dotyczące kolejnej szukanej litery.
Gdy zamknie się wszystkie obrazki, które zostaną wyświetlone, w terminalu pojawi się informacja o znalezionych literach (po sortowaniu), wyraz po egipsku, a na końcu jego tłumaczenie na język polski.
Domyślnie program jest ustawiony na tłumaczenie obrazka "chufu.jpg". W celu tłumaczenia obrazka "kleopatra.jpg" lub "ptolemeusz.jpg" należy w programie odpowiednio odkomentować linijki 132-139 lub 145-151, a zakomentować 124-126.

