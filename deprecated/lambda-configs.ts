// config/lambda-configs.ts
import 'dotenv/config'

import * as lambda from '@aws-cdk/aws-lambda'

import { S3_ACTIONS } from '../models/databases_models'
import { LambdaConfig } from '../models/lambda_models'

export const lambdaConfigs: LambdaConfig[] = [
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.GET],
      allowOrigins: ['*'],
    },
    name: 'Health Check',
    path: './functions/health_check/',
    secrets: {},
    url: '/api/v1/',
  },
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Create User',
    path: './functions/create_user/',
    policy: {
      actions: [S3_ACTIONS.PUT_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    secrets: {},
    url: '/api/v1/users/create',
  },
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.DELETE],
      allowOrigins: ['*'],
    },
    name: 'Delete User',
    path: './functions/delete_user/',
    policy: {
      actions: [S3_ACTIONS.DELETE_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    secrets: {},
    url: '/api/v1/users/delete',
  },
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Upload Video File',
    path: './functions/upload_video_file/',
    policy: [
      {
        actions: [S3_ACTIONS.PUT_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    secrets: {
      S3_BUCKET_ARN: process.env.AWS_USER_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
    url: '/api/v1/videos/upload/file',
  },
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Upload Video Meta Data',
    path: './functions/upload_video_meta_data/',
    policy: [
      {
        actions: [S3_ACTIONS.PUT_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    secrets: {
      AWS_USER_RDS_ARN: process.env.AWS_USER_VIDE_RDS_ARN as string,
      AWS_USER_RDS_NAME: process.env.AWS_USER_VIDEO_RDS_NAME as string,
      AWS_USER_VIDEO_RDS_ARN: process.env.AWS_USER_VIDEO_RDS_ARN as string,
      AWS_USER_VIDEO_RDS_ENGINE: process.env
        .AWS_USER_VIDEO_RDS_ENGINE as string,
      AWS_USER_VIDEO_RDS_HOST: process.env.AWS_USER_VIDEO_RDS_HOST as string,
      AWS_USER_VIDEO_RDS_NAME: process.env.AWS_USER_VIDEO_RDS_NAME as string,
      AWS_USER_VIDEO_RDS_PASSWORD: process.env
        .AWS_USER_VIDEO_RDS_PASSWORD as string,
      AWS_USER_VIDEO_RDS_PORT: process.env.AWS_USER_VIDEO_RDS_PORT as string,
      AWS_USER_VIDEO_RDS_USERNAME: process.env
        .AWS_USER_VIDEO_RDS_USERNAME as string,
    },
    url: '/api/v1/videos/upload/meta-data',
  },
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.DELETE],
      allowOrigins: ['*'],
    },
    name: 'Delete Video',
    path: './functions/delete_video/',
    policy: [
      {
        actions: [S3_ACTIONS.GET_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    secrets: {},
    url: '/api/v1/videos/delete',
  },
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Fetch Video',
    path: './functions/fetch_video/',
    policy: [
      {
        actions: [S3_ACTIONS.GET_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    secrets: {
      RDS_DATABASE_ARN: process.env.AWS_RDS_DATABASE_ARN as string,
      RDS_DATABASE_NAME: process.env.AWS_RDS_DATABASE_NAME as string,
    },
    url: '/api/v1/videos/request',
  },
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Fetch All Videos',
    path: './functions/fetch_all_videos/',
    policy: [
      {
        actions: [S3_ACTIONS.GET_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    secrets: {
      RDS_DATABASE_ARN: process.env.AWS_RDS_DATABASE_ARN as string,
      RDS_DATABASE_NAME: process.env.AWS_RDS_DATABASE_NAME as string,
    },
    url: '/api/v1/videos/request/all',
  },
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Fetch Videos by Date',
    path: './functions/fetch_videos_by_date/',
    policy: [
      {
        actions: [S3_ACTIONS.GET_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    secrets: {
      RDS_DATABASE_ARN: process.env.AWS_RDS_DATABASE_ARN as string,
      RDS_DATABASE_NAME: process.env.AWS_RDS_DATABASE_NAME as string,
    },
    url: '/api/v1/videos/request/date',
  },
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Fetch Videos by Date Range',
    path: './functions/fetch_videos_by_date_range/',
    policy: [
      {
        actions: [S3_ACTIONS.GET_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN as string],
      },
    ],
    secrets: {
      RDS_DATABASE_ARN: process.env.AWS_RDS_DATABASE_ARN as string,
      RDS_DATABASE_NAME: process.env.AWS_RDS_DATABASE_NAME as string,
    },
    url: '/api/v1/videos/request/date-range',
  },
]
