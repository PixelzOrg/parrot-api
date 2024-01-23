import { ec2Config } from "../models/ec2_models"
import { SQS_ACTIONS } from '../models/sqs_models';
import { DynamoDbPermissions } from '../models/databases_models';


export const ec2Configuration: ec2Config = {
  name: "ai-video-audio-processing",
  path: "./server/",
  policy: {
    actions: [
      SQS_ACTIONS.SEND_MESSAGE,
      SQS_ACTIONS.RECEIVE_MESSAGE,
      SQS_ACTIONS.GET_QUEUE_ATTRIBUTES,
      DynamoDbPermissions.PUT,
      DynamoDbPermissions.GET,
      "ecr:DescribeImages",
      "ecr:DescribeRepositories"
    ],
    resources: [
      process.env.AWS_UPLOAD_BUCKET_ARN as string,
      process.env.AWS_DYNAMO_DB_MP4_ARN as string,
      process.env.AWS_DYNAMO_DB_MP3_ARN as string,
      process.env.AWS_SQS_WHISPER_QUEUE_ARN as string,
      process.env.AWS_SQS_VIDEO_CONTEXT_QUEUE_ARN as string,
      process.env.AWS_SQS_SUMMARY_QUEUE_ARN as string,
    ],
  },
  secrets: {
    DYNAMO_DB_MP3_ARN: process.env.AWS_DYNAMO_DB_MP3_ARN as string,
    DYNAMO_DB_MP3_NAME: process.env.AWS_DYNAMO_DB_MP3_NAME as string,
    DYNAMO_DB_MP4_ARN: process.env.AWS_DYNAMO_DB_MP4_ARN as string,
    DYNAMO_DB_MP4_NAME: process.env.AWS_DYNAMO_DB_MP4_NAME as string,
    S3_BUCKET_ARN: process.env.AWS_UPLOAD_BUCKET_ARN as string,
    S3_BUCKET_NAME: process.env.AWS_UPLOAD_BUCKET_NAME as string,
    WHISPER_QUEUE_URL: process.env.AWS_SQS_WHISPER_QUEUE_URL as string,
    VIDEO_CONTEXT_QUEUE_URL: process.env.AWS_SQS_VIDEO_CONTEXT_QUEUE_URL as string,
    SUMMARY_QUEUE_URL: process.env.AWS_SQS_SUMMARY_QUEUE_URL as string,
  }
}