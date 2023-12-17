import * as cdk from 'aws-cdk-lib';
import * as lambda from "aws-cdk-lib/aws-lambda";
import { Construct } from 'constructs';
import { lambdaConfigs, LambdaConfig } from '../config/lambda-configs';
import { ApiGateway } from './api_gateway';
import { PolicyStatement } from 'aws-cdk-lib/aws-iam';

export class API extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const api = new ApiGateway(this)

    for (const config of lambdaConfigs) {
    /**
     * For each LambdaConfig, create a DockerImageFunction and add it to the API Gateway.
     * - The DockerImageFunction is created from an image asset in the lambda-functions directory.
     * - The function is named after the LambdaConfig, with spaces removed and all letters lowercased.
     * - The function is added to the API Gateway resource with the path specified in the LambdaConfig.
     */
      const lambdaFunction = new lambda.DockerImageFunction(this, config.name, {
        code: lambda.DockerImageCode.fromImageAsset(config.path),
        timeout: cdk.Duration.seconds(10),
        architecture: lambda.Architecture.ARM_64,
      });

      if (config.policies) {
        for (const policy of config.policies) {
          lambdaFunction.addToRolePolicy(
            new PolicyStatement({
              actions: policy.actions,
              resources: policy.resources,
            }),
          );
        }
      }
      // @ts-ignore
      api.addIntegration(config.corsConfig.allowMethods[0], config.url, lambdaFunction);
    }
  };
}
