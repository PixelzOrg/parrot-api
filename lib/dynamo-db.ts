import * as cdk from 'aws-cdk-lib'
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb'
import { Construct } from 'constructs'

export class DynamoDbStack extends cdk.Stack {
  public mp3Table: dynamodb.Table
  public mp4Table: dynamodb.Table

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)
    this.mp4Table = this.loadMp4Tables(this)
    this.mp3Table = this.loadMp3Tables(this)
  }

  private loadMp4Tables(stack: cdk.Stack): dynamodb.Table {
    const mp4Table = new dynamodb.Table(stack, 'createMp4Table', {
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      partitionKey: {
        name: 'file_uid',
        type: dynamodb.AttributeType.STRING,
      },
      tableName: process.env.AWS_DYNAMO_DB_MP4_NAME as string,
    })

    mp4Table.addGlobalSecondaryIndex({
      indexName: 'transcriptionIndex',
      partitionKey: {
        name: 'transcription',
        type: dynamodb.AttributeType.STRING,
      },
    })
    mp4Table.addGlobalSecondaryIndex({
      indexName: 'videoContextIndex',
      partitionKey: {
        name: 'videoContext',
        type: dynamodb.AttributeType.STRING,
      },
    })
    mp4Table.addGlobalSecondaryIndex({
      indexName: 'summaryIndex',
      partitionKey: { name: 'summary', type: dynamodb.AttributeType.STRING },
    })

    return mp4Table
  }

  private loadMp3Tables(stack: cdk.Stack): dynamodb.Table {
    const mp3Table = new dynamodb.Table(stack, 'createMp3Table', {
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      partitionKey: {
        name: 'file_uid',
        type: dynamodb.AttributeType.STRING,
      },
      tableName: process.env.AWS_DYNAMO_DB_MP3_NAME as string,
    })

    mp3Table.addGlobalSecondaryIndex({
      indexName: 'transcriptionIndex',
      partitionKey: {
        name: 'transcription',
        type: dynamodb.AttributeType.STRING,
      },
    })
    mp3Table.addGlobalSecondaryIndex({
      indexName: 'summaryIndex',
      partitionKey: { name: 'summary', type: dynamodb.AttributeType.STRING },
    })

    return mp3Table
  }
}
