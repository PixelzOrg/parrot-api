import * as cdk from 'aws-cdk-lib'
import { PolicyStatement } from 'aws-cdk-lib/aws-iam'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import { Construct } from 'constructs'

import { lambdaConfigs } from '../config/lambda-config'
import { ApiLambdaConfigs } from '../config/routes-lambdas-config'
import {
  LambdaStackProps,
  verifyApiLambdaConfig,
} from '../models/lambda_models'
import { APILambdaConfig } from '../models/lambda_models'
import { ApiGatewayStack } from './api-gateway-stack'
import { S3BucketStack } from './s3-stack'
import * as ec2 from 'aws-cdk-lib/aws-ec2'
import * as rds from 'aws-cdk-lib/aws-rds';

export class LambdaStack extends cdk.Stack {
  private s3BucketStack: S3BucketStack
  private apiStack: ApiGatewayStack
  private RDS_VPC_ID: string
  private RDS_VPC: ec2.IVpc

  constructor(scope: Construct, id: string, props: LambdaStackProps) {
    super(scope, id, props)
    this.s3BucketStack = props.s3BucketStack
    this.apiStack = props.apiGatewayStack
    this.RDS_VPC_ID = process.env.AWS_CACHE_RDS_VPC_ID as string
    this.RDS_VPC = this.getRdsVpc(this)

    this.initializeAPILambdas()
    this.initializeServiceLambdas()
  }

  private initializeAPILambdas(): void {
    ApiLambdaConfigs.forEach((apiLambdaConfig) => {
      verifyApiLambdaConfig(apiLambdaConfig)

      const ApiLambdaFunction = this.createApiLambdaFunction(
        this,
        apiLambdaConfig.name,
        apiLambdaConfig.path,
        apiLambdaConfig.secrets
      )

      this.configureApiRouteToLambda(ApiLambdaFunction, apiLambdaConfig)
      this.attachPoliciesToLambda(
        ApiLambdaFunction,
        apiLambdaConfig.policy.actions,
        apiLambdaConfig.policy.resources
      )
    })
  }

  private initializeServiceLambdas(): void {
    lambdaConfigs.forEach((lambdaConfig) => {
      // TODO: write verification for lambdaConfig
      const serviceLambdaFunction = this.createLambdaFunctionWithRdsVPC(
        this,
        lambdaConfig.name,
        lambdaConfig.path,
        lambdaConfig.secrets
      )
      this.attachPoliciesToLambda(
        serviceLambdaFunction,
        lambdaConfig.policy.actions,
        lambdaConfig.policy.resources
      )
    })
  }

  private createApiLambdaFunction(
    stack: cdk.Stack,
    name: string,
    path: string,
    secrets: Record<string, string>
  ): lambda.DockerImageFunction {
    return new lambda.DockerImageFunction(stack, name, {
      architecture: lambda.Architecture.ARM_64,
      code: lambda.DockerImageCode.fromImageAsset(path),
      environment: secrets,
      functionName: name,
      timeout: cdk.Duration.seconds(10),
    })
  }

  private configureApiRouteToLambda(
    lambdaFunction: lambda.DockerImageFunction,
    config: APILambdaConfig
  ): void {
    this.apiStack.addIntegration(
      // @ts-expect-error - TODO: fix this
      config.corsConfig.allowMethods,
      config.url,
      lambdaFunction
    )
  }

  private getRdsVpc(stack: cdk.Stack): ec2.IVpc {
    return ec2.Vpc.fromLookup(stack, 'RDS_VPC', {
      vpcId: this.RDS_VPC_ID,
    })
  }

  private createLambdaFunctionWithRdsVPC(
    stack: cdk.Stack,
    name: string,
    path: string,
    secrets: Record<string, string>
  ): lambda.DockerImageFunction {
    return new lambda.DockerImageFunction(stack, name, {
      architecture: lambda.Architecture.ARM_64,
      code: lambda.DockerImageCode.fromImageAsset(path),
      environment: secrets,
      functionName: name,
      timeout: cdk.Duration.seconds(10),
      vpc: this.RDS_VPC,
    })
  }

  private attachPoliciesToLambda(
    lambdaFunction: lambda.DockerImageFunction,
    actions: string[],
    resources: string[]
  ): void {
    lambdaFunction.addToRolePolicy(
      new PolicyStatement({
        actions: actions,
        resources: resources,
      })
    )
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
