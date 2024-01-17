import * as cdk from 'aws-cdk-lib'
import * as rds from 'aws-cdk-lib/aws-rds'
import * as sm from 'aws-cdk-lib/aws-secretsmanager'
import * as ec2 from 'aws-cdk-lib/aws-ec2'

import { Construct } from 'constructs'

export class RdsStack extends cdk.Stack {
  public rdsInstance: rds.DatabaseInstance
  public rdsVPC: ec2.IVpc

  constructor(scope: Construct, id: string, props: cdk.StackProps) {
    super(scope, id, props)
    const RDS_SECRETS = sm.Secret.fromSecretCompleteArn(
      this,
      'RDS_SECRETS',
      process.env.AWS_CACHE_RDS_ARN as string
    )

    this.rdsVPC = new ec2.Vpc(this, 'RDS_VPC', {
      maxAzs: 2,
    })

    this.rdsInstance = new rds.DatabaseInstance(this, 'RDS', {
      engine: rds.DatabaseInstanceEngine.MYSQL,
      credentials: rds.Credentials.fromSecret(RDS_SECRETS),
      vpc: this.rdsVPC,
    })
  }
}
