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

`docker run --rm --tty --interactive -v $BACKUPFILE:tmp/backups/daily/share_desk-20220322.sql.gz postgres:$VERSION /bin/sh -c "zcat tmp/backups/daily/share_desk-20220322.sql.gz | psql --host=host.docker.internal --username=postgresuser --dbname=share_desk -W`

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

You could also see all changes in [CHANGELOG](CHANGELOG) file with detail changes.

### New version

Must have a node installed and then run command: `standard-version`

## Authors

* **Dominik Bullo** - *Initial work* - [bullo.sk](http://bullo.sk/)

## License

This project is licensed under the GPL License - see the [LICENSE](LICENSE) file for details

## Assignment

1. Anal??za po??iadaviek na syst??m.

- 1.1. Pou????vatelia r??znych typov (zamestnanec, administr??tor)
- 1.2. Prihl??senie/Registr??cia pou????vate??ov
- 1.3. Rozde??ovanie zamestnancov do t??mov
- 1.4. Spr??va zdie??an??ch pracovn??ch miest s vizu??lnou reprezent??ciou miest a dispoz??ci?? priestorov.
- 1.5. Prira??ovanie miest t??mom ale aj jednotliv??m zamestnancom (maj?? n??rok na st??le prac. miesto)
- 1.6. Mo??nos?? realtime vizualiz??cie obsadenosti prac. miest.
- 1.7. Rezervovanie prac. miest s pol dnovou granularitou.
- 1.8. Mo??nos?? reportova?? technick?? alebo in?? probl??my spojen?? s pracovn??m miestom.

2. Anal??za nefunkcion??lnych po??iadaviek, v??ber vhodn??ch technol??gii (implementa??n?? jazyk, framework, datab??za)
3. Implement??cia, otestovanie a produk??n?? nasadenie
4. Vyhodnotenie pr??nosov
