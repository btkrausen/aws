# Bastion Host

This is a quick CloudFormation template to launch bastion hosts in AWS for management or testing.

## Getting Started

**bastion.yml:**

The simplest way to deploy the template is to use the CloudFormation [console](https://console.aws.amazon.com/cloudformation). This template will automatically create **one (1) Windows 2016 instance** or one Linux host with a public IP address. The console will prompt you to enter your information for the *VPC*, *InstanceSubnet*, *EC2KeyPair*, and *PublicIPaddress* parameters and the template will provision the instance with a security group allowing access only from your public IP. If you want access from anywhere, enter 0.0.0.0/0 for *PublicIPaddress*.

The template uses Mappings as a way to run this template anywhere in the United States. It will automatically grab the AMI-Id from the region where the template is provisioned.

### Prerequisites

The account deploying the CloudFormation template needs to have an appropriate IAM policy attached that permits you to create CloudFormation stacks, security groups, and EC2 instances
