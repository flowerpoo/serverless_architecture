import json
import urllib.parse
import boto3



ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    """tag_key = 'Auto-Start'
    tag_value = 'Action'
    
    instances = ec2.describe_instances(Filters=[{'Name': f'tag:{tag_key}', 'Values': [tag_value]}])
    
    instance_ids = [instance['InstanceId'] for reservation in instances['Reservations'] for instance in reservation['Instances']]
    
    print(instance_ids) """
    
    #define empty list 
    startids = []
    stopids = []
    #storing instance in a variable 
    instances = ec2.describe_instances(Filters=[{'Name' : 'tag:tag',"Values" : ['Auto-Start','Auto-Stop']}])
    # storing the instance in respective list 
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            for tags in instance['Tags']:
                if tags['Value'] == 'Auto-Start':
                    startids.append(instance['InstanceId'])
                elif tags['Value'] == 'Auto-Stop':
                    stopids.append(instance['InstanceId'])
    #printing the instance 
    print(startids)
    print(stopids)
    
    #start the instance
    ec2.start_instances(InstanceIds=startids)
    print("started  instance  ")
    # stop the instance
    ec2.stop_instances(InstanceIds=stopids)
    print("ended instance")