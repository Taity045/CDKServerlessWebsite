from aws_cdk import (
    core,
    aws_lambda,
    aws_dynamodb,
    aws_s3 as _s3,
    aws_apigateway as apigw,
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

        # create s3 bucket
        s3 = _s3.Bucket(self, "s3bucket")

#       apigw.LambdaRestApi(
#             self, 'Endpoint',
#             handler=fx,)

       
        fx = _lambda_function(
            self, 'lambda_function',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.asset('lambda'),
            handler='main.handler')   

       

app = core.App()
ServerlessStack(app,"website")
app.synth()        