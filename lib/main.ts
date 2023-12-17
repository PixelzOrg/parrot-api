import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import { Construct } from 'constructs';
import { lambdaConfigs } from '../config/lambda-configs';
import { LambdaConfig } from '../models/lambdas';
import { ApiGateway } from './api_gateway';
import { PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { Policy } from '../models/lambdas';

export class API extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const api = new ApiGateway(this);

    for (const config of lambdaConfigs) {
      const lambdaFunction = createLambdaFunction(this, config);
      addPoliciesToLambda(lambdaFunction, config.policies);
      // @ts-ignore
      api.addIntegration(config.corsConfig.allowMethods[0], config.url, lambdaFunction);
    }
  }
}

function createLambdaFunction(stack: cdk.Stack, config: LambdaConfig): lambda.DockerImageFunction {
  return new lambda.DockerImageFunction(stack, config.name, {
    code: lambda.DockerImageCode.fromImageAsset(config.path),
    timeout: cdk.Duration.seconds(10),
    architecture: lambda.Architecture.ARM_64,
  });
}

function addPoliciesToLambda(lambdaFunction: lambda.DockerImageFunction, policies: Policy[] | undefined): void {
  if (policies) {
    for (const policy of policies) {
      lambdaFunction.addToRolePolicy(
        new PolicyStatement({
          actions: policy.actions,
          resources: policy.resources,
        }),
      );
    }
  }
}