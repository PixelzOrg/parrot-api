import * as cdk from 'aws-cdk-lib';
import * as sqs from '@aws-cdk/aws-sqs';
import { Construct } from 'constructs';

export class SqsStack extends cdk.Stack {
    public readonly myQueue: sqs.Queue;

    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);
    }
}
