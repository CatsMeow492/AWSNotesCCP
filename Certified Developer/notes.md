# Amazon Elastic Container Service on Fargate
- Highly scalable, fast and secure container management service that allows you to run containers without having to manage servers or clusters
- Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS)
    - Fargate makes it easy for you to focus on building your applications
    - Fargate removes the need to provision and manage servers, lets you specify and pay for resources per application

# Security Groups
- Security groups are stateful
    - If you allow inbound traffic, that traffic is automatically allowed back out again
- All inbound traffic is blocked by default
- All outbound traffic is allowed
- Changes to security groups take effect immediately
- You can have any number of EC2 instances within a security group
- You can have multiple security groups attached to EC2 instances
- Security groups are locked down to a region/VPC combination
- You can have multiple security groups within a VPC
- Security groups can reference by IP or by security group
- Not suited for S3 or CloudFront

# AWS CLI
## Command Structure
- aws <service> <command> <subcommand> [parameters] [options] [output options]
### S3
- aws s3 ls
- aws s3 cp <source> <destination>
- aws s3 mb <bucket name>
- aws s3 rb <bucket name>
- aws s3 rm <bucket name> --recursive
- aws s3 sync <source> <destination> --delete
- aws s3 website <bucket name> --index-document index.html --error-document error.html
### EC2
- aws ec2 describe-instances
- aws ec2 describe-images
- aws ec2 describe-key-pairs
- aws ec2 describe-security-groups
- aws ec2 describe-vpcs
- aws ec2 describe-subnets
- aws ec2 describe-route-tables
### IAM
- aws iam list-users
- aws iam list-roles
- aws iam list-groups
- aws iam list-policies
- aws iam list-attached-user-policies --user-name <user name>
- aws iam list-attached-role-policies --role-name <role name>
- aws iam list-attached-group-policies --group-name <group name>
- aws iam get-user --user-name <user name>
- aws iam get-role --role-name <role name>
### Lambda
- aws lambda list-functions
- aws lambda list-event-source-mappings
- aws lambda list-layers
- aws lambda list-aliases
- aws lambda list-versions-by-function --function-name <function name>
- aws lambda list-tags --resource <function arn>
- aws lambda list-permission --function-name <function name>
- aws lambda list-code-signing-configs
- aws lambda list-provisioned-concurrency-configs
- aws lambda list-functions-by-code-signing-config --code-signing-config-arn <code signing config arn>
### CloudFormation
- aws cloudformation list-stacks
- aws cloudformation list-stack-sets
- aws cloudformation list-stack-instances
- aws cloudformation list-stack-set-operation-results
- aws cloudformation list-change-sets --stack-name <stack name>
- aws cloudformation list-exports
- aws cloudformation list-import-jobs
- aws cloudformation list-types
- aws cloudformation list-type-registrations
- aws cloudformation list-type-versions
- aws cloudformation list-resource-types
- aws cloudformation list -stack-resources --stack-name <stack name>
- aws cloudformation list-stack-set-operation-results --stack-set-name <stack set name>

# Types of APIs
## REST APIs
- REST APIs are stateless
- REST APIs are cacheable
- REST APIs typically use JSON
- REST APIs are defined by HTTP methods
    - GET
    - POST
    - PUT
    - PATCH
    - DELETE
- REST APIs are self-descriptive
- REST APIs are hypermedia-driven
- REST APIs allow you to decouple the client from the server
## WebSocket APIs
- WebSocket APIs are stateful
- WebSocket APIs are not cacheable
- WebSocket APIs typically use JSON
- WebSocket APIs are defined by WebSocket protocol
- WebSocket APIs are not self-descriptive
- WebSocket APIs are not hypermedia-driven
- WebSocket APIs allow you to decouple the client from the server
