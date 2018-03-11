# Billing Alerts

For somebody new to AWS, or a lab environment, Billing Alerts are a necessity to ensure mistakes or forgotten resources aren't racking up your monthly bill. If you have a fairly consistent monthly bill, alerts can help ensure you're aware of potential security breaches or an increase in traffic to provisioned AWS resources.

## Getting Started

**BillingAlerts.yml:**

The simplest way to deploy the template is to use the CloudFormation [console](https://console.aws.amazon.com/cloudformation). This template will automatically create **six (6) billing alarms**, including alarms with $5, $10, $20, $30, $40, and $50 thresholds. The console will prompt you to enter your email address for the *EmailAddress* parameter and the template will automatically subscribe you to the SNS topic. You will need to confirm the subscription by clicking the link in the initial email received.

**BillingAlerts_w_InputParameters.yml**

Per request, this template uses an input parameter so you can create the billing alarms using desired thresholds if the above values don't work for you. Simply enter the threshold values as a comma delimited list for the *AlarmThresholds* parameter, such as 10,20,30,40,50. Enter your email address for the *EmailAddress* parameter and the template will automatically subscribe you to the SNS topic. You will need to confirm the subscription by clicking the link in the initial email received.

**As AWS Billing is only handled in N. Virginia, you must run this template in US-East-1**

### Prerequisites

The account deploying the CloudFormation template needs to have an appropriate IAM policy attached that permits you to create CloudFormation stacks, create SNS topics, and create CloudWatch alarms.
