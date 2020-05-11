from aws_cdk import (aws_s3 as s3, core)


class S3Hosting(core.Construct):

    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        s3_host = s3.Bucket(
            self, 'SweetSite', bucket_name=kwargs['name'],
            website_index_document="index.html",
            website_error_document="404.html",
            public_read_access=True)

        s3.CfnBucket(self, 'Bucket',  bucket_name=s3_host.bucket_name)