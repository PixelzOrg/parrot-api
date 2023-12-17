import * as cdk from 'aws-cdk-lib'
import { Construct } from 'constructs'
import { lambdaConfigs } from '../config/lambda-configs'
import { ApiGateway } from './api_gateway'
import { createLambdaFunction } from './lambdas'
import { addPoliciesToLambda } from './lambdas'

export class API extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    const api = new ApiGateway(this)

    for (const config of lambdaConfigs) {
      const lambdaFunction = createLambdaFunction(this, config)
      addPoliciesToLambda(lambdaFunction, config.policies)
      api.addIntegration(
        // @ts-ignore
        config.corsConfig.allowMethods[0],
        config.url,
        lambdaFunction
      )
    }
  }
}
