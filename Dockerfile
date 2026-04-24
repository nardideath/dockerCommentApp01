FROM python:3.12.13

WORKDIR /app

RUN apt-get update
RUN apt-get -y install sed attr dialog bash bash-doc bash-completion grep nano net-tools iputils-ping sshpass
RUN apt-get -y install libffi-dev gcc python3-dev python3-pip musl-dev libssl-dev cargo make rsync build-essential postgresql-server-dev-all

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"] 
