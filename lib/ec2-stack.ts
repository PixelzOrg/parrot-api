import * as cdk from "aws-cdk-lib";
import * as ec2 from "aws-cdk-lib/aws-ec2";

import { ec2Config } from "../models/ec2_models";
import { ec2Configuration } from "../config/ec2-config"

import { DockerImageAsset } from "aws-cdk-lib/aws-ecr-assets";

import { join } from "path";
import { Policy } from "../models/lambda_models";

export class Ec2Stack extends cdk.Stack {
  private vpc: ec2.Vpc;
  private dockerImage: DockerImageAsset;
  private ec2Instance: ec2.Instance;

  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    this.vpc = this.createVpc();
    this.ec2Instance = this.loadEc2Instance(this.vpc);
  }

  private loadEc2Instance(vpc: ec2.Vpc): ec2.Instance {
    const instance = this.createEc2Instance(vpc);
    if (!ec2Configuration.policy) {
      throw new Error("No policy provided");
    }
    this.attachPoliciesToEc2Instance(instance, ec2Configuration.policy);
    return instance
  }

  private createEc2Instance(vpc: ec2.Vpc): ec2.Instance {
    const dockerImageAsset = new DockerImageAsset(this, "uploadDockerImage", {
      directory: join(__dirname, "..", "server"),
    });

    const userDataScript = ec2.UserData.forLinux();
    userDataScript.addCommands(
      "sudo yum update -y",
      "sudo amazon-linux-extras install docker -y",
      "sudo service docker start",
      `sudo docker run ${dockerImageAsset.imageUri}`
    );

    const instance = new ec2.Instance(this, "createEc2Instance", {
      instanceName: "ai-video-audio-processing-ec2-instance",
      vpc: vpc,
      instanceType: ec2.InstanceType.of(
        ec2.InstanceClass.STANDARD4,
        ec2.InstanceSize.MEDIUM,
      ),
      machineImage: ec2.MachineImage.latestAmazonLinux2023(),
      blockDevices: [
        {
          deviceName: "/dev/sdh",
          volume: ec2.BlockDeviceVolume.ebs(100),
        },
      ],
      userData: userDataScript,
    });

    return instance;
  }

  private createVpc() {
    const vpc = new ec2.Vpc(this, "createVpc", {});
    return vpc
  }

  private attachPoliciesToEc2Instance(
    ec2: ec2.Instance,
    policy: Policy,
  ): void {
    ec2.addToRolePolicy(
      new cdk.aws_iam.PolicyStatement({
        actions: policy.actions,
        resources: policy.resources,
      })
    )
  }
}