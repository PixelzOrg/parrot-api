import * as cdk from 'aws-cdk-lib'
import * as s3 from 'aws-cdk-lib/aws-s3'
import { Construct } from 'constructs'

export class S3BucketStack extends cdk.Stack {
  public uploadBucket: s3.Bucket

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)
    this.uploadBucket = this.createBucket(
      this,
      process.env.AWS_UPLOAD_BUCKET_NAME as string
    )
  }

  private createBucket(stack: cdk.Stack, name: string): s3.Bucket {
    const bucket = new s3.Bucket(stack, 'Bucket', {
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      bucketName: name,
      objectOwnership: s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
    })
    return bucket
  }
}
