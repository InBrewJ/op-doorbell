aws cloudformation deploy --template-file ./s3-bucket.yml --stack-name home-wizard-hosting-bucket --parameter-overrides BucketName=home.urawizard.com;

aws cloudformation deploy --template-file ./cf-dist.yml --stack-name home-urawizard-cloudfront-0