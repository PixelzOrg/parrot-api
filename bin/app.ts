#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib'

import { ApiGatewayStack } from '../lib/api-gateway-stack'
import { DynamoDbStack } from '../lib/dynamo-db'
import { LambdaStack } from '../lib/lambda-stack'
import { S3BucketStack } from '../lib/s3-stack'
import { SqsStack } from '../lib/sqs-stack'

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

console.log('Starting Stacks...')

// Instantiate the DynamoDB Stack
console.log('Started DynamoDbStack...')
const dynamoDbStack = new DynamoDbStack(app, 'DynamoDbStack', {
  env: {
    account: defaultAccount,
    region: defaultRegion,
  },
})
console.log(`Started stack: ${dynamoDbStack.stackName}`)

// Instantiate the SQS Stack
console.log('Starting SqsStack...')
const sqsStack = new SqsStack(app, 'SqsStack', {
  env: {
    account: defaultAccount,
    region: defaultRegion,
  },
})
console.log(`Started stack: ${sqsStack.stackName}`)

// Instantiate the S3 Bucket Stack
console.log('Starting S3BucketStack...')
const s3BucketStack = new S3BucketStack(app, 'S3BucketStack', {
  env: {
    account: defaultAccount,
    region: defaultRegion,
  },
})
console.log(`Started stack: ${s3BucketStack.stackName}`)

// Instantiate the API Gateway Stack
console.log('Starting ApiGatewayStack...')
const apiGatewayStack = new ApiGatewayStack(app, 'ApiGatewayStack', {
  env: {
    account: defaultAccount,
    region: defaultRegion,
  },
})
console.log(`Started stack: ${apiGatewayStack.stackName}`)

// Instantiate the Lambda Stack
console.log('Starting LambdaStack...')
const lambdaStack = new LambdaStack(app, 'LambdaStack', {
  apiGatewayStack: apiGatewayStack,
  env: {
    account: defaultAccount,
    region: defaultRegion,
  },
  s3BucketStack: s3BucketStack,
})
console.log(`Started stack: ${lambdaStack.stackName}`)
