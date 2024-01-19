export const S3_ACTIONS = {
  DELETE_OBJECT: 's3:DeleteObject',
  GET_OBJECT: 's3:GetObject',
  LIST_BUCKET: 's3:ListBucket',
  PUT_OBJECT: 's3:PutObject',
}

export const DynamoDbPermissions = {
  BATCH_GET: 'dynamodb:BatchGetItem',
  BATCH_WRITE: 'dynamodb:BatchWriteItem',
  GET: 'dynamodb:GetItem',
  PUT: 'dynamodb:PutItem',
  QUERY: 'dynamodb:Query',
  SCAN: 'dynamodb:Scan',
  UPDATE: 'dynamodb:UpdateItem',
}
