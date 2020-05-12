from aws_cdk import aws_s3 as s3, core


class SweetCookiesStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(
            scope,
            id
            # , stack_name=kwargs["name"]
        )
        s3_host = s3.Bucket(
            self,
            id,
            website_index_document="index.html",
            website_error_document="404.html",
            public_read_access=True,
        )

        s3.CfnBucket(self, "CookieJar", bucket_name=s3_host.bucket_name)
