import { RemovalPolicy } from "aws-cdk-lib";
import { LambdaIntegration, LogGroupLogDestination, RestApi } from "aws-cdk-lib/aws-apigateway";
import { IFunction } from "aws-cdk-lib/aws-lambda";
import { LogGroup, RetentionDays } from "aws-cdk-lib/aws-logs";
import { Construct } from "constructs";



export class ApiGateway extends RestApi {
    constructor(scope: Construct) {
        super(scope, "ApiGateway", {
            cloudWatchRole: true,
            restApiName: 'video-storage-api',
            deployOptions: {
                accessLogDestination: new LogGroupLogDestination(new LogGroup(scope, "video-storage-api-log-group", {
                    logGroupName: "api-gateway",
                    retention: RetentionDays.SIX_MONTHS,
                    removalPolicy: RemovalPolicy.DESTROY
                }))
            }
        })
    }

    addIntegration(method: string, url: string, lambda: IFunction) {
        const resource = this.root.resourceForPath(url);
        resource.addMethod(method, new LambdaIntegration(lambda))
    }

}