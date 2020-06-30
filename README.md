<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-passwordless-auth.svg?maxAge=3600)](https://pypi.org/project/django-passwordless-auth/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-passwordless-auth.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-passwordless-auth.py/actions)

### Installation
```bash
$ [sudo] pip install django-passwordless-auth
```

#### Pros
+   3rd party/social authentication without password

#### Examples
`settings.py`
```python
# from django_passwordless_auth.settings import AUTHENTICATION_BACKENDS

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
    <a href="https://readme42.com/">readme42.com</a>
</p>