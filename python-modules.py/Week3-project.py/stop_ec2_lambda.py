import boto3


def lambda_handler(event,context):
    ec2 = boto3.client('ec2')

    running_instances = []

    instances = ec2.describe_instance(
        filter = [
            {'Name': 'instance-status', 'values': ['running']}
        ]
    )

    for reservation in instances['Reservations']:
        for instance in reservation ['Instances']:
            print(instance['InstanceID'])
            running_instances.append(instance['InstanceID'])

    response = ec2.stop_instances(InstanceID = running_instances)

    print(response)

    #TODO implement
    return {
        'StatusCode': 200,
        'body': response
    }         
