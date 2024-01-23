import * as cdk from 'aws-cdk-lib'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as s3 from 'aws-cdk-lib/aws-s3'
import * as s3n from 'aws-cdk-lib/aws-s3-notifications'
import { Construct } from 'constructs'

import { S3ToSQSConfig } from '../config/lambda-config'

export class S3BucketStack extends cdk.Stack {
  public uploadBucket: s3.Bucket

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)
    this.uploadBucket = this.createBucket(
      this,
      process.env.AWS_UPLOAD_BUCKET_NAME as string
    )
    this.createS3EventLambda(this)
  }

  private createBucket(stack: cdk.Stack, name: string): s3.Bucket {
    const bucket = new s3.Bucket(stack, 'createBucket', {
      bucketName: name,
    })
    return bucket
  }

  private createS3EventLambda(stack: cdk.Stack): void {
    const eventLambda = new lambda.DockerImageFunction(
      stack,
      'createS3EventLambda',
      {
        architecture: lambda.Architecture.ARM_64,
        code: lambda.DockerImageCode.fromImageAsset(S3ToSQSConfig.path),
        environment: S3ToSQSConfig.secrets,
        functionName: S3ToSQSConfig.name,
        timeout: cdk.Duration.seconds(10),
      }
    )
    this.uploadBucket.addEventNotification(
      s3.EventType.OBJECT_CREATED,
      new s3n.LambdaDestination(eventLambda)
    )
    if (S3ToSQSConfig.policy) {
      eventLambda.addToRolePolicy(
        new cdk.aws_iam.PolicyStatement({
          actions: S3ToSQSConfig.policy.actions,
          resources: S3ToSQSConfig.policy.resources,
        })
      )
    }
  }
}
