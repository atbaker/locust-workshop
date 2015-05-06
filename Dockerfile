FROM python:2.7.7-onbuild

EXPOSE 8089

CMD [ "locust" ]
