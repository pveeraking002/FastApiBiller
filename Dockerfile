FROM python:3.10-slim

ENV PYTHONUNBUFFERED = True

WORKDIR /usr/src/app

COPY req.txt ./

RUN pip install --no-cache-dir -r req.txt 

COPY . . 

CMD ["uvicorn","main:app","--host","0.0.0.0", "--port", "8080"]





