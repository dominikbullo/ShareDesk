Share Desk
==========

Diploma thesis

## Development

Install [Docker](https://docs.docker.com/install/) and [Docker-Compose](https://docs.docker.com/compose/). Start your virtual machines with the following shell command:

`docker-compose up --build`

If all works well, you should be able to create an admin account with:

`docker-compose run backend python manage.py createsuperuser`


##Assignment
1.	Analýza požiadaviek na systém
   - 1.1.	Používatelia rôznych typov (zamestnanec, administrátor)
   - 1.2.	Registrácia pomocou exspirujúceho tokenu. (administrátor odošle email s registračnou linkou zamestnancom)Prihlásenie/Registrácia používateľov
   - 1.3.	Rozdeľovanie zamestnancov do tímov
   - 1.4.	Správa zdieľaných pracovných miest s vizuálnou reprezentáciou miest a dispozícií priestorov.
   - 1.5.	Priraďovanie miest tímom ale aj jednotlivým zamestnancom (majú nárok na stále prac. miesto)
   - 1.6.	Možnosť realtime vizualizácie obsadenosti prac. miest.
   - 1.7.	Rezervovanie prac. miest  s pol dnovou granularitou.
   - 1.8.	Možnosť reportovať technické alebo iné problémy spojené s pracovným miestom.
2.	 Analýza nefunkcionálnych požiadaviek, výber vhodných technológii (implementačný jazyk, framework, databáza)
3.	Implementácia, otestovanie a produkčné nasadenie
4.	Vyhodnotenie prínosov
