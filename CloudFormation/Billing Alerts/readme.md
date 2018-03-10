# Billing Alerts

For somebody new to AWS, or a lab environment, Billing Alerts are a necessity to ensure mistakes or forgotten resources aren't racking up your monthly bill. If you have a fairly consistent monthly bill, alerts can help ensure you're aware of potential security breaches or an increase in traffic to provisioned AWS resources.

## Getting Started

The simplest way to deploy the template is to use the CloudFormation [console](https://console.aws.amazon.com/cloudformation). The console will prompt you to enter your email address for the **EmailAddress** parameter and will automatically subscribe you to the SNS topic. You will need to confirm the subscription by clicking the link in the initial email received.

### Prerequisites

The account deploying the CloudFormation template needs to have an appropriate IAM policy attached that permits you to create CloudFormation stacks, create SNS topics, and create CloudWatch alarms.
