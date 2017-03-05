# Step 01. Creating the Django App

We will now create our first Django application. I assume that you have everything all setup from [Step 00](https://github.com/MikeTYChen/django-reactjs-starter/tree/step00-install-requirements). We let Django take care of creating our skeleton app.

```python
django-admin startproject djangoreactstarter
```
In our `.gitignore` file, you should add `*.pyc` and `db.sqlite3`.

To verify that this step works, run `python manage.py runserver` in the root folder and you should be able to see a welcome screen in `http://localhost:8000`

Step 02

