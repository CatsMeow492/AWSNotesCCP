# Amazon RDS (Relational Database Service)

**Purpose:** Managed service for relational databases in the cloud.

**Features:**
- Automates backups, patching, scaling, replication.
- Supports MySQL, PostgreSQL, Oracle, SQL Server, MariaDB, Amazon Aurora.

**Benefits:** Simplifies database management, ensuring scalability and reliability.

# Amazon DynamoDB

**Purpose:** NoSQL database service for all scales.

**Features:**
- Consistent, single-digit millisecond latency.
- DynamoDB Accelerator (DAX) for up to 10x performance improvement.

**Use Cases:** Mobile, web, gaming, ad tech, IoT applications.

# Amazon DocumentDB

**Purpose:** Document database service compatible with MongoDB.

**Benefits:** Offers scalability, durability, security for MongoDB data management.

# Amazon Keyspaces (for Apache Cassandra)

**Purpose:** Managed Apache Cassandra-compatible database service.

**Benefits:** Ideal for applications needing Cassandra's flexible schema and high availability.

# Amazon Quantum Ledger Database (QLDB)

**Purpose:** Fully managed ledger database.

**Features:** Provides an immutable, cryptographically verifiable transaction log.

**Use Cases:** Applications requiring accurate, complete transaction records.

# AWS Outposts

**Purpose:** Extends AWS infrastructure to on-premises.

**Benefits:** Offers consistent hybrid experience for low latency or local data processing workloads.

# AWS Dedicated Host

**Purpose:** Physical server fully dedicated for your use.

**Benefits:** Meets specific compliance requirements; ideal for licensed software.

# AWS Simple Queue Service (SQS)

**Purpose:** Fully managed message queuing service.

**Features:** Standard and FIFO queues.

**Use Cases:** Decouples and scales microservices, distributed systems, serverless applications.

# Security Services Overview

- Amazon GuardDuty: Threat detection for AWS accounts and workloads.
- AWS Shield: DDoS protection. Standard (common attacks) and Advanced (enhanced protection).
- AWS WAF (Web Application Firewall): Protects web apps from common exploits.
- AWS Firewall Manager: Central management for AWS WAF, Shield, and VPC security groups.
- Amazon Inspector: Automated security assessment for AWS applications.
- Amazon Macie: Machine learning for discovering and protecting sensitive data.
- AWS Key Management Service (KMS): Manages cryptographic keys.
- AWS Identity and Access Management (IAM): Manages access and permissions.

# AWS Support and Security Expertise

- AWS Support: Cloud Support Engineers, especially under the Enterprise plan.
- AWS Professional Services: Incident response, security expertise.
- AWS Marketplace: Third-party security solutions.

# Infrastructure Management and Compliance

- AWS CloudFormation: Manages AWS infrastructure using code.
- AWS OpsWorks: Configuration management using Chef and Puppet.
- AWS Artifact: Access to AWS security and compliance reports.
- AWS Config: Detailed view of AWS resource configurations.
- AWS CloudTrail: History of AWS API calls.
- AWS Security Hub: Comprehensive view of security alerts and posture.

# Amazon S3 Storage Classes

- S3 Standard: General-purpose storage with high availability.
- S3 Standard-IA: Less frequently accessed data, rapid access needed.
- S3 Intelligent-Tiering: Auto-moves data to cost-effective tiers.
- S3 One Zone-IA: Single AZ storage for infrequently accessed data.
- S3 Glacier & Glacier Deep Archive: For long-term data archiving.

# AWS Cloud Adoption Framework (CAF)

**Perspectives:** Business, People, Governance, Platform, Security, Operations.

**Purpose:** Guides cloud transformation with best practices and resources.

# Migration Strategies (7 R's)

**Strategies:** Rehost, Replatform, Repurchase, Refactor/Re-architect, Retire, Retain, Remediate.

# AWS Well-Architected Framework Five Pillars

**Pillars:** Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization.

# AWS Services for Specific Functions

**Chatbots:** Amazon Lex, Amazon Connect.

**Machine Learning:** Amazon SageMaker, Comprehend, Rekognition, Forecast, Personalize, Textract, Fraud Detector.

# AWS Direct Connect

**Purpose:** Dedicated network connection to AWS.

**Benefits:** Ideal for latency-sensitive or high-data-transfer applications.

# AWS Snow Family

**Purpose:** Physical devices for large data transfers into/out of AWS.

**Use Cases:** Data migration, disaster recovery.

# AWS CloudWatch

**Purpose:** Monitoring and observability service.

**Features:**
- CloudWatch Logs: Collects, monitors, analyzes log data.
- CloudWatch Events: Monitors events and triggers automated responses.
- CloudWatch Metrics: Collects and tracks metrics.

# AWS CloudTrail

**Purpose:** Records AWS API calls for auditing and compliance.

**Features:**
- CloudTrail Insights: Detects unusual activity.
- CloudTrail Event History: View, search, download recent events.
- CloudTrail Insights Event History: View, search, download unusual activity events.

# AWS CloudFront

**Purpose:** CDN

**Benefits:** Improves performance, reduces latency, lowers network traffic.

**Use Cases:** Static and dynamic content, streaming media, APIs.

# Amazon Machine Image

**Purpose:** Template for virtual servers.

