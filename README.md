<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-passwordless-auth.svg?longCache=True)](https://pypi.org/project/django-passwordless-auth/)
[![](https://img.shields.io/pypi/v/django-passwordless-auth.svg?maxAge=3600)](https://pypi.org/project/django-passwordless-auth/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/django-passwordless-auth.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/django-passwordless-auth.py/)

#### Installation
```bash
$ [sudo] pip install django-passwordless-auth
```

#### Examples
`settings.py`
```python
AUTHENTICATION_BACKENDS = (
    'django_passwordless_auth.backend.PasswordlessAuthBackend',
)
```

`views.py`
```python
from django.contrib.auth import login

def view(request):
    ...
    login(request, user, backend='django_passwordless_auth.backend.PasswordlessAuthBackend')
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>