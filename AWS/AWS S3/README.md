#AWS S3 Bucket

> Learn how to create AWS S3 bucket and fetch data using DVC


Install the AWS CLI version 2 on Linux
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Check version
```
/usr/local/bin/aws --version
 ```

Configure AWS CLI
```
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json
```

Creating S3 bucket
```
aws s3api create-bucket --bucket my-bucket --region ussudo docker system prune-east-1
```

<p align="center">
  <img style="width:26rem; height:auto" src="https://github.com/Sparten-Ashvinee/Ferrato/blob/8bb79ec32f2bae3cc8290384bd5ef396a8eb0d26/imgs/DVC.png"/>
</p>


Adding S3 bucket to DVC
```
dvc remote add -d awsbucket s3://ferrato
export AWS_ACCESS_KEY_ID='mykey'
export AWS_SECRET_ACCESS_KEY='mysecret'
dvc push
```


Adding files to AWS S3 bucket
```
dvc add ../Data/similar_ingredients.csv --file similar_ingredients.dvc
dvc push
git add dvcfiles/similar_ingredients.dvc Data/.gitignore
git commit -m "Added all data files in AWS S3 bucket using dvc"
git push
```

Download all data
```
dvc pull
```
> Need to setup AWS S3 bucket to download all dataset



All DVC files

```
dvc dag
```
Output:
```
+-----------------------------------+  
| dvcfiles/all_ingredients_name.dvc |  
+-----------------------------------+  
+--------------------+ 
| dvcfiles/model.dvc | 
+--------------------+ 
+-----------------------------------------------+  
| dvcfiles/breakfast_ingredients_835_final6.dvc |  
+-----------------------------------------------+  
+-----------------+  
| dvcfiles/bf.dvc |  
+-----------------+  
+-------------------------------------------+  
| dvcfiles/breakfast_ingredients_all_v1.dvc |  
+-------------------------------------------+  
+----------------------------------+ 
| dvcfiles/similar_ingredients.dvc | 
+----------------------------------+ 
```