FROM python:3-alpine


COPY ./config /root/.kube/config



COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

#EXPOSE 5000
ENTRYPOINT [ "python3" ]

CMD [ "api.py" ]