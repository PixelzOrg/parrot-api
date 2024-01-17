#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib'

import { ApiGateway } from '../lib/api-gateway-stack'
import { S3BucketStack } from '../lib/s3-stack'
import { LambdaStack } from '../lib/lambda-stack'
import { RdsStack } from '../lib/rds-stack'

const app = new cdk.App()

// Instantiate the RDS Stack
const rdsStack = new RdsStack(app, 'RDSStack', {})

// Instantiate the S3 Bucket Stack
const s3BucketStack = new S3BucketStack(app, 'S3BucketStack', {})

// Instantiate the API Gateway Stack
const apiGatewayStack = new ApiGateway(app, 'ApiGatewayStack', {})

// Instantiate the Lambda Stack
const lambdaStack = new LambdaStack(app, 'LambdaStack', apiGatewayStack, {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
})

apiGatewayStack.addDependency(lambdaStack)
