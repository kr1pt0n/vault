FROM python:3.11-slim
WORKDIR /app
COPY main.py .
COPY index.html .
RUN pip install --no-cache-dir fastapi uvicorn pydantic pyjwt python-multipart
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
