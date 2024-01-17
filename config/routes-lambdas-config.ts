import 'dotenv/config'

import * as lambda from '@aws-cdk/aws-lambda'

import { S3_ACTIONS } from '../models/databases_models'
import { APILambdaConfig } from '../models/lambda_models'

export const ApiLambdaConfigs: APILambdaConfig[] = [
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Upload-Video-File',
    path: './functions/routes/upload_file/',
    policy: {
      actions: [S3_ACTIONS.PUT_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    secrets: {
      S3_BUCKET_ARN: process.env.AWS_USER_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
    url: '/api/v1/capture/upload/upload_file',
  },
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Start-Multipart-Upload',
    path: './functions/routes/start_multipart_upload/',
    policy: {
      actions: [S3_ACTIONS.PUT_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    secrets: {
      S3_BUCKET_ARN: process.env.AWS_USER_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
    url: '/api/v1/capture/upload/start_multipart_upload',
  },
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Append-Multipart-Upload',
    path: './functions/routes/append_multipart_upload/',
    policy: {
      actions: [S3_ACTIONS.PUT_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    secrets: {
      S3_BUCKET_ARN: process.env.AWS_USER_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
    url: '/api/v1/capture/upload/append_multipart_upload',
  },
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.DELETE],
      allowOrigins: ['*'],
    },
    name: 'Complete-Multipart-Upload',
    path: './functions/routes/complete_multipart_upload/',
    policy: {
      actions: [S3_ACTIONS.PUT_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    secrets: {
      S3_BUCKET_ARN: process.env.AWS_USER_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
    url: '/api/v1/capture/upload/complete_multipart_upload',
  },
]
