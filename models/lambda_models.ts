import * as apigateway from 'aws-cdk-lib/aws-apigateway'
import * as cdk from 'aws-cdk-lib'
import * as s3 from 'aws-cdk-lib/aws-s3'

import { ApiGatewayStack } from '../lib/api-gateway-stack'
import { S3BucketStack } from '../lib/s3-stack'

// LAMBDA CONFIG MODELS

export interface LambdaConfig {
  name: string
  authorizer?: boolean
  url?: string
  queueName?: string
  path: string
  policy?: Policy
  secrets: {
    [key: string]: string
  }
  corsConfig?: apigateway.CorsOptions
  eventSource?: {
    events: s3.EventType[]
    filters: s3.NotificationKeyFilter[]
  }
  bucketName?: string
}

export interface Policy {
  actions: string[]
  resources: string[]
}

export interface LambdaStackProps extends cdk.StackProps {
  apiGatewayStack: ApiGatewayStack
  s3BucketStack: S3BucketStack
}

export function verifyLambdaConfig(config: LambdaConfig): void {
  if (!config.path) {
    throw new Error(`Lambda ${config.name} is missing path`)
  }
  if (!config.name) {
    throw new Error(`Lambda is missing name`)
  }
}
