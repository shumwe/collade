#! /bin/sh

file=db.sqlite3
if [ -e "$file" ]; then
    rm $file
fi

user=bravin
email=admin_bravin@mail.com
password=Bravin123#

python manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('$user', '$email', '$password')"|python3 manage.py shell