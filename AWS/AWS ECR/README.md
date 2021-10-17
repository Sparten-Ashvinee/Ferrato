#AWS ECR

> This step after creating docker image for storing the image to AWS


```
sudo aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 734592791604.dkr.ecr.us-east-2.amazonaws.com
```

> Run this command if you face any problem while authenticating
> ```
> chmod 777 /var/run/docker.sock
> ```


```
docker tag ferrato:test 734592791604.dkr.ecr.us-east-2.amazonaws.com/ferrato-ecr:latest
``` 

```
docker push 734592791604.dkr.ecr.us-east-2.amazonaws.com/ferrato-ecr:latest
```
