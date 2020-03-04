# django-datapeace

Set up:

1. Setup virtual environment.
2. Install requirements: pip install -r requirements.txt
3. Run server: python manage.py runserver

Runnig Tests:
1. To run test: python manage.py test


Notes:

1. The project uses sqlite db becuase the purpose of this project is for demo/assignment and it sqldb requires not additional setup requirements.
2. The default limit/pagesize of list is set to 5. The spec document of the assignment has two default values of a list and it was confusing. So I kept it 5.
3. There are no authencation/authorization on REST endpoint because it was not mentioned in spec document.
