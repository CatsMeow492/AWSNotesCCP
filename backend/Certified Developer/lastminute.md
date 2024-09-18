Prompt: I need you to act as a study helper for the AWS DVA-C02 exam. Your answers should be concsise and emphasize EASY TO REMEMBER for last minute studying. Please me sure to include any acronyms, rhymes, or analagies you know if possible.

# AWS DVA-C02 Exam Study Notes

## ETL Workload
- **E**xtract, **T**ransform, **L**oad
- Collects data from various sources, transforms it according to business rules, and loads it into a destination data store
- Common in data warehousing and data integration

## Elasticache
- Ideal for compute-intensive and read-heavy workloads
- Fully managed in-memory data store and cache service by AWS
- Compatible with Redis and Memcached

## Services that Rely on CloudFormation to Provision Resources
- Elastic Beanstalk
- AWS SAM

## ALB (Application Load Balancer)
- 3 target types: EC2, Lambda, IP
- Cannot specify public IP addresses
- Designed for HTTP/HTTPS traffic
- Offers advanced routing targeted at web applications
- Supports features like content-based routing, HTTP/2 and WebSocket support, and the ability to route requests to multiple services or containers

## Load Balancers
- **ELB (Elastic Load Balancer)**: Basic load balancing across multiple EC2 instances. Often referred to as Classic Load Balancer
- **ALB (Application Load Balancer)**: Optimized for advanced load balancing of HTTP/HTTPS traffic, ideal for modern web applications
- **NLB (Network Load Balancer)**: Operates at the Transport Layer (Layer 4 of OSI model), suitable for TCP, UDP, and TLS traffic where high performance and low latency are required

### Key Differences
- **Use Case**
    - ELB: Basic load balancing of HTTP/HTTPS and TCP traffic
    - ALB: Advanced load balancing of HTTP/HTTPS traffic, ideal for modern web applications
    - NLB: High-performance, low-latency load balancing of TCP/UDP/TLS traffic, suitable for any type of application
- **Performance and Latency**
    - NLB: Highest performance and lowest latency, capable of handling volatile traffic patterns and millions of requests per second
    - ALB: Robust performance with application-level (Layer 7) features
    - ELB: Basic performance capabilities suitable for early AWS applications
- **Features**
    - ALB: Supports advanced routing, multiple HTTP/HTTPS features, and integration with AWS services like ECS
    - NLB: Supports static IP or Elastic IP addresses and is used for extreme performance scenarios
    - ELB: Provides basic load balancing across AWS services

## AWS Elastic Beanstalk Environments
- Supports two main types of environments tailored to different deployment and management needs: Web Server Environments and Worker Environments.

### 1. Web Server Environments
- Purpose: Designed to host web applications accessible over the Internet. These environments manage the deployment of applications onto servers that can handle HTTP(S) requests.
- Use Cases: Ideal for running web applications or services that respond to web browser requests. Typically used for hosting websites, RESTful APIs, or any application that serves web content.
- Configuration: Can be configured with a variety of AWS resources, including Amazon EC2 instances, Auto Scaling groups, Amazon RDS databases, and load balancers (either Application Load Balancer, Network Load Balancer, or Classic Load Balancer).

### 2. Worker Environments
- Purpose: Optimized for background processing tasks that can be triggered by HTTP POST requests or periodic tasks. Worker environments listen for messages from an Amazon SQS queue; when a message is received, it sends an HTTP POST request to a specified endpoint in your application, processing the task.
- Use Cases: Suitable for asynchronous workloads, such as processing uploaded files, performing intensive computations, sending batch emails, or handling long-running tasks that don't need to immediately respond to user requests.
- Configuration: Typically involves setting up an Amazon SQS queue for task messages and an Auto Scaling group of Amazon EC2 instances configured to process these tasks. Unlike web server environments, worker environments do not require a publicly accessible endpoint.

### Key Differences
- Accessibility: Web server environments are publicly accessible and designed to respond to direct web requests, whereas worker environments are designed for internal background processing tasks.
- Trigger Method: Web servers are triggered by HTTP(S) requests, while worker environments are triggered by messages in an Amazon SQS queue.
- Primary Use: Web servers for serving web pages or APIs directly to users; workers for processing tasks asynchronously in the background.

## DynamoDB
- Optimistic locking
- DynamoDB transactions provide a way to group multiple actions across one or more tables into a single, all-or-nothing operation. This capability ensures that either all the actions in the transaction are completed successfully or none of them are applied, maintaining data integrity and consistency. Transactions in DynamoDB support two key operations: TransactWriteItems and TransactGetItems
- Max item size: 400 KB
- Streams can directly invoke a Lambda function

User Data in EC2
What It Is: User Data is used to automate software installations, run shell scripts, or perform other configuration tasks when your instance boots for the first time.
How to Use: You can specify user data at the instance launch. The script runs as the root user, allowing you to install software, update settings, configure users, or do anything else you might manually configure.