// config/lambda-configs.ts
import 'dotenv/config'
import * as secrets from "aws-cdk-lib/aws-secretsmanager";
import * as lambda from '@aws-cdk/aws-lambda'
import { S3_ACTIONS } from '../models/constants'
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
    name: 'Create User',
    url: '/api/v1/users/create',
    path: './functions/create_user/',
    authType: lambda.FunctionUrlAuthType.NONE,
    policies: [
      {
        actions: [S3_ACTIONS.PUT_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ['*'],
      allowOrigins: ['*'],
    },
    secrets: {},
  },
  {
    name: 'Delete User',
    url: '/api/v1/users/delete',
    path: './functions/delete_user/',
    authType: lambda.FunctionUrlAuthType.NONE,
    policies: [
      {
        actions: [S3_ACTIONS.DELETE_OBJECT],
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
  {
    name: 'Upload Video File',
    url: '/api/v1/videos/upload/file',
    path: './functions/upload_video_file/',
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
    name: 'Upload Video Meta Data',
    url: '/api/v1/videos/upload/meta-data',
    path: './functions/upload_video_meta_data/',
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
    name: 'Delete Video',
    url: '/api/v1/videos/delete',
    path: './functions/delete_video/',
    authType: lambda.FunctionUrlAuthType.NONE,
    policies: [
      {
        actions: [S3_ACTIONS.GET_OBJECT],
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
  {
    name: 'Fetch Video',
    url: '/api/v1/videos/request',
    path: './functions/fetch_video/',
    authType: lambda.FunctionUrlAuthType.NONE,
    policies: [
      {
        actions: [S3_ACTIONS.GET_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ['*'],
      allowOrigins: ['*'],
    },
    secrets: {
      RDS_DATABASE_NAME: process.env.AWS_RDS_DATABASE_NAME as string,
      RDS_DATABASE_ARN: process.env.AWS_RDS_DATABASE_ARN as string,
    },
  },
  {
    name: 'Fetch All Videos',
    url: '/api/v1/videos/request/all',
    path: './functions/fetch_all_videos/',
    authType: lambda.FunctionUrlAuthType.NONE,
    policies: [
      {
        actions: [S3_ACTIONS.GET_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ['*'],
      allowOrigins: ['*'],
    },
    secrets: {
      RDS_DATABASE_NAME: process.env.AWS_RDS_DATABASE_NAME as string,
      RDS_DATABASE_ARN: process.env.AWS_RDS_DATABASE_ARN as string,
    },
  },
  {
    name: 'Fetch Videos by Date',
    url: '/api/v1/videos/request/date',
    path: './functions/fetch_videos_by_date/',
    authType: lambda.FunctionUrlAuthType.NONE,
    policies: [
      {
        actions: [S3_ACTIONS.GET_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ['*'],
      allowOrigins: ['*'],
    },
    secrets: {
      RDS_DATABASE_NAME: process.env.AWS_RDS_DATABASE_NAME as string,
      RDS_DATABASE_ARN: process.env.AWS_RDS_DATABASE_ARN as string,
    },
  },
  {
    name: 'Fetch Videos by Date Range',
    url: '/api/v1/videos/request/date-range',
    path: './functions/fetch_videos_by_date_range/',
    authType: lambda.FunctionUrlAuthType.NONE,
    policies: [
      {
        actions: [S3_ACTIONS.GET_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ['*'],
      allowOrigins: ['*'],
    },
    secrets: {
      RDS_DATABASE_NAME: process.env.AWS_RDS_DATABASE_NAME as string,
      RDS_DATABASE_ARN: process.env.AWS_RDS_DATABASE_ARN as string,
    },
  },
]
