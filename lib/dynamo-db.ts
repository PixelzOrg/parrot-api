import * as cdk from 'aws-cdk-lib'
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb'
import { Construct } from 'constructs'

export class DynamoDbStack extends cdk.Stack {
  public dynamoTable: dynamodb.Table

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)
    this.dynamoTable = this.createDynamoDbTable(this)
  }

  private createDynamoDbTable(stack: cdk.Stack): dynamodb.Table {
    const dynamoDbTable = new dynamodb.Table(stack, 'CreateDynamoDbTable', {
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      partitionKey: {
        name: 'memory_id',
        type: dynamodb.AttributeType.STRING,
      },
      tableName: process.env.AWS_DYNAMODB_TABLE_NAME as string,
    })
    return dynamoDbTable
  }
}
