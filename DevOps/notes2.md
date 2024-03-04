# AWS Study Guide

## AWS Web Application Firewall (WAF) and AWS Config

### Context: Ensuring ALBs and API Gateway APIs are associated with AWS WAF web ACLs

- **AWS WAF**: Protects web applications from common web exploits. Allows control over application traffic to mitigate risks like SQL injection and XSS.
- **AWS Config**: Assesses, audits, and evaluates AWS resource configurations. Ensures compliance and monitors configurations against security policies.
- **Key Concepts**:
  - **Automating Security Best Practices**: Use AWS Config to ensure ALBs and API Gateway instances comply with security policies by associating them with WAF web ACLs.
  - **AWS Firewall Manager**: Centrally manage WAF rules across AWS Organization, simplifying administration and ensuring consistent security posture.

## AWS CodePipeline, CodeBuild, and CodeDeploy

### Context: Automating deployments with CodePipeline, CodeBuild, and CodeDeploy

- **AWS CodePipeline**: Automates CI/CD processes for reliable application updates.
- **AWS CodeBuild**: Compiles source code, runs tests, and produces ready-to-deploy software packages.
- **AWS CodeDeploy**: Automates application deployments to various compute services including EC2, Lambda, and on-premises servers.
- **Key Concepts**:
  - **Deployment Automation**: Integrating CodeDeploy with CodePipeline for automated deployments, ensuring consistent updates.
  - **Preparation for Deployment**: Target EC2 instances must have the CodeDeploy agent and appropriate IAM roles for successful deployment.

## AWS IAM Identity Center and Permission Models

### Context: Implementing robust permission models with AWS IAM Identity Center and SAML 2.0

- **AWS IAM Identity Center (AWS SSO)**: Centralizes user access management across AWS accounts and applications, integrating with corporate credentials.
- **Principle of Least Privilege**: Minimizes risk by ensuring users and services have only necessary permissions.
- **Key Concepts**:
  - **Granular Permission Control**: Utilize IAM policies, permission sets, and tags for detailed access control based on roles and resource management needs.
  - **External Identity Integration**: Leverages SAML 2.0 for seamless integration with external IdPs, simplifying user management and enhancing security.

## AWS CodeCommit and CodePipeline Integration

### Context: Troubleshooting CodePipeline not triggered by CodeCommit changes

- **AWS CodeCommit**: Hosts secure Git-based repositories for team collaboration.
- **AWS CodePipeline Triggers**: Can be set to react to source code changes, such as commits to a specified branch.
- **Key Concepts**:
  - **EventBridge Integration**: Ensure Amazon EventBridge is set up to detect CodeCommit changes and trigger CodePipeline.
  - **Permission Checks**: Verify CodePipeline service role permissions for accessing CodeCommit and proper pipeline configuration for source repository events.
