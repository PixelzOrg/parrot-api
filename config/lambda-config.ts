import 'dotenv/config'

import * as lambda from '@aws-cdk/aws-lambda'
import * as s3 from '@aws-cdk/aws-s3'

import { S3_ACTIONS } from '../models/databases_models'
import { LambdaConfig } from '../models/lambda_models'

export const lambdaConfigs: LambdaConfig[] = [
  {
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
  {
    name: 'S3-File-Upload-To-SQS',
    path: './functions/event/s3_upload_file_to_queue/',
    policy: {
      actions: [
        's3:GetObject',
        'sqs:ReceiveMessage',
        'sqs:DeleteMessage',
        'sqs:GetQueueAttributes',
      ],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    s3Events: [s3.EventType.OBJECT_CREATED],
    secrets: {
      S3_BUCKET_ARN: process.env.AWS_USER_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
  },
  {
    name: 'Whisper-Transcription-Stage',
    path: './functions/pipe/whisper_transcription_stage/',
    policy: {
      actions: [
        S3_ACTIONS.GET_OBJECT,
        'sqs:ReceiveMessage',
        'sqs:DeleteMessage',
        'sqs:GetQueueAttributes',
      ],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    queueName: 'WhisperQueue',
    secrets: {
      S3_BUCKET_ARN: process.env.AWS_USER_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
  },
  {
    name: 'Vision-Analysis-Stage',
    path: './functions/pipe/vision_analysis_stage/',
    policy: {
      actions: [
        S3_ACTIONS.GET_OBJECT,
        'sqs:ReceiveMessage',
        'sqs:DeleteMessage',
        'sqs:GetQueueAttributes',
      ],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    queueName: 'VisionQueue',
    secrets: {
      S3_BUCKET_ARN: process.env.AWS_USER_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
  },
  {
    name: 'ChatGPT-Summary-Stage',
    path: './functions/pipe/chatgpt_summary_stage/',
    policy: {
      actions: [
        S3_ACTIONS.GET_OBJECT,
        'sqs:ReceiveMessage',
        'sqs:DeleteMessage',
        'sqs:GetQueueAttributes',
      ],
      resources: [process.env.AWS_USER_BUCKET_ARN as string],
    },
    queueName: 'SummaryQueue',
    secrets: {
      S3_BUCKET_ARN: process.env.AWS_USER_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_USER_BUCKET_NAME as string,
    },
  },
]
