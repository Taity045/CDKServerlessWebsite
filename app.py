from aws_cdk import (
    core,
    aws_lambda,
    aws_dynamodb,
    aws_s3 as s3,
)


class ServerlessStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create dynamo table
        table = aws_dynamodb.Table(
            self, "mapping_table",
            partition_key=aws_dynamodb.Attribute(
                name="id",
                type=aws_dynamodb.AttributeType.STRING
            )
        )

        #Create S3 Bucket
        s3 = _s3.Bucket(self, "s3bucket")

app = core.App()
ServerlessStack(app, "website")
app.synth()        