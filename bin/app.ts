#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib'

import { ApiGatewayStack } from '../lib/api-gateway-stack'
import { LambdaStack } from '../lib/lambda-stack'
import { RdsStack } from '../lib/rds-stack'
import { S3BucketStack } from '../lib/s3-stack'

const app = new cdk.App()
// Here we instantiate the stacks that we will be using
// Across the application we will be using the following stacks:
// 1. RDS Stack           (Cache/Database) (IN USE)
// 2. S3 Bucket Stack     (Cache/Database) (IN USE)
// 3. API Gateway Stack   (Gateway) (IN USE)
// 4. Lambda Stack        (API/Services) (IN USE)
// 5. Ec2 Stack           (Services) (TODO:)
// 6. Cloudfront Stack    (Serving) (TODO:)
// 7. Route53 Stack       (Domain) (TODO:)

// Instantiate the RDS Stack
const rdsStack = new RdsStack(app, 'RDSStack', {})
// Instantiate the S3 Bucket Stack
const s3BucketStack = new S3BucketStack(app, 'S3BucketStack', {})
// Instantiate the API Gateway Stack
const apiGatewayStack = new ApiGatewayStack(app, 'ApiGatewayStack', {})
// Instantiate the Lambda Stack
const lambdaStack = new LambdaStack(app, 'LambdaStack', {
  apiGatewayStack: apiGatewayStack,
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
  rdsVpcId: cdk.Fn.importValue('RdsVpcId'),
  s3BucketStack: s3BucketStack,
})
