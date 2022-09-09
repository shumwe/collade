#! /bin/sh

file=db.sqlite3
if [ -e "$file" ]; then
    rm $file
fi

user=admin
email=admin@mail.com
password=Admin123_#

python manage.py migrate

echo "from django.contrib.auth import get_user_model; User=get_user_model(); User.objects.create_superuser('$user', '$email', '$password')"|python3 manage.py shell
