import * as lambda from '@aws-cdk/aws-lambda'
import * as apigateway from '@aws-cdk/aws-apigateway'

export interface LambdaConfig {
  name: string
  url: string
  path: string
  authType: lambda.FunctionUrlAuthType
  policies: Policy[]
  corsConfig: apigateway.CorsOptions
  secrets: {
    [key: string]: string
  }
}

export interface Policy {
  actions: string[]
  resources: string[]
}
