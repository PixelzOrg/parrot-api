import * as cdk from 'aws-cdk-lib'
import * as ec2 from 'aws-cdk-lib/aws-ec2'
import * as rds from 'aws-cdk-lib/aws-rds'
import * as sm from 'aws-cdk-lib/aws-secretsmanager'
import { Construct } from 'constructs'

export class RdsStack extends cdk.Stack {
  public rdsInstance: rds.DatabaseInstance
  public rdsVPC: ec2.IVpc
  private rdsCredentials: rds.Credentials

  constructor(scope: Construct, id: string, props: cdk.StackProps) {
    super(scope, id, props)
    this.rdsCredentials = this.getRdsCredentials()
    this.rdsVPC = this.createNewVPC()
    this.rdsInstance = this.createNewInstance()

    this.outputRdsVpcId()
  }

  private outputRdsVpcId(): void {
    new cdk.CfnOutput(this, 'VpcId', {
      exportName: 'RdsVpcId',
      value: this.rdsVPC.vpcId,
    })
  }

  private getRdsCredentials(): rds.Credentials {
    const temp = sm.Secret.fromSecretCompleteArn(
      this,
      'RDS_SECRETS',
      process.env.AWS_CACHE_RDS_LOGIN as string
    )
    return rds.Credentials.fromSecret(temp)
  }

  private createNewInstance(): rds.DatabaseInstance {
    return new rds.DatabaseInstance(this, 'RDS', {
      credentials: this.rdsCredentials,
      engine: rds.DatabaseInstanceEngine.MYSQL,
      vpc: this.rdsVPC,
    })
  }

  private createNewVPC(): ec2.IVpc {
    return new ec2.Vpc(this, 'RDS_VPC', {
      maxAzs: 2,
    })
  }

  public getRdsVpc(stack: cdk.Stack): ec2.IVpc {
    return ec2.Vpc.fromLookup(stack, 'RDS_VPC', {
      vpcId: process.env.AWS_CACHE_RDS_VPC_ID as string,
    })
  }
}
