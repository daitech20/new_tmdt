FROM python:3.8

# Update APT
RUN apt-get update

# Make work directory
RUN mkdir /app
WORKDIR /app

# Install required packaged for Dijango projects
COPY ./server/requirements.txt ./server/requirements.txt
RUN pip install -r ./server/requirements.txt

# Clone source code
COPY . .

# Expose Dijango Server Port
EXPOSE 8000

# Start webserver
CMD ["python", "server/manage.py", "runserver", "0.0.0.0:8000"]