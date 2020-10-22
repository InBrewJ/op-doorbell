# home.urawizard on AWS

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
aws s3 sync <FILES> s3://home.urawizard.com --delete
```

## Add the redirect rule to always show maintenance.html

- CLI docs:
  https://docs.aws.amazon.com/cli/latest/reference/s3api/put-bucket-website.html

```
aws s3api put-bucket-website --bucket home.urawizard.com --website-configuration ./redirects.xml
```

## Docs

LOADSA HELP:
https://forestry.io/blog/automate-your-static-hosting-environment-with-aws-cloudformation/

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-s3.html
- qhttps://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-cloudfront.html#scenario-cloudfront-s3origin

AND

https://medium.com/swlh/aws-website-hosting-with-cloudformation-guide-36cac151d1af

Loads of help from:

- https://medium.com/@ryanjyost/deploy-react-apps-to-aws-part-3-create-a-hosting-s3-bucket-with-cloudformation-16a1125d2ad6

Also a great example here:

- https://github.com/sjevs/cloudformation-s3-static-website-with-cloudfront-and-route-53
