import * as cdk from 'aws-cdk-lib'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as kinesis from 'aws-cdk-lib/aws-kinesis'
import * as iam from 'aws-cdk-lib/aws-iam'

import { lambdaConfigs } from '../config/lambda-configs'
import { Policy } from '../models/lambda_models'
import { LambdaConfig } from '../models/lambda_models'
import { FileProcessingStages } from './kinesis';

export const LoadLambdaFunctions = (
    stack: cdk.Stack, 
    fileProcessingStages: FileProcessingStages
  ) => {
    for (const config of lambdaConfigs) {
  
      if (config.type == 'api') {
        const apiRole: iam.Role = createApiLambdaRole(stack, config.name, config.policies ?? [])
        const lambdaFunction = createLambdaFunction(stack, config, apiRole)
        // @ts-ignore
        api.addIntegration(config.corsConfig.allowMethods[0], config.path ?? '', lambdaFunction)
      }

      if (config.type == 'pipeline') {
        // @ts-ignore
        const kinesisStream: string = config.kinesisStream
        const pipelineRole: iam.Role = createKinesisLambdaRole(stack, 
          'KinesisLambdaRole',
          config.kinesisStream ?? '',
          fileProcessingStages, 
          config.policies ?? [],
        )
        const lambdaFunction = createLambdaFunction(stack, config, pipelineRole)
        addKinesisStreamToLambda(lambdaFunction, kinesisStream, fileProcessingStages)
      }
    }
}

export function createLambdaFunction(
  stack: cdk.Stack,
  config: LambdaConfig,
  role: iam.Role
): lambda.DockerImageFunction {
  if (!config.path) {
    throw new Error('Path is required to create Lambda Function')
  }

  return new lambda.DockerImageFunction(stack, config.name, {
    code: lambda.DockerImageCode.fromImageAsset(config.path),
    timeout: cdk.Duration.seconds(10),
    architecture: lambda.Architecture.ARM_64,
    environment: config.secrets,
    role: role
  })
}


export function createApiLambdaRole(
  scope: cdk.Stack,
  name: string,
  policies: Policy[]
): iam.Role {
  if (!policies) {
    throw new Error('Policies are required to add Policies to Lambda')
  }

  const role = new iam.Role(scope, name, {
    assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
  });

  // Add policies to the role
  for (const policy of policies) {
    role.addToPolicy(
      new iam.PolicyStatement({
        actions: policy.actions,
        resources: policy.resources,
      })
    );
  }
  return role;
}


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
  lambdaFunction.addEventSourceMapping(
    `${kinesisStreamName}EventSource`,
    {
      eventSourceArn: kinesisStream.streamArn,
      batchSize: 1,
      startingPosition: lambda.StartingPosition.TRIM_HORIZON,
    }
  )
}

export function createKinesisLambdaRole(
  scope: cdk.Stack,
  name: string,
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
  const role = new iam.Role(scope, name, {
    assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
  });

  // Add policies to the role
  for (const policy of policies) {
    role.addToPolicy(
      new iam.PolicyStatement({
        actions: policy.actions,
        resources: [kinesisStreamArn],
      })
    );
  }

  return role;
}

