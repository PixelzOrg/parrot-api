// config/lambda-configs.ts
import 'dotenv/config';
import * as lambda from '@aws-cdk/aws-lambda';
import * as apigateway from '@aws-cdk/aws-apigateway';
import { S3_ACTIONS } from '../models/constants';



/**
 * Configuration for defining Lambda functions and their associated settings.
 *
 * @typedef {Object} LambdaConfig
 * @property {string} name - The name of the Lambda function.
 * @property {string} url - The URL path where the Lambda function is exposed through the API Gateway.
 * @property {string} path - The local path to the Lambda function code or Docker image for deployment.
 * @property {lambda.FunctionUrlAuthType} authType - The authentication type for securing the Lambda function endpoint.
 * @property {{
*     actions: string[];
*     resources: string[Arn];
*   }} roles - The IAM roles associated with the Lambda function, specifying allowed actions and resource Arns for fine-grained permissions.
* @property {apigateway.CorsOptions} corsConfig - Cross-Origin Resource Sharing (CORS) configuration for the Lambda function's API Gateway.
*/
export interface LambdaConfig {
  name: string;
  url: string
  path: string;
  authType: lambda.FunctionUrlAuthType;
  roles: {
    actions: string[];
    resources: string[]; 
  }
  corsConfig: apigateway.CorsOptions;
}

export const lambdaConfigs: LambdaConfig[] = [
  {
    name: 'Health Check',
    url: '/api',
    path: './functions/health_check/',
    authType: lambda.FunctionUrlAuthType.NONE,
    roles: {
      actions: [''],
      resources: [''],
    },
    corsConfig: {
      allowMethods: [lambda.HttpMethod.GET],
      allowHeaders: ["*"],
      allowOrigins: ["*"],
    },
  },
  {
    name: 'Create User',
    url: '/api/v1/users/create',
    path: './functions/create_user/',
    authType: lambda.FunctionUrlAuthType.NONE,
    roles: {
      actions: [S3_ACTIONS.PUT_OBJECT],
      resources: [process.env.S3_BUCKET_ARN as string]
    },
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ["*"],
      allowOrigins: ["*"],
    },
  },
  {
    name: 'Delete User',
    url: '/api/v1/users/delete',
    path: './functions/delete_user/',
    authType: lambda.FunctionUrlAuthType.NONE,
    roles: {
      actions: [S3_ACTIONS.DELETE_OBJECT],
      resources: [process.env.S3_BUCKET_ARN as string],
    },
    corsConfig: {
      allowMethods: [lambda.HttpMethod.DELETE],
      allowHeaders: ["*"],
      allowOrigins: ["*"],
    },
  },
  {
    name: 'Upload Video',
    url: '/api/v1/videos/upload',
    path: './functions/upload_video/',
    roles: {
      actions: [S3_ACTIONS.PUT_OBJECT],
      resources: [process.env.S3_BUCKET_ARN as string],
    },
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ["*"],
      allowOrigins: ["*"],
    },
  },
  {
    name: 'Delete Video',
    url: '/api/v1/videos/delete',
    path: './functions/delete_video/',
    authType: lambda.FunctionUrlAuthType.NONE,
    roles: {
      actions: [S3_ACTIONS.DELETE_OBJECT],
      resources: [process.env.S3_BUCKET_ARN as string],
    },
    corsConfig: {
      allowMethods: [lambda.HttpMethod.DELETE],
      allowHeaders: ["*"],
      allowOrigins: ["*"],
    },
  },
  {
    name: 'Fetch Video',
    url: '/api/v1/videos/request',
    path: './functions/fetch_video/',
    authType: lambda.FunctionUrlAuthType.NONE,
    roles: {
      actions: [S3_ACTIONS.GET_OBJECT],
      resources: [process.env.S3_BUCKET_ARN as string],
    },
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ["*"],
      allowOrigins: ["*"],
    },
  },
  {
    name: 'Fetch All Videos',
    url: '/api/v1/videos/request/all',
    path: './functions/fetch_all_videos/',
    authType: lambda.FunctionUrlAuthType.NONE,
    roles: {
      actions: [S3_ACTIONS.GET_OBJECT],
      resources: [process.env.S3_BUCKET_ARN as string],
    },
    corsConfig: {
      allowMethods: [lambda.HttpMethod.GET],
      allowHeaders: ["*"],
      allowOrigins: ["*"],
    },
  },
  {
    name: 'Fetch Videos by Date',
    url: '/api/v1/videos/request/date',
    path: './functions/fetch_videos_by_date/',
    authType: lambda.FunctionUrlAuthType.NONE,
    roles: {
      actions: [S3_ACTIONS.GET_OBJECT],
      resources: [process.env.S3_BUCKET_ARN as string],
    },
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ["*"],
      allowOrigins: ["*"],
    },
  },
  {
    name: 'Fetch Videos by Date Range',
    url: '/api/v1/videos/request/date-range',
    path: './functions/fetch_videos_by_date_range/',
    authType: lambda.FunctionUrlAuthType.NONE,
    roles: {
      actions: [S3_ACTIONS.GET_OBJECT],
      resources: [process.env.S3_BUCKET_ARN as string],
    },
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ["*"],
      allowOrigins: ["*"],
    },
  },
];
