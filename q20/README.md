# serverless_architecture

Assignment 20: Load Balancer Health Checker

Objective: Design a Lambda function that checks the health of registered instances behind an Elastic Load Balancer (ELB) and notifies via SNS if any instances are unhealthy.

Instructions:

1. Create a Lambda function.

2. With Boto3, configure the function to:

1. Check the health of registered instances behind a given ELB.
2. If any instances are found to be unhealthy, publish a detailed message to an SNS topic.

3. Set up a CloudWatch event to trigger this Lambda function every 10 minutes.

---------------------------------------------------------------------
Solution:

* Lambda function created to check the health status of the instance that are added with the taget group in Load Balancer.
* If the instance are in unhealthy status SNS will send the alert via email.
*  Cron job is setup by creating Evenbridge rule that can run every 10 mins.
* Done.