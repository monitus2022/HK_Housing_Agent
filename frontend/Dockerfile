FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY . /app/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "main.py", \
"--server.port=${STREAMLIT_SERVER_PORT}", \
"--server.address=${STREAMLIT_SERVER_ADDRESS}", \
"--server.headless=${STREAMLIT_SERVER_HEADLESS}"]