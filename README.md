# Step 2. Adding Django Views

We will now some Django views that Django will render and serve to the client. This is known as server side rendering. React-Redux has done a phenomenal job at replacing these "legacy server side views".

First we add in the `urls.py`:

```python
from django.conf.urls import url
from django.contrib import admin
from django.views import generic

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', generic.TemplateView.as_view(template_name='index.html')),
]
```

Next create a folder in your app called `templates` and make a `index.html` file. In that file, add some HTML:
```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
  </head>
  <body>
    <h3> This is a Django rendered view</h3>
  </body>
</html>
```

If you are successful with this step, you should be able to run `python manage.py runserver` and go to `http://localhost:8000` and be able to see the HTML we created.

Next, we will add webpack to get ready to add React into our project. See you in the next step. 

Step 3: Webpack Loader

