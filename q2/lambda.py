import json
import urllib.parse
import boto3
from datetime import datetime, timedelta

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #bucket name specified 
    bucket_name = 'poovarasanb3'

    # for testing replace 30 with 20 days 
    retention_days = 20

    # Create S3 client
    s3 = boto3.client('s3')
   

    # List objects in the bucket
    objects = s3.list_objects_v2(Bucket=bucket_name)

    # Iterate through objects and delete those older than retention_days
    for obj in objects.get('Contents', []):
        key = obj['Key']
        last_modified = obj['LastModified']
        #get last modified date
        LastModified_date = obj['LastModified'].date()
        print(LastModified_date)
        # get current date
        current_date = datetime.today().date()
        print(current_date)
        
        # Calculate the difference in days
        age_in_days = (current_date - LastModified_date).days
        print(age_in_days)
        # delete all the files which are older than mentioned days 
        if age_in_days > retention_days:
            print(f"Deleting object: {key}")
            s3.delete_object(Bucket=bucket_name, Key=key)

    return {
        'statusCode': 200,
        'body': 'S3 bucket cleanup completed.'
    }

   