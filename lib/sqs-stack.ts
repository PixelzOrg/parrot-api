import * as cdk from 'aws-cdk-lib'
import * as sqs from 'aws-cdk-lib/aws-sqs'
import { Construct } from 'constructs'

export class SqsStack extends cdk.Stack {
  public ServerQueue: sqs.Queue

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    this.ServerQueue = this.createQueue(this, 'ServerQueue')
  }

  private createQueue(stack: cdk.Stack, name: string): sqs.Queue {
    const queue = new sqs.Queue(stack, name, {
      queueName: name,
    })
    return queue
  }
}
