Aplikacja zarządzająca obiegiem narzędzi skrawających w przedsiębiorstwie

Główne funkcjonalności (moduły) aplikacji:

1. Logowanie – do bazy/aplikacji mogą mieć dostęp tylko uprawnieni użytkownicy.

2. Narzędzia: 
a) moduł ten ma za zadanie wyszukiwać narzędzie po numerze EDV, który ma mieć postać 51 - *****. 
b) po wyszukiwaniu narzędzia aplikacja ma wyświetlać stan magazynowy danego narzędzia, tzn: 
- ilość sztuk w magazynie produkcyjnym, 
- zużycie miesięczne narzędzia oraz jeśli stan  narzędzia wystarcza na czas krótszy niż tydzień musi informować o niskim stanie i zagrożeniu zatrzymania maszyny produkcyjnej na brak narzędzia. 
- ma wyświetlać wszystkie informację dotyczące danego narzędzie, tzn. 
	• nr półfabrykatu w postaci 57-*****, 
	• informację czy narzędzie jest prawe czy lewe, 
	• czy narzędzie jest kupne czy produkowane przez naszą firmę, 
	• typ narzędzia: obrotowe czy toczne, 
	• rodzaj narzędzia: wiertło, rozwiertak, płytka etc., 
	• maszynę, na której jest produkowane to narzędzie, 
	• detal produkcyjny, na którym pracuje dane narzędzie, 
	• maszynę produkcyjną, 
	• cena półfabrykatu, 
	• cena wyprodukowania narzędzia, 
	• firmę powlekającą, powłokę. 

c) Z tego modułu musimy mieć możliwość dodania rysunku narzędzia w pdf, rysunku detalu w pdf oraz planu ustawczego w pdf. 

3. Powlekanie: 
– w tym module musimy mieć możliwość wyszukania narzędzia po jego EDV,
- mieć możliwość przypisać do danego narzędzia:
	• rodzaj powłoki, 
	• firmę powlekającą, 
	• cenę powlekania w walucie PLN oraz EUR. 
- informacje dodane w tym module mają wyświetlać się w module Narzędzia, po wpisaniu nr EDV czyli oba moduły muszą być ze sobą powiązane.

4. Wycena: 
– w tym module znajdować się ma kalkulator, do którego wprowadzamy informację takie jak:
	• typ narzędzia, 
	• rodzaj, 
	• półfabrykat, 
	• czas maszynowy, 
	• maszynę na której produkowane jest narzędzie.

5. Wimmer (magazyn działu szlifierni narzędzi):
– moduł ma zawierać informację o nadwyżkach narzędziowych. Będą tu przechowywane ilości narzędzi, których stan przekracza miesięczne zapotrzebowanie więc nie będą one od razu kierowane do magazynu produkcyjnego tylko przechowywane w magazynie szlifierni, dopiero kiedy stan na magazynie produkcyjnym zostanie zredukowany wtedy ilości będą przenoszone ręcznie z magazynu szlifierni. Informację o tym, że narzędzie znajduje się w Wimmer’ze musi wyświetlać się również w module Narzędzia, po wpisaniu EDV w wyszukiwarce. 
