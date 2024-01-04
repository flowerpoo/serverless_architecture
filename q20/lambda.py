import json
import urllib.parse
import boto3

def lambda_handler(event, context):
    region = 'us-east-1'

    # Create ELB client
    elbv2 = boto3.client('elbv2', region_name=region)

    """# Describe all load balancers
    response = elbv2.describe_load_balancers()

    # Extract load balancer information
    load_balancers = response['LoadBalancers']
    for lb in load_balancers:
        print(f"Load Balancer Name: {lb['LoadBalancerName']}")
        print(f"Load Balancer ARN: {lb['LoadBalancerArn']}")
        print(f"Load Balancer DNS Name: {lb['DNSName']}")
        print(f"Load Balancer Scheme: {lb['Scheme']}")
        print(f"Load Balancer VPC ID: {lb['VpcId']}")
        print("\n")"""
    load_balancer_arn = 'arn:aws:elasticloadbalancing:us-east-1:295397358094:targetgroup/poovatarget/5c5d18dd6c89082d'
    
   

    # Describe instances registered with the Load Balancer
    instances = elbv2.describe_target_health(TargetGroupArn=load_balancer_arn)

    # Check the health status of each instance
    for instance in instances['TargetHealthDescriptions']:
        instance_id = instance['Target']['Id']
        health_status = instance['TargetHealth']['State']

        print(f"Instance ID: {instance_id}, Health Status: {health_status}")
        
    return {
        'statusCode': 200,
        'body': 'Load Balancer health check completed.'
    }