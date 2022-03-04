Share Desk
==========

Diploma thesis

## Development

### Installation

Install [Docker](https://docs.docker.com/install/) and [Docker-Compose](https://docs.docker.com/compose/). Start your
virtual machines with the following shell command:

`docker-compose up --build`

If all works well, you should be able to create an admin account with:

`docker-compose run --rm backend python manage.py createsuperuser`

#### Adding package to pipenv

After adding, run `docker-compose up --build`

### Database

#### Migrations

`docker-compose run --rm backend python manage.py makemigrations`

`docker-compose run --rm backend python manage.py migrate`

#### Reset migrations

https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html

1. Drop cascade
2. Remove migrations from folder
3. `docker-compose run --rm backend python manage.py makemigrations <app_name>`
4. `docker-compose run --rm backend python manage.py migrate --fake <app_name> zero`
5. `docker-compose run --rm backend python manage.py migrate <app_name>`

#### Manual backup

From dir where you want to back up file, ideally `/tmp/backups` to match docker-compose

`docker run --rm -v "$PWD:/backups" -u "$(id -u):$(id -g)" -e POSTGRES_HOST=host.docker.internal -e POSTGRES_DB=share_desk -e POSTGRES_USER=postgresuser -e POSTGRES_PASSWORD=mysecretpass  prodrigestivill/postgres-backup-local /backup.sh`

## Deploy app

For production you'll need to fill out `.env` file and use
`docker-compose-prod.yml` file:

    $ docker-compose -f docker-compose-prod.yml up --build -d

The app will then be available at http://localhost

## Built With

* [Docker](https://www.docker.com/)
* [12 Factor](http://12factor.net/)
* Template: [Vuexy](https://pixinvent.com/demo/vuexy-vuejs-admin-dashboard-template/landing/)
* Frontend: [Vue.js](https://vuejs.org/) + [Vue Cli](https://cli.vuejs.org/)
  + [PWA](https://developers.google.com/web/progressive-web-apps/)
* Backend: [Django](https://www.djangoproject.com/)
* Database: [PostgreSQL](https://www.postgresql.org/)
* Server: [Nginx](https://nginx.org/)
* API:  [Django REST Framework](https://www.django-rest-framework.org/)

## Versioning

I use [Conventional versioning](https://www.conventionalcommits.org/en/) for versioning style with combination
of [standard version utility](https://github.com/conventional-changelog/standard-version) . For the versions available,
see the
[Releases on this repository](https://github.com/dominikbullo/ShareDesk/releases) or if you need more details you could
check you
[Tags on this repository](https://github.com/dominikbullo/ShareDesk/tags).

### New version

Must have a node installed and then run command: `standard-version`

## Authors

* **Dominik Bullo** - *Initial work* - [bullo.sk](http://bullo.sk/)

## License

This project is licensed under the GPL License - see the [LICENSE](LICENSE) file for details

## Assignment

1. Analýza požiadaviek na systém.

- 1.1. Používatelia rôznych typov (zamestnanec, administrátor)
- 1.2. Prihlásenie/Registrácia používateľov
- 1.3. Rozdeľovanie zamestnancov do tímov
- 1.4. Správa zdieľaných pracovných miest s vizuálnou reprezentáciou miest a dispozícií priestorov.
- 1.5. Priraďovanie miest tímom ale aj jednotlivým zamestnancom (majú nárok na stále prac. miesto)
- 1.6. Možnosť realtime vizualizácie obsadenosti prac. miest.
- 1.7. Rezervovanie prac. miest s pol dnovou granularitou.
- 1.8. Možnosť reportovať technické alebo iné problémy spojené s pracovným miestom.

2. Analýza nefunkcionálnych požiadaviek, výber vhodných technológii (implementačný jazyk, framework, databáza)
3. Implementácia, otestovanie a produkčné nasadenie
4. Vyhodnotenie prínosov
