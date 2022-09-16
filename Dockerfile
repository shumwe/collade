FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
RUN sh init.sh

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "collade.asgi:application", "--host", "0.0.0.0", "--port", "8000"]