FROM python:latest
COPY /app .
ENV FLASK_APP=app
ENV FLASK_ENV=development
RUN pip install flask && pip install PyMySQL
EXPOSE 5000
CMD ["flask","run","--host=0.0.0.0"]
