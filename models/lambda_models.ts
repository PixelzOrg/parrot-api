import * as lambda from '@aws-cdk/aws-lambda'
import * as apigateway from '@aws-cdk/aws-apigateway'
import { KinesisConfig } from './kinesis_models'

export interface LambdaConfig {
  type: string
  name: string
  url?: string
  path?: string
  authType?: lambda.FunctionUrlAuthType
  policies?: Policy[]
  corsConfig?: apigateway.CorsOptions | null
  secrets?: {
    [key: string]: string
  }
  kinesisStream?: string
}

export interface Policy {
  actions: string[]
  resources: string[]
}
