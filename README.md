# Running The Application Locally

### (method 1) Clone and run

- Clone the repository
- Install dependancies ```   python -m pip install -r requirements.txt```
- Create the superuser ```   pythom manage.py createsuperuser ```
- Run   ```  python manage.py runserver 8000  ``` 
- populate the database via [Collade Admin](127.0.0.1:8000/admin) or console

### (method 2) Pull docker image

- Install and configure docker on your machine
- Pull my docker image ```   docker pull shumwe/collade   ```
- Run the image ```   docker run -d -p 8000:8000 collade:latest ```
- Visit [Collade Homepage](127.0.0.1:8000)  OR [Collade Admin](127.0.0.1:8000/admin)


# Contributors

```
Feel free to fork this repo and contribute
```