import * as cdk from 'aws-cdk-lib'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as ec2 from 'aws-cdk-lib/aws-ec2'

import { ApiGateway } from './api-gateway-stack'
import { PolicyStatement } from 'aws-cdk-lib/aws-iam'
import { LambdaConfig } from '../models/lambda_models'
import { lambdaConfigs } from '../config/lambda-configs'
import { verifyLambdaConfig } from '../models/lambda_models'
import { Construct } from 'constructs'

export class LambdaStack extends cdk.Stack {
  constructor(
    scope: Construct,
    id: string,
    api: ApiGateway,
    props?: cdk.StackProps
  ) {
    super(scope, id, props)

    /*
    const S3_BUCKET_NAME = cdk.Fn.importValue('S3_Bucket_Name')
    const S3_BUCKET_ARN = cdk.Fn.importValue('S3_Bucket_ARN')
    */
    this.loadLambdaFunctions(this, api)
  }
  private loadLambdaFunctions(stack: cdk.Stack, api: ApiGateway): void {
    const RDS_VPC = this.getRdsVpc(stack)
    for (const config of lambdaConfigs) {
      verifyLambdaConfig(config)

      let lambdaFunction: lambda.DockerImageFunction

      if (config.vpcId) {
        lambdaFunction = this.createLambdaFunctionWithRdsVPC(
          stack,
          config.name,
          config.path,
          config.secrets,
          RDS_VPC
        )
      } else {
        lambdaFunction = this.createLambdaFunction(
          stack,
          config.name,
          config.path,
          config.secrets
        )
      }

      if (config.policy) {
        this.addPoliciesToLambda(lambdaFunction, config)
      }
      if (config.type === 'api') {
        api.addIntegration(
          // @ts-expect-error - Neither of these will be undefined because we verify the config
          config.corsConfig.allowMethods[0],
          // @ts-expect-error - Read above
          config.url,
          lambdaFunction
        )
      }
    }
  }

  private createLambdaFunction(
    stack: cdk.Stack,
    name: string,
    path: string,
    secrets: Record<string, string>
  ): lambda.DockerImageFunction {
    return new lambda.DockerImageFunction(stack, name, {
      functionName: name,
      code: lambda.DockerImageCode.fromImageAsset(path),
      timeout: cdk.Duration.seconds(10),
      architecture: lambda.Architecture.ARM_64,
      environment: secrets,
    })
  }

  private createLambdaFunctionWithRdsVPC(
    stack: cdk.Stack,
    name: string,
    path: string,
    secrets: Record<string, string>,
    vpc: ec2.IVpc
  ): lambda.DockerImageFunction {
    return new lambda.DockerImageFunction(stack, name, {
      functionName: name,
      code: lambda.DockerImageCode.fromImageAsset(path),
      timeout: cdk.Duration.seconds(10),
      architecture: lambda.Architecture.ARM_64,
      environment: secrets,
      vpc: vpc,
    })
  }

  private addPoliciesToLambda(
    lambdaFunction: lambda.DockerImageFunction,
    config: LambdaConfig
  ): void {
    if (!config.policy) {
      throw new Error('Policies are required to add Policies to Lambda')
    }

    lambdaFunction.addToRolePolicy(
      new PolicyStatement({
        actions: config.policy.actions,
        resources: config.policy.resources,
      })
    )
  }

  private getRdsVpc(stack: cdk.Stack): ec2.IVpc {
    const vpc = ec2.Vpc.fromLookup(stack, 'RDS_VPC', {
      vpcId: process.env.AWS_CACHE_RDS_VPC_ID,
    })
    return vpc
  }
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
