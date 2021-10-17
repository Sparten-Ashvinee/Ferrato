#Creating Docker Image

```
sudo apt-get update
```

```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

```

```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  bionic stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```


```
sudo apt-get update
```

```
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

```
apt-cache madison docker-ce
```

```
sudo apt-get install docker-ce=5:18.09.0~3-0~ubuntu-bionic docker-ce-cli=5:18.09.0~3-0~ubuntu-bionic containerd.io
```

Create Dockerfile
```
FROM huggingface/transformers-pytorch-cpu:latest
COPY ./ /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

```
sudo docker build -t ferrato:latest .
```

To remove all the unused or incomplete docker images
```
sudo docker system prune
```

Docker container

```
docker run -p 8000:8000 --name inference_container inference:latest
```


docker-compose.yml
```
version: '3'
services:
  prediction_api:
    build: .
    container_name: 'ferrato_container'
    ports:
      - '8000:8000'
```

Install Docker Compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

```
sudo chmod +x /usr/local/bin/docker-compose
```

```
docker-compose --version
```

```
sudo docker-compose up
```