# Example API with Django and Django Rest Framework

This API is a representation of prescription and progrmation model. Based of MIPRESS
<https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/OT/Documentacion-web-services-V-3.1.pdf>

## Steps required to start the application

1.  It is recommended to use **Python 3.4** or higher
2.  Install the packages contained in **requirements.txt** using the command    installation of `pip install -r requirements.txt`
3.  Execute the run.py file with `python manage.py makemigrations`
4.  Execute the run.py file with `python manage.py migrate`
5.  Execute the run.py file with `python manage.py runserver`
6.  Open the browser and go to the address <http://localhost:8000/> or <http://127.0.0.1:8000/>

---

# Test whit Insomnia 
### <https://insomnia.rest/>

## Generate Token
### <https://apimipres.herokuapp.com/api_generate_token/>

```
{
  "username": "admin"
  ,
  "password": "12345678"
}
```

## Get Addressing for date 
### <https://apimipres.herokuapp.com/api/addressdate/>

### Header
```
date: 2019-09-25
token: token_generate
nit: 87654321
```

## Get Addressing for prescription number
### <https://apimipres.herokuapp.com/api/addressprescription/>

### Header
```
noPrescripcion: 20190727183013425426
token: token_generate
nit: 87654321
```


## Get Addressing for document
### <https://apimipres.herokuapp.com/api/addressdocument/>

### Header
```
tipodoc: CC
token: token_generate
nit: 87654321
numdoc: 28565084
```

## Get Addressing for document
### <https://apimipres.herokuapp.com/api/addressdocument/>

### Header
```
tipodoc: CC
token: token_generate
nit: 87654321
numdoc: 28565084
```

