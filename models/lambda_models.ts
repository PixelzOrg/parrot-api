import * as lambda from '@aws-cdk/aws-lambda'
import * as apigateway from '@aws-cdk/aws-apigateway'

export interface LambdaConfig {
  type: string
  name: string
  url?: string
  path: string
  authType: lambda.FunctionUrlAuthType
  policy?: Policy
  corsConfig?: apigateway.CorsOptions
  secrets: {
    [key: string]: string
  }
  kinesisStream?: string
}

export interface Policy {
  actions: string[]
  resources: string[]
}

type ConfigVerificationCallback = (config: LambdaConfig) => void

export const verifyLambdaConfig: ConfigVerificationCallback = (config) => {
  if (!config) {
    throw new Error('Config is required to create API Lambda Function')
  }
  if (!config.name) {
    throw new Error('Name is required to create API Lambda Function')
  }
  if (!config.type) {
    throw new Error('Type is required to create API Lambda Function')
  }
  if (!config.authType) {
    throw new Error('Auth Type is required to create API Lambda Function')
  }
  if (!config.corsConfig) {
    throw new Error('CORS Config is required to create API Lambda Function')
  }
  if (!config.corsConfig.allowHeaders) {
    throw new Error('You must specify at least one header to allow CORS')
  }
}
