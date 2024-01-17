import * as apigateway from '@aws-cdk/aws-apigateway'
import * as lambda from '@aws-cdk/aws-lambda'
import * as cdk from 'aws-cdk-lib'

import { ApiGatewayStack } from '../lib/api-gateway-stack'
import { S3BucketStack } from '../lib/s3-stack'

// LAMBDA CONFIG MODELS

export interface LambdaConfig {
  name: string
  path: string
  authType: lambda.FunctionUrlAuthType
  policy: Policy
  secrets: {
    [key: string]: string
  }
}

export interface APILambdaConfig extends LambdaConfig {
  url: string
  corsConfig: apigateway.CorsOptions
}

export interface Policy {
  actions: string[]
  resources: string[]
}

export interface LambdaStackProps extends cdk.StackProps {
  apiGatewayStack: ApiGatewayStack
  s3BucketStack: S3BucketStack
  rdsVpcId: string
}

export function verifyApiLambdaConfig(config: APILambdaConfig): void {
  if (!config.authType) {
    throw new Error(`Lambda ${config.name} is missing authType`)
  }
  if (!config.policy) {
    throw new Error(`Lambda ${config.name} is missing policy`)
  }
  if (!config.corsConfig) {
    throw new Error(`Lambda ${config.name} is missing corsConfig`)
  }
  if (!config.url) {
    throw new Error(`Lambda ${config.name} is missing url`)
  }
  if (!config.path) {
    throw new Error(`Lambda ${config.name} is missing path`)
  }
  if (!config.name) {
    throw new Error(`Lambda ${config.name} is missing name`)
  }
}
