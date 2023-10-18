#!/usr/bin/env python3
import os
from aws_cdk import Environment
import aws_cdk as cdk
import boto3
from cdk_bug.network_stack import NetworkStack
from cdk_bug.doc_db_stack import DatabaseStack

environment = Environment(
        account=boto3.client('sts').get_caller_identity()['Account'], region=boto3.session.Session().region_name)
print(environment)
app = cdk.App()
networking_stack = NetworkStack(app, "network-stack", env=environment)
db_stack = DatabaseStack(
    app,
    "database-stack",
    db_vpc=networking_stack.db_vpc,
    env=environment)
app.synth()
