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
### Dualstack
1. Supports both IPv4 and IPv6
2. EC2 instances must be added to the
target group
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
## S3
### Notes
1. Objects must be deleted before the bucket can be deleted, protections will prevent DeletionPolicy. This can be circumvented by using a lambda to delete objects before the bucket is deleted.
2. Can act as an artifact store for CodePipeline. Codepipeline must have permissions to access the bucket.
3. Can act as a static website host. The bucket must be public and the objects must be public.
4. Can store lambda code and be used to trigger lambda functions.
## OpsWorks
1. Autohealing can stop and restart instances that are not responding to health checks.
## IAM 
### Policy 
1. Can be used with conditionals to restrict access to resources based on tags.
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:DescribeInstances",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "ec2:ResourceTag/department": "${aws:PrincipalTag/department}"
        }
      }
    }
  ]
}
### Roles
1. Typically created in the account where the resource is located.
2. Cross-account access is handled by creating a role in the target account, setting the trust policy to the source account, and attaching a policy to the role that allows the source account to assume the role.