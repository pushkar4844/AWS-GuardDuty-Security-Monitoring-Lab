import boto3
import json

def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2))

    # Extract relevant data from GuardDuty finding
    try:
        detail = event['detail']
        instance_id = detail['resource']['instanceDetails']['instanceId']
        attacker_ip = detail['service']['action']['networkConnectionAction']['remoteIpDetails']['ipAddressV4']
    except KeyError as e:
        print(f"Missing expected key: {e}")
        return {"status": "error", "reason": str(e)}

    # Tag the EC2 instance
    ec2 = boto3.client('ec2')
    try:
        ec2.create_tags(
            Resources=[instance_id],
            Tags=[
                {'Key': 'Status', 'Value': 'Compromised'},
                {'Key': 'AttackerIP', 'Value': attacker_ip}
            ]
        )
        print(f"Tagged instance {instance_id} as compromised.")
    except Exception as e:
        print(f"Failed to tag instance: {e}")

    return {"status": "success", "instance_id": instance_id, "attacker_ip": attacker_ip}
