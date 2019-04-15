"""
checking permissions for a user in AWS

Input Format:
                {
            "access_key":"?",
            "secret_access_key":"?"
                 }

? - replaced by access and secret keys
"""

import boto3
import botocore.exceptions as excep
import json
from flask import Flask, request

app = Flask(__name__)


# checking for permission for Iam roles..
def roles(acc_key, sec_key):
    read = True
    create = True
    update = True
    delete = True
    iam = boto3.client('iam', aws_access_key_id=acc_key,
                       aws_secret_access_key=sec_key)
    roles_response = {"roles": {}}

    try:
        iam.create_role(RoleName='test', AssumeRolePolicyDocument='temp')
    except excep.ClientError:
        create = False

    try:
        iam.get_role(RoleName='admin')
    except excep.ClientError:
        read = False

    try:
        iam.delete_role(RoleName='test')
    except excep.ClientError:
        delete = False

    try:
        iam.update_role(RoleName='test')
    except excep.ClientError:
        update = False

    if read:
        roles_response["roles"].update({"read_access": "true"})
    else:
        pass
    if create:
        roles_response["roles"].update({"create_access": "true"})
    else:
        pass
    if delete:
        roles_response["roles"].update({"delete_access": "true"})
    else:
        pass
    if update:
        roles_response["roles"].update({"update_access": "true"})
    else:
        pass

    if len(roles_response['roles']):
        pass
    else:
        roles_response["roles"].update({"Access": "restricted"})

    return json.dumps(roles_response)


# checking permission for policies
def policy(acc_key, sec_key):
    listp = True
    read = True
    create = True
    delete = True
    policy_response = {"policy": {}}
    iam = boto3.client('iam', aws_access_key_id=acc_key,
                       aws_secret_access_key=sec_key)
    try:
        iam.list_policies()
    except excep.ClientError as e:
        listp = False
    try:
        iam.create_policy(
            PolicyName='test',
            PolicyDocument='temp',
            Description='to check permission'
        )
    except excep.ClientError:
        create = False
    try:
        iam.get_policy(PolicyArn='aws:iam::aws:policy/test')
    except excep.ClientError:
        read = False
    try:
        iam.delete_policy(PolicyArn='aws:iam::aws:policy/test')
    except excep.ClientError:
        delete = False
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

    if read:
        policy_response["policy"].update({"read_access": "true"})
    else:
        pass
    if create:
        policy_response["policy"].update({"create_access": "true"})
    else:
        pass
    if delete:
        policy_response["policy"].update({"delete_access": "true"})
    else:
        pass
    if listp:
        policy_response["policy"].update({"list_access": "true"})
    else:
        pass

    if len(policy_response['policy']):
        pass
    else:
        policy_response["policy"].update({"Access": "restricted"})

    return json.dumps(policy_response)


# checking permission for S3
def s3(acc_key, sec_key):
    listbuc = True
    create = True
    delete = True
    s3_response = {"s3": {}}
    s3 = boto3.client('s3', aws_access_key_id=acc_key,
                      aws_secret_access_key=sec_key)
    try:
        s3.list_buckets()
    except excep.ClientError:
        listbuc = False
    try:
        s3.create_bucket(Bucket='test')
    except excep.ClientError:
        create = False
    try:
        s3.delete_bucket(Bucket='test')
    except excep.ClientError:
        delete = False

    if listbuc:
        s3_response["s3"].update({"list_buckets": "true"})
    else:
        pass
    if create:
        s3_response["s3"].update({"create_access": "true"})
    else:
        pass
    if delete:
        s3_response["s3"].update({"delete_access": "true"})
    else:
        pass

    if len(s3_response['s3']):
        pass
    else:
        s3_response["s3"].update({"Access": "restricted"})

    return json.dumps(s3_response)


# check permission for cloudtrail
def cloudtrail(acc_key, sec_key):
    create = True
    read = True
    delete = True
    ct_response = {"CloudTrail":{}}
    ctrail = boto3.client('cloudtrail', aws_access_key_id=acc_key,
                          aws_secret_access_key=sec_key)
    try:
        ctrail.describe_trails()
    except excep.ClientError:
        read = False
    try:
        ctrail.create_trail(
            Name='test',
            S3BucketName='test'
        )
    except excep.ClientError:
        create = False
    try:
        ctrail.delete_trail(
            Name='test'
        )
    except excep.ClientError:
        delete = False

    if read:
        ct_response["CloudTrail"].update({"read_access": "true"})
    else:
        pass
    if create:
        ct_response["CloudTrail"].update({"create_access": "true"})
    else:
        pass
    if delete:
        ct_response["CloudTrail"].update({"delete_access": "true"})
    else:
        pass

    if len(ct_response['CloudTrail']):
         pass
    else:
        ct_response["CloudTrail"].update({"Access": "restricted"})

    return json.dumps(ct_response)


# checking for service cloudWatch
def cloudwatch(acc_key, sec_key):
    read = True
    cwatch_response = {"CloudWatch": {}}
    clwatch = boto3.client('cloudwatch', aws_access_key_id=acc_key,
                           aws_secret_access_key=sec_key)
    try:
        clwatch.describe_alarms()
    except excep.ClientError:
        read = False

    if read:
        cwatch_response["CloudWatch"].update({"read_alarm_access": "true"})
    else:
        pass

    if len(cwatch_response['CloudWatch']):
        pass
    else:
        cwatch_response["CloudWatch"].update({"Access": "restricted"})

    return json.dumps(cwatch_response)


@app.route('/POST', methods=['POST'])
def apicall():
    # access_key = raw_input("Enter the access key..")
    # secret_key = raw_input("Enter the secret key..")
    keys = json.loads(request.data)
    access_key = keys.get("access_key")
    secret_key = keys.get("secret_access_key")

    role_res = roles(access_key, secret_key)
    pol_res = policy(access_key, secret_key)
    s3_res = s3(access_key, secret_key)
    cd_res = cloudtrail(access_key, secret_key)
    cw_res = cloudwatch(access_key, secret_key)

    res_list = [role_res, pol_res, s3_res, cd_res, cw_res]
    return str(res_list)


if __name__ == '__main__':
    app.debug = True
    app.run()
