#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib'

import { ApiGatewayStack } from '../lib/api-gateway-stack'
import { DynamoDbStack } from '../lib/dynamo-db'
import { LambdaStack } from '../lib/lambda-stack'
import { S3BucketStack } from '../lib/s3-stack'

const app = new cdk.App()
// Here we instantiate the stacks that we will be using
// Across the application we will be using the following stacks:
// 1. DynamoDB Stack           (Cache/Database) (IN USE)
// 2. S3 Bucket Stack     (Cache/Database) (IN USE)
// 3. API Gateway Stack   (Gateway) (IN USE)
// 4. Lambda Stack        (API/Services) (IN USE)
// 5. Cloudfront Stack    (Serving) (TODO:)
// 6. Route53 Stack       (Domain) (TODO:)

const defaultAccount = process.env.CDK_DEFAULT_ACCOUNT as string
const defaultRegion = process.env.CDK_DEFAULT_REGION as string


// Instantiate the DynamoDB Stack
const dynamoDbStack = new DynamoDbStack(app, 'DynamoDbStack', {
  env: {
    account: defaultAccount,
    region: defaultRegion,
  },
})
// Instantiate the S3 Bucket Stack
const s3BucketStack = new S3BucketStack(app, 'S3BucketStack', {
  env: {
    account: defaultAccount,
    region: defaultRegion,
  },
})
// Instantiate the API Gateway Stack
const apiGatewayStack = new ApiGatewayStack(app, 'ApiGatewayStack', {
  env: {
    account: defaultAccount,
    region: defaultRegion,
  },
})
// Instantiate the Lambda Stack
const lambdaStack = new LambdaStack(app, 'LambdaStack', {
  apiGatewayStack: apiGatewayStack,
  env: {
    account: defaultAccount,
    region: defaultRegion,
  },
  s3BucketStack: s3BucketStack,
})
