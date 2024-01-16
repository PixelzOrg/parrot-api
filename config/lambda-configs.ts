// config/lambda-configs.ts
import 'dotenv/config'
import * as lambda from '@aws-cdk/aws-lambda'

import { S3_ACTIONS } from '../models/databases_models'
import { LambdaConfig } from '../models/lambda_models'

/*/
  / API CONFIGURATIONS
  /
  */

export const lambdaConfigs: LambdaConfig[] = [
  {
    type: 'api',
    name: 'Health Check',
    url: '/api/v1/',
    path: './functions/routes/health_check/',
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowMethods: ['GET'],
      allowHeaders: ['*'],
      allowOrigins: ['*'],
    },
    secrets: {},
  },
  {
    type: 'api',
    name: 'Upload Video File',
    url: '/api/v1/capture/upload/upload_file',
    path: './functions/routes/upload_file/',
    policy: {
      actions: [S3_ACTIONS.PUT_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ['*'],
      allowOrigins: ['*'],
    },
    secrets: {
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
  },
  {
    type: 'api',
    name: 'Start Multipart_Upload',
    url: '/api/v1/capture/upload/start_multipart_upload',
    path: './functions/routes/start_multipart_upload/',
    policy: {
      actions: [S3_ACTIONS.PUT_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ['*'],
      allowOrigins: ['*'],
    },
    secrets: {
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
  },
  {
    type: 'api',
    name: 'Append Multipart Upload',
    url: '/api/v1/capture/upload/append_multipart_upload',
    path: './functions/routes/append_multipart_upload/',
    policy: {
      actions: [S3_ACTIONS.PUT_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    authType: lambda.FunctionUrlAuthType.NONE,
    corsConfig: {
      allowMethods: [lambda.HttpMethod.POST],
      allowHeaders: ['*'],
      allowOrigins: ['*'],
    },
    secrets: {
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
  },
  {
    type: 'api',
    name: 'Complete Multipart Upload',
    url: '/api/v1/capture/upload/complete_multipart_upload',
    path: './functions/routes/complete_multipart_upload/',
    authType: lambda.FunctionUrlAuthType.NONE,
    policy: {
      actions: [S3_ACTIONS.PUT_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    corsConfig: {
      allowMethods: [lambda.HttpMethod.DELETE],
      allowHeaders: ['*'],
      allowOrigins: ['*'],
    },
    secrets: {},
  },

  /*
  /
  /  FILE PROCESSING PIPELINE CONFIGURATIONS
  /
  */

  {
    type: 'pipeline',
    name: 'Whisper Transcription Stage',
    path: './functions/pipe/whisper_transcription_stage/',
    authType: lambda.FunctionUrlAuthType.NONE,
    policy: {
      actions: [S3_ACTIONS.GET_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    corsConfig: {
      allowMethods: [],
      allowHeaders: [],
      allowOrigins: [],
    },
    secrets: {
      AWS_CACHE_RDS_NAME: process.env.AWS_CACHE_RDS_NAME as string,
      AWS_CACHE_RDS_USERNAME: process.env.AWS_CACHE_RDS_USERNAME as string,
      AWS_CACHE_RDS_PASSWORD: process.env.AWS_USER_VIDEO_RDS_PASSWORD as string,
    },
    kinesisStream: 'WhisperStage',
  },
  {
    type: 'pipeline',
    name: 'Vision Analysis Stage',
    path: './functions/pipe/vision_analysis_stage/',
    authType: lambda.FunctionUrlAuthType.NONE,
    policy: {
      actions: [S3_ACTIONS.GET_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    corsConfig: {
      allowMethods: [],
      allowHeaders: [],
      allowOrigins: [],
    },
    secrets: {
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
      AWS_CACHE_RDS_NAME: process.env.AWS_CACHE_RDS_NAME as string,
      AWS_CACHE_RDS_USERNAME: process.env.AWS_CACHE_RDS_USERNAME as string,
      AWS_CACHE_RDS_PASSWORD: process.env.AWS_USER_VIDEO_RDS_PASSWORD as string,
    },
    kinesisStream: 'VisionStage',
  },
  {
    type: 'pipeline',
    name: 'ChatGPT Summary Stage',
    path: './functions/pipe/chatgpt_summary_stage/',
    authType: lambda.FunctionUrlAuthType.NONE,
    policy: {
      actions: [S3_ACTIONS.GET_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    corsConfig: {
      allowMethods: [],
      allowHeaders: [],
      allowOrigins: [],
    },
    secrets: {
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
      AWS_CACHE_RDS_NAME: process.env.AWS_CACHE_RDS_NAME as string,
      AWS_CACHE_RDS_USERNAME: process.env.AWS_CACHE_RDS_USERNAME as string,
      AWS_CACHE_RDS_PASSWORD: process.env.AWS_USER_VIDEO_RDS_PASSWORD as string,
    },
    kinesisStream: 'ChatGPTSummaryStage',
  },
]
