FROM pytorch/pytorch:latest

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install transformers

COPY . .

WORKDIR /app

CMD ["python", "model_handler.py"]
