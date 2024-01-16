import * as cdk from 'aws-cdk-lib'

import { loadLambdaFunctions } from './lambdas'
import { ApiGateway } from './api_gateway'
import { Construct } from 'constructs'
import { S3BucketStack } from './s3'

export class API extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    const api = new ApiGateway(this)
    const bucket = new S3BucketStack(this, 'S3 Bucket')
    const lambdas = loadLambdaFunctions(this, api)
  }
}
