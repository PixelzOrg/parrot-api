import { StartingPosition } from '@aws-cdk/aws-lambda'

export interface KinesisConfig {
  eventSourceArn: string
  batchSize: number
  startingPosition: StartingPosition
}

export const KinesisPermissions = {
  DescribeStream: 'kinesis:DescribeStream',
  DescribeStreamSummary: 'kinesis:DescribeStreamSummary',
  GetRecords: 'kinesis:GetRecords',
  GetShardIterator: 'kinesis:GetShardIterator',
  ListShards: 'kinesis:ListShards',
  ListStreams: 'kinesis:ListStreams',
  PutRecords: 'kinesis:PutRecords',
  PutRecord: 'kinesis:PutRecord',
}
