import * as s3 from 'aws-cdk-lib/aws-s3'
import { Policy} from './lambda_models'

export interface ec2Config {
  name: string
  path: string
  policy?: Policy
  secrets: {
    [key: string]: string
  }
  eventSource?: {
    events: s3.EventType[]
    filters: s3.NotificationKeyFilter[]
  }
  bucketName?: string
  queue?: string
}