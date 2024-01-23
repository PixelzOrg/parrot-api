class SqsServerMessage:
    def __init__(
      self,
      bucket: str,
      object_key: str,
      user_uid: str,
      file_uid: str,
      file_extension: str,
      local_path: str
      ):
        self.bucket = bucket
        self.object_key = object_key
        self.user_uid = user_uid
        self.file_uid = file_uid
        self.file_extension = file_extension
        self.local_path = local_path