# COMP


Install instructions
--------------------

**Database**
1. For install: See DATABASE.md
2. Database is created with the following command:
```
export DATABASE_USER=YOUR_USERNAME_HERE && source ./webapp_env.sh
```
Note: your user name is your computer "username":
`USER-MacBook-Pro:COMP username$`

**Build & Activate Python Environment**

```
./python_env.sh
```

```
source activate comp-dev
```

**Set stripe and email keys**
TODO: app should run without these.
```
./secret.sh
```

**Django setup**
```
python manage.py migrate
python manage.py collectstatic
```
**Run Django server**
```
python manage.py runserver
```

**Run tests**
```
py.test webapp/apps -v
```

**Docker**
Note: this is only necessary if you want to run the backend workers. The frontend works just fine without this component.
1. Install the stable community edition of Docker. Install the version that
corresponds to your operating system from this [page](https://docs.docker.com/install/).
Make sure the docker app is running. You should see a whale icon in your
toolbar. If you are not on a Mac, see the [docker-compose installation page](https://docs.docker.com/compose/install/)
for information on how to set this up on your operating system.
2. Export the image tag that you want to use: `export TAG=dev`
Build the images: `make dist-build`
Navigate to `COMP/distributed` directory and run: `docker-compose up`
