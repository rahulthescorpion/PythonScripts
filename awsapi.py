"""
checking permissions for a user in AWS
"""

import boto3
import botocore.exceptions as excep

# permission strings
readp = "permission granted for read"
createp = "permission granted for create"
updatep = "permission granted for update"
deletep = "permission granted for delete"
readpd = "permission denied for read"
createpd = "permission denied for create"
updatepd = "permission denied for update"
deletepd = "permission denied for delete"


# checking for permission for Iam roles..
def roles():
    iam = boto3.client('iam', aws_access_key_id='AKIA2NXFKTC6UZKRWNW5',
                       aws_secret_access_key='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')
    try:
        iam.create_role(RoleName='test', AssumeRolePolicyDocument='temp')
        print createp+" a role"
    except excep.ClientError:
        print createpd+" a role"

    try:
        single_role = iam.get_role(RoleName='admin')
        print readp+" a role"
    except excep.ClientError:
        print readpd+" a role"

    try:
        delete_role = iam.delete_role(RoleName='test')
        print deletep+" a role"
    except excep.ClientError:
        print deletepd+" a role"

    try:
        upd_role = iam.update_role(RoleName='test')
        print updatep+" a role"
    except excep.ClientError:
        print updatepd+" a role"


# checking permission for policies
def policy():
    iam = boto3.client('iam', aws_access_key_id='AKIA2NXFKTC6UZKRWNW5',
                       aws_secret_access_key='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')
    try:
        pol = iam.list_policies()
        print readp+" all policies"
    except excep.ClientError as e:
        print readpd+" the policies"
        # print e

    try:
        create_policy = iam.create_policy(
            PolicyName='test',
            PolicyDocument='temp',
            Description='to check permission'
        )
        print createp+ " a policy"
    except excep.ClientError:
        print createpd+" a policy"

    try:
        getpolicy = iam.get_policy(PolicyArn='aws:iam::aws:policy/test')
        print readp+" a policy"
    except excep.ClientError:
        print readpd+ " a policy"

    try:
        del_policy = iam.delete_policy(PolicyArn='aws:iam::aws:policy/test')
        print deletep+ " a policy"
    except excep.ClientError:
        print deletepd+ " a policy"
    """
    try:
        list_service_policies = iam.list_policies_granting_service_access(
            Arn='arn:aws:iam::aws:policy/ravishankar',
            ServiceNamespaces=['s3'])
        # print list_service_policies
        print "permission granted to check policies for services"
    except excep.ClientError:
        print "permission denied to check policies for services"
    """
# checking permission for S3
def s3():
    s3 = boto3.client('s3', aws_access_key_id='AKIA2NXFKTC6UZKRWNW5',
                      aws_secret_access_key='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')
    try:
        list_buc = s3.list_buckets()
        print readp+" all the buckets"
    except excep.ClientError:
        print readpd+" the buckets"

    try:
        create_buc = s3.create_bucket(Bucket='test')
        print createp+" a bucket"
    except excep.ClientError:
        print createpd+" a bucket"

    try:
        create_buc = s3.delete_bucket(Bucket='test')
        print deletep+" a bucket"
    except excep.ClientError:
        print deletepd+" a bucket"


# check permission for cloudtrail
def cloudtrail():
    ctrail = boto3.client('cloudtrail', aws_access_key_id='AKIA2NXFKTC6UZKRWNW5',
                          aws_secret_access_key='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')
    try:
        view_cloudtrail = ctrail.describe_trails()
        print readp+" all the trails"
    except excep.ClientError:
        print readpd+" about trails"

    try:
        cloud_create = ctrail.create_trail(
            Name='test',
            S3BucketName='test'
        )

        print createp+" a trail"
    except excep.ClientError:
        print createpd+" a trail"

    try:
        cloud_delete = ctrail.delete_trail(
            Name='test'
        )
        print deletep+" a trail"
    except excep.ClientError:
        print deletepd+" a trail"


# checking for service cloudWatch
def cloudwatch():
    clwatch = boto3.client('cloudwatch', aws_access_key_id='AKIA2NXFKTC6UZKRWNW5',
                           aws_secret_access_key='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')
    try:
        cloudwat = clwatch.describe_alarms()
        print "Reading permission is allowed for Cloudwatch"
    except:
        print "Reading permission is denied for Cloudwatch"


inp = raw_input("Enter the service to check the permission:")
if inp == 'roles':
    roles()
elif inp == 'policy':
    policy()
elif inp == 's3':
    s3()
elif inp == 'cloudtrail':
    cloudtrail()
elif inp == 'cloudwatch':
    cloudwatch()
else:
    print "Service not available.."

