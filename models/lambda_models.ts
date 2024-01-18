import * as apigateway from '@aws-cdk/aws-apigateway'
import * as cdk from 'aws-cdk-lib'
import * as s3 from 'aws-cdk-lib/aws-s3'

import { ApiGatewayStack } from '../lib/api-gateway-stack'
import { S3BucketStack } from '../lib/s3-stack'
import { VpcStack } from '../lib/vpc-stack'

// LAMBDA CONFIG MODELS

export interface LambdaConfig {
  name: string
  url?: string
  queueName?: string
  path: string
  policy: Policy
  secrets: {
    [key: string]: string
  }
  corsConfig?: apigateway.CorsOptions
  s3Events?: s3.EventType[]
}

export interface Policy {
  actions: string[]
  resources: string[]
}

export interface LambdaStackProps extends cdk.StackProps {
  apiGatewayStack: ApiGatewayStack
  s3BucketStack: S3BucketStack
  vpcStack: VpcStack
}

export function verifyLambdaConfig(config: LambdaConfig): void {
  if (!config.policy) {
    throw new Error(`Lambda ${config.name} is missing policy`)
  }
  if (!config.path) {
    throw new Error(`Lambda ${config.name} is missing path`)
  }
  if (!config.name) {
    throw new Error(`Lambda is missing name`)
  }
}
