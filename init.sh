#! /bin/sh

file=db.sqlite3
if [ -e "$file" ]; then
    rm $file
fi

echo "SECRET_KEY='TemporarySEcrtetKey3rb%&TGDW&E*#(**(EHU#(*E'" > .env
echo "app_env='prod'" >> .env

python manage.py collectstatic --noinput

python manage.py migrate

user=admin
email=admin@mail.com
password=Admin123_#

echo "from django.contrib.auth import get_user_model; User=get_user_model(); User.objects.create_superuser('$user', '$email', '$password')"|python3 manage.py shell
