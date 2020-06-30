import setuptools

setuptools.setup(
    name='django-passwordless-auth',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
