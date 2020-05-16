[program:course]
command=/Users/felix/PycharmProjects/DjangoSchoolYoutube/CourseDjango2/gunicorn config.wsgi:application -c /Users/felix/PycharmProjects/DjangoSchoolYoutube/CourseDjango2/config/gunicorn.conf.py
directory=/Users/felix/PycharmProjects/DjangoSchoolYoutube/CourseDjango2
user=USER
autorestart=true
redirect_stderr=true
stdout_logfile = /Users/felix/PycharmProjects/DjangoSchoolYoutube/CourseDjango2/logs/debug.log
