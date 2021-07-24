FROM python:3.7

COPY ./services/tgbot /english-bot/tgbot
COPY ./config /english-bot/config

WORKDIR /english-bot

RUN pip3 install -r /english-bot/tgbot/requirements.txt

ENV RUN_IN_DOCKER 1
ENV PYTHONPATH "."
ENTRYPOINT ["python3"]

CMD ["tgbot/bot.py"]
