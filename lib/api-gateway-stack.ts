import { RemovalPolicy } from 'aws-cdk-lib'
import {
  LambdaIntegration,
  LogGroupLogDestination,
  RestApi,
} from 'aws-cdk-lib/aws-apigateway'
import { IFunction } from 'aws-cdk-lib/aws-lambda'
import { LogGroup, RetentionDays } from 'aws-cdk-lib/aws-logs'
import { Construct } from 'constructs'
import * as cdk from 'aws-cdk-lib'

export class ApiGateway extends cdk.Stack {
  public api: RestApi

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    const logGroup = new LogGroup(this, 'parrot-api-log-group', {
      logGroupName: 'parrot-api-gateway',
      retention: RetentionDays.SIX_MONTHS,
      removalPolicy: RemovalPolicy.DESTROY,
    })

    this.api = new RestApi(this, 'parrot-api', {
      cloudWatchRole: true,
      restApiName: 'parrot-api',
      deployOptions: {
        accessLogDestination: new LogGroupLogDestination(logGroup),
      },
    })
  }

  addIntegration(method: string, url: string, lambda: IFunction) {
    const resource = this.api.root.resourceForPath(url)
    resource.addMethod(method, new LambdaIntegration(lambda))
  }
}
