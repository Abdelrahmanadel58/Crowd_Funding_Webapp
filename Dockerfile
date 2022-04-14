FROM python:3.7-slim
USER root
WORKDIR /application
RUN apt-get update
RUN apt-get install vim -y
RUN python -m pip install --upgrade pip
COPY . .
RUN pip3 install -r requirements.txt
RUN pip3 install django
RUN pip3 install bootstrap4
RUN pip3 install pillow
RUN pip3 install ajaxuploader
RUN python manage.py makemigrations
RUN python manage.py migrate
COPY request.py /usr/local/lib/python3.7/site-packages/django/http/request.py
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
