./get_current_cloudfront_conf.sh

# ADD the Cloudfront Lambda Function Association for the maintenance page
ETAG=`jq -r '.ETag' ./cloudfront.json`
 
aws cloudfront update-distribution --if-match $ETAG --id EX58XM8KBBXH9 --distribution-config file://cloudfront_with_maintenance.json