#stop_code


import json
import boto3

ec2 = boto3.resource('ec2', region_name='ap-southeast-1')

def lambda_handler(event, context):
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']},{'Name': 'tag:project','Values':['test']}])
    for instance in instances:
        id=instance.id
        ec2.instances.filter(InstanceIds=[id]).stop()
        print("Instance ID is stopped"+instance.id)

    return "success"