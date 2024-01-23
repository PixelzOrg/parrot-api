import 'dotenv/config'

import * as lambda from 'aws-cdk-lib/aws-lambda'

import { S3_ACTIONS } from '../models/databases_models'
import { DynamoDbPermissions } from '../models/databases_models'
import { LambdaConfig } from '../models/lambda_models'
import { SQS_ACTIONS } from '../models/sqs_models'

export const lambdaConfigs: LambdaConfig[] = [
  /*
  /   CHAT RELATED LAMBDAS
  */
  {
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Chat-Prompt',
    path: './functions/chat_prompt/',
    secrets: {
      OPEN_AI_KEY: process.env.OPEN_AI_KEY as string,
    },
    url: '/api/v1/chat/prompt',
  },
  {
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Chat-Prompt-With-Memory',
    path: './functions/chat_prompt_with_memory/',
    secrets: {
      OPEN_AI_KEY: process.env.OPEN_AI_KEY as string,
    },
    url: '/api/v1/chat/prompt/memory',
  },
  {
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Generate-Daily-Summary',
    path: './functions/generate_daily_summary/',
    secrets: {
      OPEN_AI_KEY: process.env.OPEN_AI_KEY as string,
    },
    url: '/api/v1/overview/daily_summary',
  },
  /*
  /   UPLOAD RELATED LAMBDAS
  */
  {
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Upload-Video-File',
    path: './functions/upload_file/',
    policy: {
      actions: [
        S3_ACTIONS.PUT_OBJECT,
        S3_ACTIONS.GET_OBJECT,
        S3_ACTIONS.LIST_BUCKET,
        S3_ACTIONS.DELETE_OBJECT,
        DynamoDbPermissions.PUT,
        DynamoDbPermissions.GET,
      ],
      resources: [
        process.env.AWS_UPLOAD_BUCKET_ARN as string,
        process.env.AWS_DYNAMO_DB_MP3_ARN as string,
      ],
    },
    secrets: {
      DYNAMO_MP3_TABLE_ARN: process.env.AWS_DYNAMO_DB_MP3_ARN as string,
      DYNAMO_MP3_TABLE_NAME: process.env.AWS_DYNAMO_DB_MP3_NAME as string,
      DYNAMO_MP4_TABLE_ARN: process.env.AWS_DYNAMO_DB_MP4_ARN as string,
      DYNAMO_MP4_TABLE_NAME: process.env.AWS_DYNAMO_DB_MP4_NAME as string,
      S3_BUCKET_ARN: process.env.AWS_UPLOAD_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_UPLOAD_BUCKET_NAME as string,
    },
    url: '/api/v1/capture/upload/upload_file',
  },
  /*
  /   FETCHING RELATED LAMBDAS
  */
  {
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.POST],
      allowOrigins: ['*'],
    },
    name: 'Check-Processing-Status',
    path: './functions/check_processing_status/',
    policy: {
      actions: [
        DynamoDbPermissions.PUT,
        DynamoDbPermissions.GET,
        DynamoDbPermissions.QUERY,
      ],
      resources: [
        process.env.AWS_DYNAMO_DB_MP4_ARN as string,
        process.env.AWS_DYNAMO_DB_MP3_ARN as string,
      ],
    },
    secrets: {
      DYNAMO_MP3_TABLE_NAME: process.env.AWS_DYNAMO_DB_MP3_NAME as string,
      DYNAMO_MP4_TABLE_NAME: process.env.AWS_DYNAMO_DB_MP4_NAME as string,
    },
    url: '/api/v1/capture/upload/status',
  },
]

export const AuthLambdaConfig: LambdaConfig =
  /*
  /  AUTH RELATED LAMBDAS
  */
  {
    corsConfig: {
      allowHeaders: ['*'],
      allowMethods: [lambda.HttpMethod.ALL],
      allowOrigins: ['*'],
    },
    name: 'Firebase-Auth',
    path: './functions/firebase_auth/',
    secrets: {
      FIREBASE_CREDENTIALS: process.env.FIREBASE_CREDENTIALS as string,
    },
  }

export const S3ToSQSConfig: LambdaConfig = {
  name: 'S3-Upload-To-SQS',
  path: './functions/s3_upload_to_sqs/',
  policy: {
    actions: [
      S3_ACTIONS.PUT_OBJECT,
      S3_ACTIONS.GET_OBJECT,
      S3_ACTIONS.LIST_BUCKET,
      S3_ACTIONS.DELETE_OBJECT,
      SQS_ACTIONS.SEND_MESSAGE,
      SQS_ACTIONS.RECEIVE_MESSAGE,
      SQS_ACTIONS.GET_QUEUE_ATTRIBUTES,
    ],
    resources: [
      process.env.AWS_UPLOAD_BUCKET_ARN as string,
      process.env.SQS_SERVER_QUEUE_ARN as string,
    ],
  },
  secrets: {
    S3_BUCKET_ARN: process.env.AWS_UPLOAD_BUCKET_ARN as string,
    S3_BUCKET_NAME: process.env.AWS_UPLOAD_BUCKET_NAME as string,
    SQS_SERVER_QUEUE_URL: process.env.SQS_SERVER_QUEUE_URL as string,
  },
}
