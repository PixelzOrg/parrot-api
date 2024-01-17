import * as ec2 from '@aws-cdk/aws-ec2'
import * as iam from '@aws-cdk/aws-iam'
import * as cdk from 'aws-cdk-lib'
import { Construct } from 'constructs'

export class EC2Stack extends cdk.Stack {
  public name: string
  public vpc: ec2.IVpc
  public role: iam.Role
  public securityGroup: ec2.SecurityGroup

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)
    this.name = 'ec2-stack'
    this.role = this.createEC2Role(scope)
    this.vpc = this.getRdsVpc(this)
    this.securityGroup = this.createEC2SecurityGroup(this)
  }

  private createEC2Instance(scope: Construct): ec2.Instance {
    const instance = new ec2.Instance(scope, this.name, {
      instanceType: ec2.InstanceType.of(
        ec2.InstanceClass.T3,
        ec2.InstanceSize.MICRO
      ),
      machineImage: ec2.MachineImage.latestAmazonLinux(),
      role: this.role,
      vpc: this.vpc,
    })
    return instance
  }

  private createEC2SecurityGroup(scope: Construct): ec2.SecurityGroup {
    return new ec2.SecurityGroup(scope, 'simple-instance-1-sg', {
      allowAllOutbound: true, // will let your instance send outboud traffic
      securityGroupName: 'simple-instance-1-sg',
      vpc: this.vpc,
    })
  }

  private createEC2Role(scope: Construct): iam.Role {
    const role = new iam.Role(scope, 'EC2Role', {
      assumedBy: new iam.ServicePrincipal('ec2.amazonaws.com'),
    })
    return role
  }

  private getRdsVpc(stack: cdk.Stack): ec2.IVpc {
    const vpc = ec2.Vpc.fromLookup(stack, 'RDS_VPC', {
      vpcId: process.env.AWS_CACHE_RDS_VPC_ID,
    })
    return vpc
  }
}
