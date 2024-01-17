import * as cdk from 'aws-cdk-lib'
import * as s3 from 'aws-cdk-lib/aws-s3'
import { IBucket } from 'aws-cdk-lib/aws-s3'
import { Construct } from 'constructs'

export class S3BucketStack extends cdk.Stack {
  public s3Bucket: s3.Bucket

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)
    this.s3Bucket = this.createBucket(this)
  }

  private createBucket(stack: cdk.Stack): s3.Bucket {
    const bucket = new s3.Bucket(stack, 'Bucket', {
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      bucketName: process.env.AWS_USER_BUCKET_NAME as string,
      objectOwnership: s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
    })
    return bucket
  }
}
