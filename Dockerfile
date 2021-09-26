FROM python:3
WORKDIR /app
COPY essai.py .
CMD ["python", "essai.py"]