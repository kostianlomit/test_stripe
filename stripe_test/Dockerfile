FROM python:3.10

RUN mkdir /stripe_test

WORKDIR /stripe_test

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh
