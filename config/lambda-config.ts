import * as lambda from '@aws-cdk/aws-lambda'
import 'dotenv/config'

import { S3_ACTIONS } from '../models/databases_models'
import { LambdaConfig } from '../models/lambda_models'

export const lambdaConfigs: LambdaConfig[] = [
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    name: 'Whisper-Transcription-Stage',
    path: './functions/pipe/whisper_transcription_stage/',
    policy: {
      actions: [S3_ACTIONS.GET_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    secrets: {
      AWS_CACHE_RDS_NAME: process.env.AWS_CACHE_RDS_NAME as string,
      AWS_CACHE_RDS_PASSWORD: process.env.AWS_USER_VIDEO_RDS_PASSWORD as string,
      AWS_CACHE_RDS_USERNAME: process.env.AWS_CACHE_RDS_USERNAME as string,
      S3_BUCKET_ARN: process.env.AWS_USER_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
  },
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    name: 'Vision-Analysis-Stage',
    path: './functions/pipe/vision_analysis_stage/',
    policy: {
      actions: [S3_ACTIONS.GET_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    secrets: {
      AWS_CACHE_RDS_NAME: process.env.AWS_CACHE_RDS_NAME as string,
      AWS_CACHE_RDS_PASSWORD: process.env.AWS_USER_VIDEO_RDS_PASSWORD as string,
      AWS_CACHE_RDS_USERNAME: process.env.AWS_CACHE_RDS_USERNAME as string,
      S3_BUCKET_ARN: process.env.AWS_USER_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
  },
  {
    authType: lambda.FunctionUrlAuthType.NONE,
    name: 'ChatGPT-Summary-Stage',
    path: './functions/pipe/chatgpt_summary_stage/',
    policy: {
      actions: [S3_ACTIONS.GET_OBJECT],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    secrets: {
      AWS_CACHE_RDS_NAME: process.env.AWS_CACHE_RDS_NAME as string,
      AWS_CACHE_RDS_PASSWORD: process.env.AWS_USER_VIDEO_RDS_PASSWORD as string,
      AWS_CACHE_RDS_USERNAME: process.env.AWS_CACHE_RDS_USERNAME as string,
      S3_BUCKET_ARN: process.env.AWS_USER_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
  },
]
