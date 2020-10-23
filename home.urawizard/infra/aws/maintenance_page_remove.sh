./get_current_cloudfront_conf.sh

# REMOVE the Cloudfront Lambda Function Association for the maintenance page
ETAG=`jq -r '.ETag' ./cloudfront.json`

aws cloudfront update-distribution --if-match $ETAG --id EX58XM8KBBXH9 --distribution-config file://cloudfront_without_maintenance.json