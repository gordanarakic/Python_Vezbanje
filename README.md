# Mini Data Monitoring Platform 

Program učitava merenja virtuelnih uređaja (CSV ili JSON), izračunava
broj, prosek i maksimum CPU merenja po uređaju, prijavljuje uređaje
iznad zadatog praga i duplikate merenja. Za sve greške vraća poruku u loggeru,
a potrebne rezultate ispisuje u rezultati.txt

## Pokretanje
Sve se nalazi u main funkciji, tako da se samo ona pokrene.
Kada se pokrene traži se prag za proveru CPU

## Ulazni podaci
-measurements_initial.csv
-measurements_edge_cases.csv
-measurements_initial 1.csv
-JSON: measurements_initial.json
-Timestamp može da bude u obliku `2026-11-12T08:05:00Z` ili `1794470700`

## Izlaz
-rezultati se upisuju u rezultati.txt
-greške se upisuju u loger.log