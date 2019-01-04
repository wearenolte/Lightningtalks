# lightning.com

## Using Docker for Development

Create `.env` file used to set environment variables with some conf and secret 
credentials, this file is not versioned

Example Dev `.env` file
```
DEBUG=True
SECRET_KEY=my-super-secret-key
```

Build docker image
```
docker build -t lightning .
```

Run all services
```
docker-compose up
```

Stop all services
```
docker-compose down
```

## Other useful commands
Run bash shell on web service
```
docker-compose exec web bash
```

Execute migrations
```
docker-compose exec web python manage.py migrate
```
Create django superuser
```
docker-compose exec web python manage.py createsuperuser
```