if [ $# -eq 0 ]; then
    echo "Usage:"
    echo "update.sh <deployment target>"
    exit 1
fi


echo "Deploying home.urawizard to $1..."

if [ $1 == "aws" ]; then
    echo Deploying to aws
    aws s3 sync site/ s3://home.urawizard.com --delete
    cd infra/aws/
    ./invalidate_cache.sh
    echo Deployed
else
    echo Deployment target not supported, sorry
    exit 1;
fi




