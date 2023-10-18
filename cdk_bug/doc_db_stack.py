from aws_cdk import aws_docdb as docdb
from aws_cdk import aws_ec2 as ec2


from aws_cdk import aws_kms as kms


from aws_cdk import Duration
from aws_cdk import (
    Stack
)
from constructs import Construct



class DatabaseStack(Stack):

    def __init__(
            self, scope: Construct, id: str, db_vpc: ec2.Vpc,
            **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.defineDocDB(vpc=db_vpc)


    def defineDocDB(self, vpc):
        key = kms.Key(self, "primary-db-key", alias="primary-db-key")
        cluster = docdb.DatabaseCluster(
            self,
            "primary-db-cluster",
            master_user=docdb.Login(username="administrator"),
            vpc=vpc,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MEDIUM),
            backup=docdb.BackupProps(retention=Duration.days(30), preferred_window="5:00-6:00"),
            instances=1,
            db_cluster_name="primary-db-cluster",
            kms_key=key)

       
    

