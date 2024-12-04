# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Define environment variable
COPY ./test_pandas.py /test_pandas.py

RUN pip install pandas

CMD [ "python", "/test_pandas.py" ]
