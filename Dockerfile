FROM python:3.7

WORKDIR /app

COPY . /app

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple  --upgrade pip
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt


EXPOSE 5050


CMD ["python3","app.py"]