FROM python:3.9

WORKDIR /code

RUN mkdir -p /code/images

COPY ./requirements.txt /code/

RUN pip install -r requirements.txt

COPY ./volcan /code/volcan

# Добавляем src в PYTHONPATH
ENV PYTHONPATH=/code/volcan

# Запускаем как модуль
CMD ["python", "-m", "volcan"]
