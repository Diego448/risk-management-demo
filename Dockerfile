FROM python:3.8-buster
WORKDIR /risk-management-demo
COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt
COPY . .
CMD [ "python", "-m", "flask", "run", "--host", "0.0.0.0"]