import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import * as cdk from 'aws-cdk-lib'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as lambdaEventSources from 'aws-cdk-lib/aws-lambda-event-sources'
import * as s3 from 'aws-cdk-lib/aws-s3'
import { Construct } from 'constructs'

import { lambdaConfigs } from '../config/lambda-config'
import { LambdaConfig } from '../models/lambda_models'
import { LambdaStackProps } from '../models/lambda_models'
import { ApiGatewayStack } from './api-gateway-stack'
import { S3BucketStack } from './s3-stack'

export class LambdaStack extends cdk.Stack {
  private s3BucketStack: S3BucketStack
  private apiStack: ApiGatewayStack

  constructor(scope: Construct, id: string, props: LambdaStackProps) {
    super(scope, id, props)
    this.s3BucketStack = props.s3BucketStack
    this.apiStack = props.apiGatewayStack

    this.initializeLambdas()
  }

  private initializeLambdas(): void {
    lambdaConfigs.forEach((config) => {

      const lambdaFunction: lambda.DockerImageFunction =
        this.createLambdaFunction(
          this,
          config.name,
          config.path,
          config.secrets
      )

      if (config.url && config.corsConfig) {
        this.configureApiRouteToLambda(lambdaFunction, config)
      }

      if (config.eventSource && config.bucketName) {
        this.addS3EventSourceToLambda(
          lambdaFunction,
          config.eventSource.events,
          config.eventSource.filters
        )
      }
      if (config.policy) {
        this.attachPoliciesToLambda(
          lambdaFunction,
          config.policy.actions,
          config.policy.resources
        )
      }
    })
  }

  private addS3EventSourceToLambda(
    lambdaFunction: lambda.DockerImageFunction,
    events: s3.EventType[],
    filters: s3.NotificationKeyFilter[]
  ): void {
    const s3EventSource = new lambdaEventSources.S3EventSource(
      this.s3BucketStack.uploadBucket,
      {
        events: events,
        filters: filters,
      }
    )
    lambdaFunction.addEventSource(s3EventSource)
  }

  private createLambdaFunction(
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
    config: LambdaConfig,
  ): void {
    this.apiStack.addRouteIntegration(
      // @ts-ignore
      config.corsConfig.allowMethods,
      // @ts-ignore
      config.url,
      lambdaFunction,
      this.apiStack.auth
    )
  }

  private attachPoliciesToLambda(
    lambdaFunction: lambda.DockerImageFunction,
    actions: string[],
    resources: string[]
  ): void {
    lambdaFunction.addToRolePolicy(
      new cdk.aws_iam.PolicyStatement({
        actions: actions,
        resources: resources,
      })
    )
  }
}
