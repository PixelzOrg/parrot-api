// config/lambda-configs.ts
import 'dotenv/config'
import * as secrets from "aws-cdk-lib/aws-secretsmanager";
import * as lambda from '@aws-cdk/aws-lambda'
import { S3_ACTIONS, RDS_ACTIONS } from '../models/constants'
import { LambdaConfig } from '../models/lambdas'

export const lambdaConfigs: LambdaConfig[] = [
  {
    name: 'Health Check',
    url: '/api/v1/',
    path: './functions/health_check/',
    authType: lambda.FunctionUrlAuthType.NONE,
    policies: [],
    corsConfig: {
      allowMethods: [lambda.HttpMethod.GET],
      allowHeaders: ['*'],
      allowOrigins: ['*'],
    },
    secrets: {},
  },
  {
    name: 'Start Capture Upload',
    url: '/api/v1/capture/upload/start',
    path: './functions/start_video_upload_process/',
    policies: [
      {
        actions: [S3_ACTIONS.PUT_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ['*'],
      allowOrigins: ['*'],
    },
    secrets: {
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
      S3_BUCKET_ARN: process.env.AWS_USER_BUCKET_ARN as string,
    },
  },
  {
    name: 'Append Capture Upload',
    url: '/api/v1/capture/upload/append',
    path: './functions/append_video_upload_process/',
    policies: [
      {
        actions: [S3_ACTIONS.PUT_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ['*'],
      allowOrigins: ['*'],
    },
    secrets: {
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
      S3_BUCKET_ARN: process.env.AWS_USER_BUCKET_ARN as string,
    },
  },
  {
    name: 'Complete Capture Upload',
    url: '/api/v1/capture/upload/complete',
    path: './functions/complete_video_upload_process/',
    authType: lambda.FunctionUrlAuthType.NONE,
    policies: [
      {
        actions: [S3_ACTIONS.PUT_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    corsConfig: {
      allowMethods: [lambda.HttpMethod.DELETE],
      allowHeaders: ['*'],
      allowOrigins: ['*'],
    },
    secrets: {},
  },
]
