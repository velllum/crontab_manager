https://routerus.com/scheduling-cron-jobs-with-crontab/
https://hamsterden.ru/cron/

работать в режиме root

sudo su - ввести пароль

crontab -e — отредактировать файл crontab или создать его, если он еще не существует.
crontab -l — Показать содержимое файла crontab.
crontab -r — удалить текущий файл crontab.
crontab -i — удалить текущий файл crontab с запросом перед удалением.
crontab -u <username> — редактировать файл crontab другого пользователя. Эта опция требует прав системного


*/1 * * * * cd /home/pavel/PycharmProjects/mrgeng_flask && /home/pavel/PycharmProjects/mrgeng_flask/venv/bin/python3 run.py >> log.txt
0 23 * * * /home/pavel/PycharmProjects/mrgeng_flask && /home/pavel/PycharmProjects/mrgeng_flask/venv/bin/python3 run.py >> log.txt

chmod 750 run.py
which python3