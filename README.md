# CDKServerlessWebsite 
# Static site

##This is a Serverless Web App with AWS CDK packaged together in a way that you can deploy the starter application to s3.


This example creates the infrastructure for a static site, which uses an S3 bucket for storing the content.  The site contents (located in the 'app.py')

The site redirects from HTTP to HTTPS, using a CloudFront distribution, Route53 alias record, and ACM certificate.
It is serverless, the backend utilizies AWS DynamoDB and Lambda, which communicate through API Gateway


## Prep

The domain for the static site (i.e. mystaticsite.com) must be configured as a hosted zone in Route53 prior to deploying this example.  For instructions on configuring Route53 as the DNS service for your domain, see the [Route53 documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring.html).

## DEPLOYMENT MIGHT NOT WORK OUT OF THE BOX, MINOR CONFIG CHANGES MIGHT NEED TO BE MADE FIRST!!!

## Deploy


```
$ npm install -g aws-cdk
$ cdk synth
$ cdk deploy -c domain=mystaticsite.com -c subdomain=www
```



