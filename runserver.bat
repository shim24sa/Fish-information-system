@echo off 
for /f "tokens=1-2 delims=:" %%a in ('ipconfig^|findstr "IPv4"') do set local_ip=%%b
python manage.py runserver  %local_ip%:3000