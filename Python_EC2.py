import boto3

# Initialize EC2 client
ec2_client = boto3.client("ec2", region_name="us-east-1")


def list_instances():
    """Lists all running EC2 instances"""
    response = ec2_client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(
                f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}"
            )


def start_instance(instance_id):
    """Starts an EC2 instance"""
    ec2_client.start_instances(InstanceIds=[instance_id])
    print(f"Starting instance: {instance_id}")


def stop_instance(instance_id):
    """Stops an EC2 instance"""
    ec2_client.stop_instances(InstanceIds=[instance_id])
    print(f"Stopping instance: {instance_id}")


if __name__ == "__main__":
    print("AWS EC2 Connection Established")
    list_instances()

    # Uncomment the following lines to start/stop an instance
    # instance_id = "your-instance-id-here"
    # start_instance(instance_id)
    # stop_instance(instance_id)
