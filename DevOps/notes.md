## AMI
### Steps to copying an AMI across an account
1. Copy unencrypted AMI to encrypted AMI, specify the KMS in the copy action
2. Give the target account permissions to create a grant. Delegate permissions to groups.
3. Share the encrypted AMI with the target account

## CodeDeploy
### CodeDeploy Deployment Configurations
1. OneAtATime: Deploys the application to one instance at a time. If the deployment fails, the deployment stops.
2. HalfAtATime: Deploys the application to half of the instances at a time. If the deployment fails, the deployment stops.
3. AllAtOnce: Deploys the application to all instances at once. If the deployment fails, the deployment stops.
4. Custom: Deploys the application to an explicit percentage of instances at a time.

### Functionality
1. Deployment Management
2. File Handling
3. Lifecycle Event Hooks

## ALB
1. Can directly log to S3

### Dualstack
1. Supports both IPv4 and IPv6
2. EC2 instances must be added to the target group

## AWS Control Tower
### Automated Landing Zone
Automates the setup of a multi-account environment, including the creation of a new AWS account, identity management, and account provisioning.

### Blueprints
Uses blueprints that encapsulate AWS best practices for security and compliance to create a multi-account environment.

### Guardrails
Provides both preventive and detective guardrails to help enforce policies and detect violations.

### Account Factory
To provision new AWS accounts in organization, we can be useful for DevOps teams managing multiple accounts.

### Log Archive and Audit Manager
Automatically configures a log archive and sets up AWS Audit Manager for compliance check which can be crucial for devops teams.

### CfCT
Automates the deployment of resources, including CloudFormation templates and SCPs, based on the organization's requirements. By leveraging an AWS CodeCommit repository to manage and version control these customizations, CfCT can automatically apply the necessary configurations and policies to new accounts provisioned through Account Factory, aligning closely with the requirement for a highly automated solution.

## S3
### Notes
1. Objects must be deleted before the bucket can be deleted, protections will prevent DeletionPolicy. This can be circumvented by using a lambda to delete objects before the bucket is deleted.
2. Can act as an artifact store for CodePipeline. Codepipeline must have permissions to access the bucket.
3. Can act as a static website host. The bucket must be public and the objects must be public.
4. Can store lambda code and be used to trigger lambda functions.

## OpsWorks
1. Autohealing can stop and restart instances that are not responding to health checks.

## IAM 
1. Best practice for allowing cross-account access is to create a role in the target account and allow the source account to assume the role using a trust policy.
Then the source account can assume the role and access the resources in the target account.
### Policy 
1. Can be used with conditionals to restrict access to resources based on tags.

## AWS Systems Manager
1. Allows for the creation of custom patch baselines that can include custom repositories, and the AWS-RunPatchBaseline document automates the verification and installation of patches.
{
    "PatchFilters": [
        {
            "Key": "MSRC_SEVERITY",
            "Values": ["Critical", "Important"]
        },
        {
            "Key": "PATCH_SET",
            "Values": ["$LATEST"]
        }
    ]
}
2. Systems manager hybrid activations can be used to manage on-premises instances.
3. IAM role is necessary to use the Systems Manager service. (Attached to target instances)
4. Can be used to automate patching of EC2 instances (Maintenance Windows).

## Storage Gateway
1. Can be used to connect on-premises storage to AWS storage services.
2. Volume Gateway can cache data on-premises and asynchronously upload data to S3.

## EventBridge
1. Near real-time event processing

## Kinesis Firehose
1. Near real-time data processing

## AWS Config
1. Can be used to monitor compliance of resources with rules.
2. Can only be modified by the root account.
3. Good for ongoing compliance and remediation.

## Service Catalog
1. Can be used to standardize cloudformation templates and allow users to launch them.
    - enforce tagging
    - enforce resource requirements
    - limit deployments to certain regions
    - enable versioned deployments
    
## CloudWatch
1. Logs are near real time

## Codepipeline
1. Does not have the ability to create a new artifact store, must use an existing S3 bucket.
2. Cannot make HTTP requests to external services.

## CloudFormation
1. iam:PassRole is used to allow a resource to assume a role.
2. Good for deploying or updating resources across multiple account in a templated matter. Ideal for initial setup and bulk updates but can lack granularity.

### Stack Template

AWSTemplateFormatVersion: '2010-09-09'
Description: Example CloudFormation to create an EC2 instance and IAM user with EC2 read access.

Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-0abcdef1234567890 # Specify a valid AMI ID for your region
      InstanceType: t2.micro
      KeyName: my-key-pair # Specify your EC2 Key Pair for SSH access

  EC2ReadOnlyPolicy:
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: EC2ReadOnlyAccess
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Action: ec2:Describe*
            Resource: '*'
      Users:
        - Ref: IAMUser

  IAMUser:
    Type: AWS::IAM::User
    Properties:
      UserName: EC2ReadOnlyUser

Outputs:
  InstanceId:
    Description: The Instance ID of the EC2 instance
    Value: !Ref MyInstance
  IAMUserName:
    Description: IAM User with EC2 read-only access
    Value: !Ref IAMUser

### Nested Stack
- TemplateURL is used to specify the location of the nested stack
- Parameters are used to pass parameters to the nested stack
- Outputs are used to pass outputs from the nested stack to the parent stack (!GetAtt NestedStack.Outputs.OutputName)

AWSTemplateFormatVersion: '2010-09-09'
Description: Main stack that nests VPC and EC2 instance stacks.

Resources:
  VPCStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/mybucket/vpc-stack.yaml
      Parameters:
        # Add any parameters required by the VPC stack

  EC2Stack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/mybucket/ec2-stack.yaml
      Parameters:
        VPCId: !GetAtt VPCStack.Outputs.VPCId
        # Add any other parameters required by the EC2 stack

Outputs:
  VPCId:
    Description: The ID of the VPC
    Value: !GetAtt VPCStack.Outputs.VPCId

  EC2InstanceId:
    Description: The ID of the EC2 instance
    Value: !GetAtt EC2Stack.Outputs.InstanceId

