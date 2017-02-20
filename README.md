# Step 00. Setup Requirements

We need to first create a Django application. I assume that you have everything all setup from Step 00. We let Django take care of creating our skeleton app.

```python
django-admin startproject djangoreactstarter
```

We need to create `requirements.txt` and put `Django==1.10.5`. Pip is similar to `package.json`. Here is some documentation about pip.

To verify that this step works, run `python manage.py runserver` in the root folder and you should be able to see a welcome screen in `http://localhost:8000`

Step 01

