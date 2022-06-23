
FROM python:3.10.4
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
ADD entrypoint.sh /app
RUN chmod +x *.sh
CMD uwsgi --module=ArticleProject.wsgi --http=0.0.0.0:80