aws s3api put-bucket-website --bucket home.urawizard.com --website-configuration file://redirects_none.json && \
./invalidate_cache.sh