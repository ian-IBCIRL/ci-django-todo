![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the readme for my first Django project.

The last update to this file was: **Dec 21, 2022**

## Gitpod Reminders

To install django, `pip3 install 'django<4'`

Use `python3 manage.py runserver` to launch web server

------

## Release History

We continually tweak and adjust this repository to help give you the best experience. 
Here is the version history:

**November 18 2022:** Initial release.

**Dec 21 2022:** Readme cleanup.

------

## FAQ about: 1) adding views and 2) initial config for env.py, and settings.py to keep things secure

**1) Adding Views**

three steps When adding views, remember to 
1) update views.py in the app folder `\todo in this case`
```
def say_hi(request):
    return HttpResponse("hello world !")
```

2) and then remember to import the relevant function into urls.py in `django_<app>` folder

```
from todo.views import say_hi, say_hi2, say_hitop
```

3) and update urlpatterns in urls.py
```
urlpatterns = [
    path('hi/', say_hi, name='hi'),
```


**2) initial config for env.py, and settings.py to keep things secure**

Note env py needed. e.g.
```
import os
os.environ.setdefault("S_K","74fxaa8t2lfyvdk-e7ok9_2+coc$1$p)g")
```

and settings py is:
```
import os
if os.path.isfile('env.py'):
    import env
```
# SECURITY WARNING: keep the secret key used in production secret!
```
SECRET_KEY = os.environ.get('SECRET_KEY')
```

and `python3 manage.py runserver` to launch web server

---

Happy coding!
