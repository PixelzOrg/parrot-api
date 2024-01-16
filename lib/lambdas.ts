import * as cdk from 'aws-cdk-lib'
import * as lambda from 'aws-cdk-lib/aws-lambda'

import { ApiGateway } from './api_gateway'
import { PolicyStatement } from 'aws-cdk-lib/aws-iam'
import { Policy } from '../models/lambda_models'
import { lambdaConfigs } from '../config/lambda-configs'
import { verifyLambdaConfig } from '../models/lambda_models'

export function loadLambdaFunctions(stack: cdk.Stack, api: ApiGateway): void {
  for (const config of lambdaConfigs) {
    verifyLambdaConfig(config)
    const lambdaFunction = createLambdaFunction(
      stack,
      config.name,
      config.path,
      config.secrets
    )
    if (config.policy) {
      addPoliciesToLambda(lambdaFunction, config.policy)
    }
    if (config.type === 'api') {
      api.addIntegration(
        // @ts-ignore
        config.corsConfig.allowMethods[0],
        // @ts-ignore
        config.url,
        lambdaFunction
      )
    }
  }
}

export function createLambdaFunction(
  stack: cdk.Stack,
  name: string,
  path: string,
  secrets: Record<string, string>
): lambda.DockerImageFunction {
  return new lambda.DockerImageFunction(stack, name, {
    code: lambda.DockerImageCode.fromImageAsset(path),
    timeout: cdk.Duration.seconds(10),
    architecture: lambda.Architecture.ARM_64,
    environment: secrets,
  })
}

export function addPoliciesToLambda(
  lambdaFunction: lambda.DockerImageFunction,
  policy: Policy
): void {
  console.log(lambdaFunction.functionName, policy)
  lambdaFunction.addToRolePolicy(
    new PolicyStatement({
      actions: policy.actions,
      resources: policy.resources,
    })
  )
}
/*
export function addKinesisStreamToLambda(
  lambdaFunction: lambda.DockerImageFunction,
  kinesisStreamName: string,
  fileProcessingStages: FileProcessingStages
): void {
  // Define a mapping of Kinesis stream names to their respective stream objects
  const stages: Record<string, kinesis.Stream> = {
    WhisperStage: fileProcessingStages.WhisperStage,
    VisionStage: fileProcessingStages.VisionStage,
    ChatGPTSummaryStage: fileProcessingStages.ChatGPTSummaryStage,
  }

  // Get the Kinesis stream object based on the stream name
  const kinesisStream = stages[kinesisStreamName]

  if (!kinesisStream) {
    throw new Error(`Kinesis stream with name '${kinesisStreamName}' not found`)
  }

  // Add an event source mapping to the Lambda function
  lambdaFunction.addEventSourceMapping(`${kinesisStreamName}EventSource`, {
    eventSourceArn: kinesisStream.streamArn,
    batchSize: 1,
    startingPosition: lambda.StartingPosition.TRIM_HORIZON,
  })
}

export function createKinesisLambdaRole(
  scope: cdk.Stack,
  kinesisStream: string,
  fileProcessingStages: FileProcessingStages,
  policies: Policy[]
): iam.Role {
  if (!policies) {
    throw new Error('Policies are required to add Policies to Lambda')
  }

  const stages: Record<string, string> = {
    WhisperStage: fileProcessingStages.WhisperStage.streamArn,
    VisionStage: fileProcessingStages.VisionStage.streamArn,
    ChatGPTSummaryStage: fileProcessingStages.ChatGPTSummaryStage.streamArn,
  }

  const kinesisStreamArn: string = stages[kinesisStream]

  // Create a new IAM role
  const role = new iam.Role(scope, 'KinesisLambdaRole', {
    assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
  })
  for (const policy of policies) {
    addRoleToPolicy(role, policy, [kinesisStreamArn])
  }

  return role
}
*/
