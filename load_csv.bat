@echo off
set /p DB_PASSWORD="Enter a DB_PASSWORD: "
set MYSQL_PWD=%DB_PASSWORD%
python manage.py makemigrations
python manage.py migrate
type *.sql | mysql -u root 
mysqlimport --ignore-lines=1  --fields-terminated-by=,  --local -u root fish_db  fishes_table.csv