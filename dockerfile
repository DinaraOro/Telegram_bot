FROM python:3.10-slim
ENV TOKEN='твой токен'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]вщ