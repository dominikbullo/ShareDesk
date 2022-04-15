# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [0.6.2](https://github.com/dominikbullo/ShareDesk/compare/v0.6.1...v0.6.2) (2022-04-15)


### Features

* **reservations-manager:** fix table data ([21ef94c](https://github.com/dominikbullo/ShareDesk/commit/21ef94c0725ca51cd3414a3d5a26c14f2fff28fd))
* **spot-issues:** allow changing issue status ([8222225](https://github.com/dominikbullo/ShareDesk/commit/822222558be1cadeef7dd15a01e5bdf45b0217b6))
* **spot-issues:** correct info in table & deleting issue working ([fe2e94b](https://github.com/dominikbullo/ShareDesk/commit/fe2e94b2a11680d30ad835349c8ed4b9d18e910e))
* **teams:** removing teams now working correctly ([0685e83](https://github.com/dominikbullo/ShareDesk/commit/0685e835a8141b88e49a68e0609efcc267ce250a))
* **users:** User can be removed (is_active=False) from app ([fa2f4eb](https://github.com/dominikbullo/ShareDesk/commit/fa2f4ebf87ae66f2a09ba29fc54958a53730062a))


### Bug Fixes

* **UI:** clean selected seats after submit ([6524a48](https://github.com/dominikbullo/ShareDesk/commit/6524a48695535bc62cf2470a0ae4c3f92243e882))

### [0.6.1](https://github.com/dominikbullo/ShareDesk/compare/v0.6.0...v0.6.1) (2022-04-05)


### Features

* badges ([f7af3f9](https://github.com/dominikbullo/ShareDesk/commit/f7af3f953eec6e864854df38f626bf1f9d3bae62))
* multiselect on touch devices ([c14c1f0](https://github.com/dominikbullo/ShareDesk/commit/c14c1f0f72ee83941644a1232bd579fc0cd37b36))
* **spot-issues:** Now you can submit spot issue from ReservationsBooking.vue ([685c651](https://github.com/dominikbullo/ShareDesk/commit/685c651c8347108f51648b16241e6e36fb0edbc4))


### Bug Fixes

* if created room generate seats ([e1eb22a](https://github.com/dominikbullo/ShareDesk/commit/e1eb22a713eb0d59276cffda7986fced8ec3a986))

## [0.6.0](https://github.com/dominikbullo/ShareDesk/compare/v0.5.0...v0.6.0) (2022-03-31)


### ⚠ BREAKING CHANGES

* **reservation:** Reservation now could be created from FE

### Features

* **reservation:** now supporting permanent pending and allowed in reservations view ([a959d3e](https://github.com/dominikbullo/ShareDesk/commit/a959d3e8da7cd902eeafa1a8f8bc58c7877b6c49))
* **reservation:** Reservation now could be created from FE ([7c87959](https://github.com/dominikbullo/ShareDesk/commit/7c8795971661699f8d015cd81a3f00c063ff1fc6))
* spinner while loading ([1e2897a](https://github.com/dominikbullo/ShareDesk/commit/1e2897a4ed0322dac1dee504e74cfbfe547a0ec5))

## [0.5.0](https://github.com/dominikbullo/ShareDesk/compare/v0.4.2...v0.5.0) (2022-03-31)


### ⚠ BREAKING CHANGES

* **workspaces:** Auto generated seats when creating room

### Features

* **auth:** force re-login if bad refresh token for whatever reason ([fa61750](https://github.com/dominikbullo/ShareDesk/commit/fa61750478adb22169772afe1d71ff939d4b12de))
* **reservation:** multiple seat selection on FE ([8d522e0](https://github.com/dominikbullo/ShareDesk/commit/8d522e0b1c0144e87f03eb86556e3b7dece456a3))
* **reservation:** permanent now working ([81b1bfa](https://github.com/dominikbullo/ShareDesk/commit/81b1bfaf41d115d4b08c6550df60f9c5ddb7094f))
* **reservation:** POC and creating reservation from FE working ([47447fc](https://github.com/dominikbullo/ShareDesk/commit/47447fcd9684a3c048ffe0178fd050c4684b3654))
* **reservation:** reservation api create reservation working ([237b961](https://github.com/dominikbullo/ShareDesk/commit/237b96186f0471a8fa73ee3c0eba90f133c466ba))
* **reservation:** Seat data showing when seat is selected ([0bfc8a7](https://github.com/dominikbullo/ShareDesk/commit/0bfc8a757426fa5a16189226dba656f9d159a61b))
* **reservation:** seat reservation data on alt + click ([d8ad2d4](https://github.com/dominikbullo/ShareDesk/commit/d8ad2d433e386798221d15144f02787bba610f40))
* **workspaces:** seats are creating automatically when room is created ([2e147f2](https://github.com/dominikbullo/ShareDesk/commit/2e147f257693d684adee7889cb897d8fe5bd47b0))


### Bug Fixes

* reservation date keys ([e87a111](https://github.com/dominikbullo/ShareDesk/commit/e87a11105bd2a47c085a792ecf1dd283ac0f7e13))
* runserver_plus does not work with werkzeug 2.1.0 ([71a612b](https://github.com/dominikbullo/ShareDesk/commit/71a612baf6f8100ce045dbea79070b5acb4e3ecc))
* user lsit search ([f9ea772](https://github.com/dominikbullo/ShareDesk/commit/f9ea772a8a1143b4f8372d201c2647833ecc56af))

### [0.4.2](https://github.com/dominikbullo/ShareDesk/compare/v0.4.1...v0.4.2) (2022-03-29)


### Bug Fixes

* runserver_plus does not work with werkzeug 2.1.0 ([07111e8](https://github.com/dominikbullo/ShareDesk/commit/07111e8a8a423d85a60c1e5d23c48c956a32ea85))

### [0.4.1](https://github.com/dominikbullo/ShareDesk/compare/v0.4.0...v0.4.1) (2022-03-29)


### Features

* Add user to team suggestions working now ([f511251](https://github.com/dominikbullo/ShareDesk/commit/f511251d0c7cd0f6aca690e87d988fe7a2015f02))
* change permanent status from FE ([567773a](https://github.com/dominikbullo/ShareDesk/commit/567773a13465a7ee2035bb8f379856bfe2b6da6b))
* **teams:** You could now add user to team with autosuggestions ([57b58cd](https://github.com/dominikbullo/ShareDesk/commit/57b58cdd36b4837ae04182be9fd3ed440bea38d1))
* **user-reservations:** basics ([c7cb412](https://github.com/dominikbullo/ShareDesk/commit/c7cb412277d06e4058684faa21fadabf67b9c484))

## [0.4.0](https://github.com/dominikbullo/ShareDesk/compare/v0.3.0...v0.4.0) (2022-03-27)


### ⚠ BREAKING CHANGES

* SpotReservations now could contain multiple spots. Primary usage for teams.

### Features

* add user to team modal POC ([9e792a5](https://github.com/dominikbullo/ShareDesk/commit/9e792a5d7033da737acb273c8e644b30845f0950))
* **admin:** better django admin ([a858ef3](https://github.com/dominikbullo/ShareDesk/commit/a858ef39ec65c806a9d256ae775c5e7770fb8eda))
* ManyToMany reservations - spots ([e60b1bc](https://github.com/dominikbullo/ShareDesk/commit/e60b1bcc0d1d7bc3a2a6667daf9c7390cf1cf8d9))
* **my-reservations:** my reservations showing on endpoint and also success tested on FE ([0c80315](https://github.com/dominikbullo/ShareDesk/commit/0c803157f57619fb94b4f6844d78b53d64e7104c))
* team view now has users list filtered by selected team ([7d88d93](https://github.com/dominikbullo/ShareDesk/commit/7d88d938dd9d24c53bf727ed6c47758237940337))


### Bug Fixes

* github actions deploy.yml ([5920566](https://github.com/dominikbullo/ShareDesk/commit/5920566d2d690bbfe80e09cfb0db63fd0a023487))
* github actions deploy.yml again ([e0aa2cb](https://github.com/dominikbullo/ShareDesk/commit/e0aa2cb165c21df81085a64003620a1873c69808))
* multi-day reservations ([18a548e](https://github.com/dominikbullo/ShareDesk/commit/18a548e5f242470cff2925b5e149164afac3f1a4))
* permanent reservation...again ([05210d6](https://github.com/dominikbullo/ShareDesk/commit/05210d61453d31bd0d505a5586f36512153bed6e))
* permanentné miesta sa zobrazia stálo ([3dfc718](https://github.com/dominikbullo/ShareDesk/commit/3dfc718d6207a1f69b7ea4225604e853dd347e8b))
* teams through field ([86b6665](https://github.com/dominikbullo/ShareDesk/commit/86b6665a6485aec2ac1841c5581528b90155fd21))

## [0.3.0](https://github.com/dominikbullo/ShareDesk/compare/v0.2.1...v0.3.0) (2022-03-25)


### Features

* filter reservation based on room and start/end ([ff2a338](https://github.com/dominikbullo/ShareDesk/commit/ff2a3389efe4a080df6f17d92c5dc4c8a7e1b961))
* **reservation:** reservations finally showing correct data from BE ([7b3bab5](https://github.com/dominikbullo/ShareDesk/commit/7b3bab5642d611e39d4428a6c3c8cb0701bbbb0d))
* roomSpotsReservationsData on FE showing correct reservations for selected date and room ([ce7043e](https://github.com/dominikbullo/ShareDesk/commit/ce7043e910cfa7d4779cdbcecfd463db63f58dd1))
* spot to reservation only one to one field ([efbee93](https://github.com/dominikbullo/ShareDesk/commit/efbee93fe5dac7add1ecd66fcbe4574470b8d09f))


### Bug Fixes

* bad name ([0eb026f](https://github.com/dominikbullo/ShareDesk/commit/0eb026f04455e38d2d6cc5814cfffd2ad849e84f))
* github actions ([5526047](https://github.com/dominikbullo/ShareDesk/commit/552604775cfa644d6733c1a69e021fe9eeb00704))

### [0.2.1](https://github.com/dominikbullo/ShareDesk/compare/v0.2.0...v0.2.1) (2022-03-24)


### Features

* **issues-list:** issue list now showing issues added by users using good table ([5999e20](https://github.com/dominikbullo/ShareDesk/commit/5999e201b5b97746d58ad13d339d86bb98510822))
* **modal:** testing reservation modal layouts and functionality ([b84fed3](https://github.com/dominikbullo/ShareDesk/commit/b84fed39eeb7f9cdfc5403dd6386230924e25e55))
* **reservation:** FE get data from BE ([4768b0b](https://github.com/dominikbullo/ShareDesk/commit/4768b0bbc91af7da996a914d0be3fc00bfbcbe8a))
* **reservation:** reservation filter added  - but not working ([7a30512](https://github.com/dominikbullo/ShareDesk/commit/7a30512694a000c1687de14fc93daef3650a0890))
* **reservation:** room data on FE ([a3205f3](https://github.com/dominikbullo/ShareDesk/commit/a3205f337987c01fba91b6ab88787ed9369464cf))
* **seats:** generating seats on FE base od layout ([c38c3fa](https://github.com/dominikbullo/ShareDesk/commit/c38c3fad1e5e2654507613d9588e1c2f9ae78141))
* **team-list:** Team list working with bootstrap tables (ordering & filters on server) ([5c92296](https://github.com/dominikbullo/ShareDesk/commit/5c922960405fe8df37329ecbdacdf1314ffaaff9))
* **users-list:** Team list working with bootstrap tables (ordering/filters/search on server) ([3d1fc3e](https://github.com/dominikbullo/ShareDesk/commit/3d1fc3e174981a57e49cd5b2cbb2ae8395274820))
* **users-list:** User list & user detail ([bc7783e](https://github.com/dominikbullo/ShareDesk/commit/bc7783ea618a6bad916bde6ca23c7a533d6c6345))
* **workspace:** filtrovanie miestnosti aj podľa workspace ([ec7f361](https://github.com/dominikbullo/ShareDesk/commit/ec7f361e75685cff265ecf36bc37afc8ba1f881e))


### Bug Fixes

* **auth:** token refres now working correctly ([33d5e1f](https://github.com/dominikbullo/ShareDesk/commit/33d5e1fa5870c30dea683e378f143fde81d119a3))

## [0.2.0](https://github.com/dominikbullo/ShareDesk/compare/v0.1.0...v0.2.0) (2022-03-22)


### Features

* api support plural ([051a38c](https://github.com/dominikbullo/ShareDesk/commit/051a38c30e4cb5c67d36051cd4d1bb5905c9e2c2))
* **backend:** Django filters ([e842a70](https://github.com/dominikbullo/ShareDesk/commit/e842a70927ae5d6232e01ed8c0aa53eb463b4d20))
* **fe-users:** user list basics ([64b4a1f](https://github.com/dominikbullo/ShareDesk/commit/64b4a1f9a1eba99e468a36b0e1e1857987720ebf))
* **frontend:** account settings basics ([6d7984a](https://github.com/dominikbullo/ShareDesk/commit/6d7984a9e2f1a288ef555632fd1fb5f5becd4364))
* **frontend:** add issues and reservations files and folders structure ([f465539](https://github.com/dominikbullo/ShareDesk/commit/f4655399de30ff7fa1acb4cd87366dcbaac4bdd1))
* **frontend:** anybody can create team now ([de1f12e](https://github.com/dominikbullo/ShareDesk/commit/de1f12e2b32d889bd4059c4d911cfa5fed67a1ae))
* **frontend:** locales fix & basic layout ([35a82f4](https://github.com/dominikbullo/ShareDesk/commit/35a82f40994583593d74c4972d47444b4b0e59a8))
* remove created_by fields for now and prepare teams view ([b61186c](https://github.com/dominikbullo/ShareDesk/commit/b61186c9666e48baa894dd1eee91547c919d2a0f))
* **reservation:** Added Django Polymorphic to reservation for user/team ([e6a7f27](https://github.com/dominikbullo/ShareDesk/commit/e6a7f27fb38400773fdcc6f35296eedd0bc9f2f8))
* **spot-issues:** Spot issue basic list on FE ([6fe08b3](https://github.com/dominikbullo/ShareDesk/commit/6fe08b340010e7f338d885da86d0585768a1f2c5))
* **teams:** basic table copy from user ([819bb6a](https://github.com/dominikbullo/ShareDesk/commit/819bb6a68de2c7992fad6c758dea4c6e45176bd5))
* **workspace:** Model strings methods ([8ab0741](https://github.com/dominikbullo/ShareDesk/commit/8ab0741d33afaa928f3c32d3b939bfbf5358c222))
* **workspace:** Workspaces db more thinking ([9d1c5e6](https://github.com/dominikbullo/ShareDesk/commit/9d1c5e6ab53350ae02e7c4d99f2a8f87eebb6e70))
* **workspace:** Workspaces with layouts kinda working ([a731101](https://github.com/dominikbullo/ShareDesk/commit/a7311016421c15a3ac23c9e668ec9ad1f3752ba2))


### Bug Fixes

* forgot migrations ([77ac406](https://github.com/dominikbullo/ShareDesk/commit/77ac4062c6d59de5420bd0c660a8aaed4cb9e3aa))

## [0.1.0](https://github.com/dominikbullo/ShareDesk/compare/v0.0.3...v0.1.0) (2022-03-12)


### Features

* **FE-users:** Import demo user app ([2bcedeb](https://github.com/dominikbullo/ShareDesk/commit/2bcedebb1f38b41793260d62c71ea06b9488cf38))
* **frontend:** add localization ([c9ae335](https://github.com/dominikbullo/ShareDesk/commit/c9ae33508dfcac5fcaa91a6a4a1d550dd61d56c5))

### [0.0.3](https://github.com/dominikbullo/ShareDesk/compare/v0.0.2...v0.0.3) (2022-03-10)


### Features

* **auth:** If token is undefined on FE, redirect to login page ([0ef4576](https://github.com/dominikbullo/ShareDesk/commit/0ef4576c714083b2add414e3b081eb4c7e7e011e))
* **backend:** logout ([994e0ca](https://github.com/dominikbullo/ShareDesk/commit/994e0ca36585701c6d1622c8f41e546884e020dc))
* **teams:** manytomany in db ([6bc89bc](https://github.com/dominikbullo/ShareDesk/commit/6bc89bcf98fc578c02b4676cf274e0e593afc77e))
* **users:** registrations with necessary infos ([c0795a2](https://github.com/dominikbullo/ShareDesk/commit/c0795a21eeec31418637e27079b51be3e212a4cc))
* version in footer and also as env variable and variable in store ([4e4c80c](https://github.com/dominikbullo/ShareDesk/commit/4e4c80c28175242cd7b82d8aed3a4a0849d983dd))


### Bug Fixes

* **auth:** registration from FE working ([75b0199](https://github.com/dominikbullo/ShareDesk/commit/75b0199e1dfad62d4e79c1a933bc013d2177b616))

### [0.0.2](https://github.com/dominikbullo/ShareDesk/compare/v0.0.1...v0.0.2) (2022-03-04)


### Features

* add user roles ([34e2553](https://github.com/dominikbullo/ShareDesk/commit/34e255310915ac435b35f185f6189f5dfbba3fdb))
* **backend:** add spot to spot reservations ([3d4bc2c](https://github.com/dominikbullo/ShareDesk/commit/3d4bc2ce0b497c9ffd1ac08bc1f1bfe7da14590b))
* **backend:** spot issue added spot ([4593050](https://github.com/dominikbullo/ShareDesk/commit/4593050f331ceb8d5d42a1348564ce61a651de8e))
* db backup links and env variables ([aa3ba10](https://github.com/dominikbullo/ShareDesk/commit/aa3ba10af806692402594821d9c8db3799f7c47a))
* refresh token if expired ([7cebdfc](https://github.com/dominikbullo/ShareDesk/commit/7cebdfc8370f493105ccb091012da2f9405ef56b))


### Bug Fixes

* package-lock files ([d49ad5f](https://github.com/dominikbullo/ShareDesk/commit/d49ad5ff2c9253a922cced6485af04f6ee8a9875))

### [0.0.1](https://github.com/dominikbullo/ShareDesk/compare/v0.0.0...v0.0.1) (2022-02-28)

## 0.0.0 (2022-02-28)

### Features

* basic division into
  apps ([788175c](https://github.com/dominikbullo/ShareDesk/commit/788175c5bb732a51c025ed24af2e6e82b3e557af))
* basic log/reg with
  DRF&JWT ([9a70304](https://github.com/dominikbullo/ShareDesk/commit/9a70304d073a4b62851db08f4bee61faf8ca750e))
* **db:** new db
  structure ([ecc1c89](https://github.com/dominikbullo/ShareDesk/commit/ecc1c891c73b3bd0bfb974d650aee1ec62911797))
* JWT implemented ([7197b70](https://github.com/dominikbullo/ShareDesk/commit/7197b70894394596e3b337aa018dd835ccf4d631))
* login with additional data passed to
  FE ([9cb3a43](https://github.com/dominikbullo/ShareDesk/commit/9cb3a435405ed78f2b8614af04f9a3093f2bde13))
* login/logout ([966aaba](https://github.com/dominikbullo/ShareDesk/commit/966aabad12bc22abef204b27504fa5a154e87fd5))
* login/logout ([a50f1df](https://github.com/dominikbullo/ShareDesk/commit/a50f1dfcf93cb62d2905ca4c7f0a67701d350835))
* Teams app
  basics ([3237d61](https://github.com/dominikbullo/ShareDesk/commit/3237d616ee25d117891ec5e4a1bb3f188c8f2322))

### Bug Fixes

* urls working
  correctly ([9f2233f](https://github.com/dominikbullo/ShareDesk/commit/9f2233facc57eae2291e53ff06f83263eb21ad8c))
