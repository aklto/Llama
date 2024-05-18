FROM pytorch/pytorch:latest

RUN pip install transformers

COPY . .

WORKDIR /app

CMD ["python", "model.py"]
