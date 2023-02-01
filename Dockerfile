FROM python:3
COPY . .
ENV FLASK_APP = app
EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
