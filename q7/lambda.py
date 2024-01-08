import boto3
import json
from datetime import date

def lambda_handler(event, context):
    # Replace 'your-sns-topic-arn' with the ARN of your SNS topic
    sns_topic_arn = 'arn:aws:sns:us-east-1:295397358094:sns-poo'
    
    # Set the billing threshold in USD
    billing_threshold = 100.0

    # Invoke costexplorer using boto3 client module
    ce = boto3.client('ce')
    
    # getting todays date, date when the lambda function is triggered
    today_date = date.today()
  
    strtoday = today_date.strftime('%Y-%m-%d')

    
    # getting date for 1st of current month
    firstofmonth = today_date.replace(day=1)
    str_firstofmonth = firstofmonth.strftime('%Y-%m-%d')
    
    # Calling get_cost_and_usage to store the response
    response = ce.get_cost_and_usage(
            TimePeriod={
                'Start': str_firstofmonth,
                'End': strtoday
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost']
        )
   
    # retreiving current months bill and storing it in a variable
    latest_charge= response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
    
    
    #latest_charge = response['Datapoints'][0]['Maximum']
   
    print(latest_charge)
    if float(latest_charge) > billing_threshold:
        # Send SNS alert
        sns = boto3.client('sns')
        message = f"High AWS Billing Alert: Estimated charges exceed {billing_threshold} USD. Current charges: {latest_charge} USD."
        subject = 'High AWS Billing Alert'

        sns.publish(
            TopicArn=sns_topic_arn,
            Message=message,
            Subject=subject
        )

        print("High AWS Billing Alert sent.")
    else:
        print("AWS Billing within threshold.")

    return {
        'statusCode': 200,
        'body': 'Billing check completed.'
    }
