# Mini Data Monitoring Platform 

Program učitava merenja virtuelnih uređaja (CSV ili JSON), izračunava
broj, prosek i maksimum CPU merenja po uređaju, prijavljuje uređaje
iznad zadatog praga i duplikate merenja. Za sve greške vraća poruku u loggeru,
a potrebne rezultate ispisuje u rezultati.txt. Napravljen je da moze ove zadatke da izvrsi uz pomoc koda,
preko baze PostgreSQL ili koriscenjem polarsa. Koriscen je venv za instalaciju nekih paketa koji se nalaze u paketi.txt

## Pokretanje
Pre pokretanja programa treba da se izabere u mainu nacin izlistavanja rezultata (preko pythona, baze ili polarsa). Kada se to izabere samo se pokrene program i izvrsava se sta treba.

## Ulazni podaci
-measurements_initial.csv
-measurements_edge_cases.csv
-measurements_initial 1.csv
-devices.csv
-JSON: measurements_initial.json
-paketi.txt
-Timestamp može da bude u obliku `2026-11-12T08:05:00Z` ili `1794470700`

## Izlaz
-rezultati se upisuju u rezultati.txt
-greške se upisuju u loger.log