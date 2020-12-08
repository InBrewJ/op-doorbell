aws cloudformation deploy --template-file ./s3-bucket.yml --stack-name contrived-name-hosting-bucket --parameter-overrides BucketName=contrived.name;

aws cloudformation deploy --template-file ./cf-dist.yml --stack-name contrived-name-cloudfront-0