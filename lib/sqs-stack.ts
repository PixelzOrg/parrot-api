import * as sqs from 'aws-cdk-lib/aws-sqs'
import * as cdk from 'aws-cdk-lib'
import { Construct } from 'constructs'

export class SqsStack extends cdk.Stack {
  public readonly myQueue: sqs.Queue

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)
  }
}
