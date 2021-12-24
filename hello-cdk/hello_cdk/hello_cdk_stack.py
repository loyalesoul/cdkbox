from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy,
    aws_sqs as sqs,
)
from constructs import Construct


class HelloCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self,
            "MyFirstBucket",
            versioned=False,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        queue = sqs.Queue(self, "TheQueue", encryption=sqs.QueueEncryption.KMS_MANAGED)
