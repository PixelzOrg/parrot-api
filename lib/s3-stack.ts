import * as cdk from 'aws-cdk-lib'
import * as s3 from 'aws-cdk-lib/aws-s3'

import { Construct } from 'constructs'
import { Policy } from '../models/lambda_models'

export class S3BucketStack extends cdk.Stack {
  public s3Bucket: s3.Bucket

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    const BUCKET_NAME = process.env.AWS_USER_BUCKET_NAME as string
    const existingBucket = s3.Bucket.fromBucketName(this, 'Bucket', BUCKET_NAME)

    if (!existingBucket.bucketName) {
      this.s3Bucket = new s3.Bucket(this, 'Bucket', {
        bucketName: BUCKET_NAME,
        objectOwnership: s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
        blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      })
    } else {
      this.s3Bucket = existingBucket as s3.Bucket
      new cdk.CfnOutput(this, 'S3_Bucket_Name', {
        value: this.s3Bucket.bucketName,
      })
      new cdk.CfnOutput(this, 'S3_Bucket_ARN', {
        value: this.s3Bucket.bucketArn,
      })
    }
  }

  public updatePolicyWithS3(policy: Policy): void {
    policy.resources.push(this.s3Bucket.bucketArn)
  }
}
