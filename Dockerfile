FROM python:3-alpine
COPY . /api
WORKDIR /api
RUN pip install -r ./requirements.txt
ENTRYPOINT ["python"]
CMD ["-u", "api.py"]
