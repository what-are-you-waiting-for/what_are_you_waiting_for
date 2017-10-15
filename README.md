This is what_are_we_waiting_for - an [Opal](https://github.com/openhealthcare/opal) project.

To get started, run the following commands:

```
    python manage.py migrate
    python manage.py runserver
```


Or if Opal is new to you:

mkvirtualenv hackday
workon hackday

pip install opal

pip install -r requirements.txt

./manage.py migrate

./manage.py createsuperuser

 ./manage.py load_lookup_lists
 
./manage.py runserver


go to http://localhost:8000

login as the superuser you just created.


If you get an error:

django.db.migrations.graph.NodeNotFoundError: Migration what_are_we_waiting_for.0001_initial dependencies reference nonexistent parent node (u'opal', u'0032_auto_20171014_1527')

rm what_are_we_waiting_for/opal.sqlite
./manage.py migrate
./manage.py runserver

If you get errors about module opal.pathway not found it is probably your version of python or environment, try with/without python2 or python3 on the abbove commands.

