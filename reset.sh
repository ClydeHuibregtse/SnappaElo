rm -rf ./elo/migrations
rm db.sqlite3

python3 manage.py makemigrations elo
python3 manage.py sqlmigrate elo 0001
python3 manage.py migrate
