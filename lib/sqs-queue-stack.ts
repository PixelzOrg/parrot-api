import * as cdk from 'aws-cdk-lib'
import * as sqs from 'aws-cdk-lib/aws-sqs'
import { Construct } from 'constructs'

export class SqsStack extends cdk.Stack {
  public WhisperQueue: sqs.Queue
  public VisionQueue: sqs.Queue
  public SummaryQueue: sqs.Queue

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    // Create an SQS queue
    this.WhisperQueue = new sqs.Queue(this, 'WhisperQueue', {
      queueName: 'WhisperQueue',
    })

    this.VisionQueue = new sqs.Queue(this, 'VisionQueue', {
      queueName: 'VisionQueue',
    })

    this.SummaryQueue = new sqs.Queue(this, 'SummaryQueue', {
      queueName: 'SummaryQueue',
    })
  }
}
