from aws_cdk import (aws_s3 as _s3, core)
from s3_static_hosting import S3Hosting


class SweetCookiesStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        