import * as cdk from 'aws-cdk-lib'
import * as s3 from 'aws-cdk-lib/aws-s3'

import { Construct } from 'constructs'

export class S3BucketStack extends cdk.Stack {
  public s3Bucket: s3.Bucket

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    const BUCKET_NAME = process.env.AWS_USER_BUCKET_NAME as string
    this.s3Bucket = new s3.Bucket(this, BUCKET_NAME, {
      objectOwnership: s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
    })
  }
}
