import * as cdk from 'aws-cdk-lib'
import * as ec2 from 'aws-cdk-lib/aws-ec2'

import { Construct } from 'constructs'

export class VpcStack extends cdk.Stack {
  public vpc: ec2.Vpc
  public securityGroup: ec2.SecurityGroup

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    this.vpc = new ec2.Vpc(this, 'VpcStack', {
      cidr: '10.0.0.0/16',
      maxAzs: 2,
      subnetConfiguration: [
        {
          cidrMask: 26,
          name: 'isolatedSubnet',
          subnetType: ec2.SubnetType.PRIVATE_ISOLATED,
        },
      ],
      natGateways: 0,
    })

    this.securityGroup = new ec2.SecurityGroup(this, 'parrot-security-group', {
      vpc: this.vpc,
      allowAllOutbound: false,
      securityGroupName: 'ParrotSecurityGroup',
    })

    const PORT = process.env.AWS_RDS_CACHE_PORT as string

    this.securityGroup.addIngressRule(
      ec2.Peer.ipv4('10.0.0.0/16'),
      ec2.Port.tcp(3306),
      `Allow port ${PORT} for database connection from only within the VPC })`
    )
  }
}
