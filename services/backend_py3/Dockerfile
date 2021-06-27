FROM python:3.7

COPY ./services/backend_py3 /english-bot/backend_py3
COPY ./common /english-bot/common

RUN pip3 install -r /english-bot/backend_py3/requirements.txt

WORKDIR /english-bot/backend_py3

ENV RUN_IN_DOCKER 1
ENV FLASK_APP /english-bot/backend_py3/app.py

EXPOSE 8000
ENTRYPOINT ["python3"]

CMD ["-m", "flask", "run", "--host", "0.0.0.0", "--port", "8000"]
