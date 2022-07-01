
Test task for mains_lab: 
* `source run.sh install` - создаст виртуальное окружение, установит зависимости, применит миграции
* `run.sh run` - start server (или `python manage.py runserver`)



* `api/upload_org` - загрузка файла client_org.xlsx
* `api/upload_bills` - загрузка файла bills.xlsx
* `api/get_clients` - получение клиентов и кол-ва организаций
* `api/get_bills` - получение счетов с возможностью филтрации по полю client_org


** **
разработка и тестирование проводились на `mac_os(12.3.1)`.
