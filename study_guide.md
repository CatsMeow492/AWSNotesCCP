Sure, I'll create a short study guide for you in Markdown format to help you better understand the process of sharing an encrypted AMI across AWS accounts, focusing on using Amazon EC2 and AWS Key Management Service (AWS KMS).

```markdown
# AWS AMI Sharing and Encryption Guide

Understanding how to securely share AMI (Amazon Machine Images) across AWS accounts while ensuring they are encrypted is crucial for maintaining data security and compliance. This guide covers the key concepts and steps involved in this process, focusing on AWS Key Management Service (AWS KMS) and Amazon EC2.

## Key Concepts

- **AMI (Amazon Machine Image):** A template that contains a software configuration (operating system, application server, applications) used to create virtual machines (instances) in AWS.

- **Encryption:** The process of converting data into a coded format that is not easily accessible by unauthorized users.

- **AWS Key Management Service (AWS KMS):** A managed service that makes it easy for you to create and manage cryptographic keys used for data encryption.

- **Cross-Account Sharing:** The ability to share AWS resources, such as AMIs, with other AWS accounts.

## Steps to Share an Encrypted AMI Across Accounts

When sharing an encrypted AMI across accounts, specifically from a source account to a target account, follow these steps:

1. **Encrypt the AMI**: 
   
   First, if your AMI is not already encrypted, you'll need to encrypt it using an AWS KMS key. You can do this by creating a copy of the AMI and selecting an AWS KMS key during the copy process.

2. **Share the KMS Key**:
   
   The AWS KMS key used to encrypt the AMI must be shared with the target account. This allows the target account to use the encrypted AMI.
   
   - Go to AWS KMS in the AWS Management Console.
   - Select the KMS key that you used to encrypt the AMI.
   - Under the "Key policy" section, add the target account as a principal, allowing it to use the key.

3. **Share the AMI**:

   After encrypting the AMI and sharing the KMS key, you need to share the AMI itself with the target account.
   
   - Go to the EC2 Dashboard in the source account.
   - Find the AMI you want to share, and select the option to modify its permissions.
   - Add the target account by its AWS account ID and save the changes.

4. **Launch Instances in the Target Account**:

   Now that the AMI is shared and the target account has access to use the KMS key, instances can be launched in the target account using the AMI.
   
   - Go to the EC2 Dashboard in the target account.
   - Find the shared, encrypted AMI under "AMIs".
   - Launch EC2 instances as needed.

## Best Practices

- Always ensure that the proper IAM roles and permissions are in place for both source and target accounts to perform necessary actions.
- Consider automating the sharing process using AWS CLI or SDKs for scalability and efficiency.
- Regularly audit your shared AMIs and AWS KMS keys to ensure that only intended accounts have access.

This guide provides a starting point for sharing encrypted AMIs across AWS accounts. For specific requirements and advanced scenarios, always refer to the official AWS documentation.

```

Remember, the guidance provided here is simplified for understanding. You should tailor the steps based on your organization's specific setup and security policies. If you have further questions or need additional details, feel free to ask!