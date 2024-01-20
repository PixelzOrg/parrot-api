import { RemovalPolicy } from 'aws-cdk-lib'
import * as cdk from 'aws-cdk-lib'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import { AuthLambdaConfig } from '../config/lambda-config'
import {
  LambdaIntegration,
  LogGroupLogDestination,
  RestApi,
} from 'aws-cdk-lib/aws-apigateway'
import * as apigateway from 'aws-cdk-lib/aws-apigateway'
import { IFunction } from 'aws-cdk-lib/aws-lambda'
import { LogGroup, RetentionDays } from 'aws-cdk-lib/aws-logs'
import { Construct } from 'constructs'

export class ApiGatewayStack extends cdk.Stack {
  public api: RestApi
  public auth: apigateway.IAuthorizer
  private logGroup: LogGroup

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)
    this.logGroup = this.createLogGroup(this)
    this.api = this.createRestAPI(this, this.logGroup)
    this.auth = this.createAuthorizerLambda(this)
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

  private createAuthorizerLambda(stack: cdk.Stack): apigateway.IAuthorizer {
    const auth = new lambda.DockerImageFunction(stack, 'createAuthorizerLambda', {
      architecture: lambda.Architecture.ARM_64,
      code: lambda.DockerImageCode.fromImageAsset(AuthLambdaConfig.path),
      environment: AuthLambdaConfig.secrets,
      functionName: AuthLambdaConfig.name,
      timeout: cdk.Duration.seconds(10),
    })
    return new apigateway.TokenAuthorizer(stack, 'parrot-token-authorizer', {
      handler: auth,
      identitySource: 'method.request.header.Authorization',
      resultsCacheTtl: cdk.Duration.minutes(5),
    })
  }

  private createLogGroup(stack: cdk.Stack): LogGroup {
    return new LogGroup(stack, 'parrot-api-log-group', {
      logGroupName: 'parrot-api-gateway',
      removalPolicy: RemovalPolicy.DESTROY,
      retention: RetentionDays.SIX_MONTHS,
    })
  }

  public addRouteIntegration(
    allowMethods: string[],
    url: string,
    lambda: IFunction,
    auth: apigateway.IAuthorizer
  ) {
    const resource = this.api.root.resourceForPath(url)
    console.log(url, lambda.functionName)
    const method = allowMethods[0]
    resource.addMethod(method, new LambdaIntegration(lambda), {
      authorizer: auth,
    })
  }

}
