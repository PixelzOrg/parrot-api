export const S3_ACTIONS = {
  PUT_OBJECT: 's3:PutObject',
  GET_OBJECT: 's3:GetObject',
  LIST_BUCKET: 's3:ListBucket',
  DELETE_OBJECT: 's3:DeleteObject',
} as const;

export const RDS_ACTIONS = {
  SELECT: 'rds:Select',
  INSERT: 'rds:Insert',
  UPDATE: 'rds:Update',
  DELETE: 'rds:Delete',
} as const;
