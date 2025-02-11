FROM python:3.9-slim

ENV APP_USER gamja
ENV APP_PORT 8000

RUN adduser --disabled-password $APP_USER
WORKDIR /app
COPY deploy /app

COPY deploy/requirements.txt .
RUN pip install -r requirements.txt

USER $APP_USER
EXPOSE $APP_PORT

ENTRYPOINT ["python"]
CMD ["app.py"]
