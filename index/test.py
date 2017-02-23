import boto3

def lambda_handler(event, context):

    print(boto3.__version__)
    # TODO implement
    #1850bf7b-af0c-40c6-a480-00aeda2a2966

    session = boto3.session.Session()
    ecsClient = session.client(service_name='ecs')
    ecsResponse = ecsClient.update_container_instances_state(cluster='ecs-cd-Cluster-QPJZXE8U4HDM',containerInstances=['1850bf7b-af0c-40c6-a480-00aeda2a2966'],status='DRAINING')
    print ("Response = " , ecsResponse)

    return 'Hello from Lambda'
