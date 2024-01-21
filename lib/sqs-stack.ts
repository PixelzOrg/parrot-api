import * as cdk from 'aws-cdk-lib'
import * as sqs from 'aws-cdk-lib/aws-sqs'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as lambdaEventSources from 'aws-cdk-lib/aws-lambda-event-sources'

import { Construct } from 'constructs'
import { SQSLambdaConfigs } from '../config/lambda-config'

export class SqsStack extends cdk.Stack {
  public WhisperQueue: sqs.Queue
  public SummaryQueue: sqs.Queue
  public VideoContextQueue: sqs.Queue

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    this.WhisperQueue = this.createQueue(this, 'WhisperQueue')
    this.SummaryQueue = this.createQueue(this, 'SummaryQueue')
    this.VideoContextQueue = this.createQueue(this, 'VideoContextQueue')

    this.createSQSLambdaFunctions(this)
  }

  private createSQSLambdaFunctions(stack: cdk.Stack): void {
    for (const config of SQSLambdaConfigs) {
      let queue: sqs.Queue
      switch (config.queue) {
        case 'WhisperQueue':
          queue = this.WhisperQueue
          break
        case 'SummaryQueue':
          queue = this.SummaryQueue
          break
        case 'VideoContextQueue':
          queue = this.VideoContextQueue
          break
        default:
          throw new Error('Invalid queue name')
      }
      const SQSLambda = new lambda.DockerImageFunction(
        stack,
        config.name,
        {
          architecture: lambda.Architecture.ARM_64,
          code: lambda.DockerImageCode.fromImageAsset(config.path),
          environment: config.secrets,
          functionName: config.name,
          timeout: cdk.Duration.seconds(10),
        }
      );
      SQSLambda.addEventSource(
        new lambdaEventSources.SqsEventSource(queue, {
          batchSize: 1,
        })
      );
      if (config.policy) {
        SQSLambda.addToRolePolicy(
          new cdk.aws_iam.PolicyStatement({
            actions: config.policy.actions,
            resources: config.policy.resources,
          })
        )
      }
    }
  }

  private createQueue(stack: cdk.Stack, name: string): sqs.Queue {
    const queue = new sqs.Queue(stack, name, {
      queueName: name,
    })
    return queue
  }
}