**Features:**
- Public AMIs: Created by AWS or the community.
- Private AMIs: Created by you.

# AWS Marketplace

**Purpose:** Online store for third-party software.

**Benefits:** Simplifies software licensing and procurement.

# AWS Cost Explorer

**Purpose:** Analyzes AWS costs and usage.

**Features:**
- Cost Explorer: Analyzes costs and usage.
- Budgets: Tracks costs and usage against budgets.
- Cost and Usage Reports: Detailed cost and usage data.

# AWS Trusted Advisor

**Purpose:** Provides best practices for AWS infrastructure.

**Features:**
- Cost Optimization: Analyzes costs and usage.
- Performance: Analyzes application performance.
- Security: Analyzes security settings.
- Fault Tolerance: Analyzes fault tolerance.
- Service Limits: Analyzes service limits.

# AWS Organizations

**Purpose:** Manages multiple AWS accounts.

**Features:**
- Consolidated Billing: Single bill for all accounts.
- Service Control Policies: Sets controls for accounts.
- Organizational Units: Groups accounts for easier management.

# AWS Resource Access Manager

**Purpose:** Shares AWS resources across accounts.

**Benefits:** Simplifies resource sharing across accounts.

# AWS CloudHSM

**Purpose:** Hardware security module (HSM) for key storage and management.

**Benefits:** Ideal for compliance requirements.

# AWS CodeStar

**Purpose:** Develops, builds, deploys, and manages applications.

**Features:**
- CodeStar Projects: Develops, builds, deploys, and manages applications.
- CodeStar Connections: Connects to third-party tools.
- CodeStar Notifications: Sends notifications for events.

# AWS CodeCommit

**Purpose:** Source control service.

**Benefits:** Ideal for collaboration and code review.

# AWS CodeBuild

**Purpose:** Compiles source code, runs tests, produces software packages.

**Benefits:** Ideal for continuous integration and continuous delivery (CI/CD).

# AWS CodeDeploy

**Purpose:** Automates application deployments.

**Benefits:** Ideal for rapid, reliable application deployments.

# AWS CodePipeline

**Purpose:** Continuous delivery service.

**Benefits:** Ideal for automating software release processes.

# AWS CodeArtifact

**Purpose:** Software artifact repository.

**Benefits:** Ideal for securely storing, publishing, sharing software packages.

# AWS CodeGuru

**Purpose:** Automated code reviews and application performance recommendations.

**Benefits:** Ideal for improving code quality and identifying application performance issues.

# Shared Responsibility Model Overview
- Hardware, Software, Networking, Facilities: AWS
- Identity and Access Management, OS, Firewall, Network Configuration: Customer

# Containers Overview
- Amazon Elastic Container Service (ECS): Managed container orchestration service.
- Amazon Elastic Kubernetes Service (EKS): Managed Kubernetes service.
- AWS Fargate: Serverless compute engine for containers.
- Essential concept in microservice architectures.
- AMI: Amazon Machine Image. Template for virtual servers.

# Locations Overview
- AWS Regions: Geographical areas with multiple Availability Zones.
- AWS Availability Zones: One or more discrete data centers.
- AWS Local Zones: Edge locations for low-latency applications.
- AWS Wavelength Zones: Edge locations for 5G applications.

# AWS Global Infrastructure
- 24 Regions
- 77 Availability Zones
- 220+ Edge Locations

# Support Plans Overview
- Basic: Free
- Developer: $29/month
- Business: $100/month
- Enterprise: $15,000/month

# Basic
- 24/7 customer service
- Access to documentation, whitepapers, support forums
- Access to AWS Trusted Advisor

# Developer
- All Basic features
- 1-hour response time for urgent issues
- 24/7 phone, email, chat support
- Access to AWS Support API

# Business
- All Developer features
- 1-hour response time for urgent issues
- 24/7 phone, email, chat support
- Access to AWS Support API
- Infrastructure event management
- Concierge support team

# Enterprise
- All Business features
- 15-minute response time for urgent issues
- 24/7 phone, email, chat support
- Access to AWS Support API
- Infrastructure event management
- Concierge support team
- Technical account manager
- Well-Architected reviews

# Data Migration Overview
- AWS Snow Family: Physical devices for large data transfers into/out of AWS.
- AWS DataSync: Online data transfer service.
- AWS Transfer Family: Fully managed SFTP, FTPS, FTP service.
- AWS Database Migration Service (DMS): Migrates databases to AWS.
- AWS Server Migration Service (SMS): Migrates on-premises servers to AWS.
- AWS Application Discovery Service: Discovers on-premises applications.
- AWS Application Migration Service: Migrates on-premises applications to AWS.

# AWS Snow Family
- AWS Snowcone: Rugged, portable device for edge computing and data transfer.
- AWS Snowball: Petabyte-scale data transport solution.
- AWS Snowmobile: Exabyte-scale data transfer service.

# VPC Overview
- Virtual Private Cloud (VPC): Virtual network in AWS.
- Subnet: Range of IP addresses in a VPC.
- Route Table: Routes traffic between subnets.
- Internet Gateway: Connects VPC to the Internet.
- NAT Gateway: Connects VPC to the Internet for private subnets.
- Virtual Private Gateway: Connects VPC to on-premises network.
- VPC Endpoint: Connects VPC to AWS services.
- VPC Peering: Connects two VPCs.



