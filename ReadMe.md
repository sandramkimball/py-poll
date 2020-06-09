# py-poll

In command prompt: 
    - " python3 -m pip install pipenv "
    - " python3 -m pipenv install django "
    - " django-admin startproject pyPoll "
    - " cd pyPoll "
    - " python3 manage.py runserver 3001 " --this will create db.sqlite3 file
    - " python3 manage.py startapp pyPoll

Other:
    - " python3 manage.py makemigrations polls "
    - " python3 manage.py migrate "

Create data in terminal
    - "python3 manage.py shell"
    - "from polls.models import Question, Choice"
    - "Question.objects.all()"
    - "q = Question(question_text='blah?', pub_date='blah')
    - "q.save()"
    - "ch = Choice(question='1', choice_text='blah blah')