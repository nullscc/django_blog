git pull
git submodule update
echo yes | python manage.py collectstatic
supervisorctl reread
supervisorctl restart django_blog
