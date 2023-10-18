from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from aws_cdk import Stack, Tags, CfnOutput
from constructs import Construct
from aws_cdk import aws_ec2 as ec2
from aws_cdk.aws_ec2 import SubnetConfiguration

class NetworkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

    @property
    def db_vpc(self) -> ec2.Vpc:
        return self._db_vpc
  

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.define_vpcs()


    def define_vpcs(self):

        self._db_vpc = ec2.Vpc(
            self,
            "db-vpc",
            max_azs=3,
            cidr="10.2.0.0/16",
            subnet_configuration=[
                SubnetConfiguration(name='db-vpc-subnet-isolated', subnet_type=ec2.SubnetType.PRIVATE_ISOLATED)
            ])
    

      

    