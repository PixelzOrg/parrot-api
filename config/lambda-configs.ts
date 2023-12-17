// config/lambda-configs.ts
import 'dotenv/config';
import * as lambda from '@aws-cdk/aws-lambda';
import { S3_ACTIONS } from '../models/constants';
import { LambdaConfig } from '../models/lambdas';

export const lambdaConfigs: LambdaConfig[] = [
  {
    name: 'Health Check',
    url: '/api',
    path: './functions/health_check/',
    authType: lambda.FunctionUrlAuthType.NONE,
    policies: [],
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
    policies: [
      {
        actions: [S3_ACTIONS.PUT_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN + '/*'], 
      },
    ],
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
    policies: [
      {
        actions: [S3_ACTIONS.DELETE_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN + '/*'], 
      },
    ],
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
    policies: [
      {
        actions: [S3_ACTIONS.PUT_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN + '/*'], 
      },
    ],
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
    policies: [
      {
        actions: [S3_ACTIONS.DELETE_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN + '/*'],
      },
    ],
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
    policies: [
      {
        actions: [S3_ACTIONS.GET_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN + '/*'],
      },
    ],
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
    policies: [
      {
        actions: [S3_ACTIONS.GET_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN + '/*'],
      },
    ],
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
    policies: [
      {
        actions: [S3_ACTIONS.GET_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN + '/*'],
      },
    ],
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
    policies: [
      {
        actions: [S3_ACTIONS.GET_OBJECT],
        resources: [process.env.AWS_USER_BUCKET_ARN + '/*'],
      },
    ],
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ["*"],
      allowOrigins: ["*"],
    },
  },
];
