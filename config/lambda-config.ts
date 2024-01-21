import 'dotenv/config'

import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as s3 from 'aws-cdk-lib/aws-s3'

import { S3_ACTIONS } from '../models/databases_models'
import { DynamoDbPermissions } from '../models/databases_models'
import { LambdaConfig } from '../models/lambda_models'
import { S3 } from 'aws-cdk-lib/aws-ses-actions'

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
      resources: [process.env.AWS_UPLOAD_BUCKET_ARN as string],
    },
    secrets: {
      DYNAMO_DB_NAME: process.env.AWS_DYNAMODB_TABLE_NAME as string,
      S3_BUCKET_ARN: process.env.AWS_UPLOAD_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_UPLOAD_BUCKET_NAME as string,
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
    path: './functions/start_multipart_upload/',
    policy: {
      actions: [S3_ACTIONS.PUT_OBJECT],
      resources: [process.env.AWS_UPLOAD_BUCKET_ARN as string],
    },
    secrets: {
      S3_BUCKET_ARN: process.env.AWS_UPLOAD_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_UPLOAD_BUCKET_NAME as string,
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
    path: './functions/append_multipart_upload/',
    policy: {
      actions: [S3_ACTIONS.PUT_OBJECT],
      resources: [process.env.AWS_UPLOAD_BUCKET_ARN as string],
    },
    secrets: {
      S3_BUCKET_ARN: process.env.AWS_UPLOAD_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_UPLOAD_BUCKET_NAME as string,
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
    path: './functions/complete_multipart_upload/',
    policy: {
      actions: [
        S3_ACTIONS.PUT_OBJECT,
        DynamoDbPermissions.PUT,
        DynamoDbPermissions.GET,
      ],
      resources: [process.env.AWS_UPLOAD_BUCKET_ARN as string],
    },
    secrets: {
      DYNAMO_DB_NAME: process.env.AWS_DYNAMODB_TABLE_NAME as string,
      S3_BUCKET_ARN: process.env.AWS_UPLOAD_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_UPLOAD_BUCKET_NAME as string,
    },
    url: '/api/v1/capture/upload/complete_multipart_upload',
  },
  /*
  /   PROCESSING RELATED LAMBDAS
  */
  {
    eventSource: {
      events: [s3.EventType.OBJECT_CREATED],
      filters: [
        {
          prefix: 'upload/',
        },
      ],
    },
    name: 'Whisper-Transcription',
    path: './functions/whisper_transcription_stage/',
    policy: {
      actions: [
        S3_ACTIONS.GET_OBJECT,
        DynamoDbPermissions.PUT,
        DynamoDbPermissions.GET,
        DynamoDbPermissions.QUERY,
      ],
      resources: [
        process.env.AWS_UPLOAD_BUCKET_ARN as string,
        process.env.AWS_DYNAMODB_TABLE_ARN as string,
      ],
    },
    secrets: {
      DYNAMO_DB_NAME: process.env.AWS_DYNAMODB_TABLE_NAME as string,
      S3_BUCKET_ARN: process.env.AWS_UPLOAD_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_UPLOAD_BUCKET_NAME as string,
    },
  },
  {
    eventSource: {
      events: [s3.EventType.OBJECT_CREATED],
      filters: [
        {
          prefix: 'upload/',
        },
      ],
    },
    name: 'Video-Context-Analysis',
    path: './functions/video_context_analysis/',
    policy: {
      actions: [
        S3_ACTIONS.GET_OBJECT,
        DynamoDbPermissions.PUT,
        DynamoDbPermissions.GET,
        DynamoDbPermissions.QUERY,
      ],
      resources: [process.env.AWS_DYNAMODB_TABLE_ARN as string],
    },
    secrets: {
      DYNAMO_DB_NAME: process.env.AWS_DYNAMODB_TABLE_NAME as string,
      OPEN_AI_KEY: process.env.OPEN_AI_KEY as string,
      S3_BUCKET_ARN: process.env.AWS_UPLOAD_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_UPLOAD_BUCKET_NAME as string,
    },
  },
  {
    eventSource: {
      events: [s3.EventType.OBJECT_CREATED],
      filters: [
        {
          prefix: 'upload/',
        },
      ],
    },
    name: 'Generate-Memory-Summary',
    path: './functions/generate_memory_summary/',
    policy: {
      actions: [
        S3_ACTIONS.GET_OBJECT,
        DynamoDbPermissions.PUT,
        DynamoDbPermissions.GET,
        DynamoDbPermissions.QUERY,
      ],
      resources: [process.env.AWS_DYNAMODB_TABLE_ARN as string],
    },
    secrets: {
      DYNAMO_DB_NAME: process.env.AWS_DYNAMODB_TABLE_NAME as string,
      OPEN_AI_KEY: process.env.OPEN_AI_KEY as string,
      S3_BUCKET_ARN: process.env.AWS_UPLOAD_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_UPLOAD_BUCKET_NAME as string,
    },
  },
  /*
  /   FETCHING RELATED LAMBDAS
  */
  {
    name: 'Check-Processing-Status',
    path: './functions/check_processing_status/',
    policy: {
      actions: [
        DynamoDbPermissions.PUT,
        DynamoDbPermissions.GET,
        DynamoDbPermissions.QUERY,
      ],
      resources: [process.env.AWS_DYNAMODB_TABLE_ARN as string],
    },
    secrets: {
      DYNAMO_DB_NAME: process.env.AWS_DYNAMODB_TABLE_NAME as string,
      OPEN_AI_KEY: process.env.OPEN_AI_KEY as string,
      S3_BUCKET_ARN: process.env.AWS_UPLOAD_BUCKET_ARN as string,
      S3_BUCKET_NAME: process.env.AWS_UPLOAD_BUCKET_NAME as string,
    },
  },
]

export const AuthLambdaConfig: LambdaConfig =
  /*
  /  AUTH RELATED LAMBDAS
  */
  {
    authorizer: true,
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
