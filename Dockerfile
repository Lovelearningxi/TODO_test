FROM python:3.6
RUN pip install requirements.txt
COPY app.py /app/
WORKDIR /app
CMD python app.py