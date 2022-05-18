FROM python:3

RUN pip install ddtrace

COPY server.py /

CMD ["python","server.py"]

