# contrived.name on AWS

bucket name: home.urawizard.com

## Install the AWS CLI

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

## Deploy the static site to S3 + Cloudfront

See /home.urawizard/update.sh or (the entirely pending) hazel config

```
aws s3 sync <FILES> s3://contrived.name --delete
```
