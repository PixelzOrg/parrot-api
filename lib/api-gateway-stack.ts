import { RemovalPolicy } from 'aws-cdk-lib'
import * as cdk from 'aws-cdk-lib'
import {
  LambdaIntegration,
  LogGroupLogDestination,
  RestApi,
} from 'aws-cdk-lib/aws-apigateway'
import { IFunction } from 'aws-cdk-lib/aws-lambda'
import { LogGroup, RetentionDays } from 'aws-cdk-lib/aws-logs'
import { Construct } from 'constructs'

export class ApiGatewayStack extends cdk.Stack {
  public api: RestApi
  private logGroup: LogGroup

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)
    this.logGroup = this.createLogGroup(this)
    this.api = this.createRestAPI(this, this.logGroup)
  }

  private createRestAPI(stack: cdk.Stack, logGroup: LogGroup): RestApi {
    return new RestApi(stack, 'parrot-api', {
      cloudWatchRole: true,
      deployOptions: {
        accessLogDestination: new LogGroupLogDestination(logGroup),
      },
      restApiName: 'parrot-api',
    })
  }

  private createLogGroup(stack: cdk.Stack): LogGroup {
    return new LogGroup(stack, 'parrot-api-log-group', {
      logGroupName: 'parrot-api-gateway',
      removalPolicy: RemovalPolicy.DESTROY,
      retention: RetentionDays.SIX_MONTHS,
    })
  }

  public addIntegration(
    allowMethods: string[],
    url: string,
    lambda: IFunction
  ) {
    const resource = this.api.root.resourceForPath(url)
    console.log(url, lambda.functionName)
    const method = allowMethods[0]
    resource.addMethod(method, new LambdaIntegration(lambda))
  }
}
