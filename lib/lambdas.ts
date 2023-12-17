import { PolicyStatement } from 'aws-cdk-lib/aws-iam'
import { LambdaConfig } from '../models/lambdas'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import { Policy } from '../models/lambdas'
import * as cdk from 'aws-cdk-lib'

export function createLambdaFunction(
  stack: cdk.Stack,
  config: LambdaConfig
): lambda.DockerImageFunction {
  return new lambda.DockerImageFunction(stack, config.name, {
    code: lambda.DockerImageCode.fromImageAsset(config.path),
    timeout: cdk.Duration.seconds(10),
    architecture: lambda.Architecture.ARM_64,
  })
}

export function addPoliciesToLambda(
  lambdaFunction: lambda.DockerImageFunction,
  policies: Policy[]
): void {
  if (policies) {
    for (const policy of policies) {
      lambdaFunction.addToRolePolicy(
        new PolicyStatement({
          actions: policy.actions,
          resources: policy.resources,
        })
      )
    }
  }
}
