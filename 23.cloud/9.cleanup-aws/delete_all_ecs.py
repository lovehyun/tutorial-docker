import boto3
import json

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html

def setup_bob_track(track=None):
    dev_session = boto3.session.Session(profile_name='kitribob.dev')
    vapt_session = boto3.session.Session(profile_name='kitribob.vapt')    
    consult_session = boto3.session.Session(profile_name='kitribob.consult')
    df_session = boto3.session.Session(profile_name='kitribob.df')

    if track == "dev":
        current_session = dev_session
    if track == "vapt":
        current_session = vapt_session
    if track == "consult":
        current_session = consult_session
    if track == "df":
        current_session = df_session

    if track is None:
        raise ValueError

    return current_session
   

def list_ecs(current_session):
    print('=== ECS ===')
    ecs_client = current_session.client('ecs')
    paginator = ecs_client.get_paginator('list_clusters')
    page_iterator = paginator.paginate()
    for page in page_iterator:
        for cluster_arn in page['clusterArns']:
            print("  ", cluster_arn)


def delete_ecs(current_session):
    print('=== ECS ===')
    ecs_client = current_session.client('ecs')
    paginator = ecs_client.get_paginator('list_clusters')
    page_iterator = paginator.paginate()
    for page in page_iterator:
        for cluster_arn in page['clusterArns']:
            cluster_name = cluster_arn.split('/')[1]
            print(cluster_name)

            print('  + ECS list services')
            paginator = ecs_client.get_paginator('list_services')
            page_iterator = paginator.paginate(cluster=cluster_name)
            for page in page_iterator:
                for service_arn in page['serviceArns']:
                    print("   ", service_arn)
                    service_name = service_arn.split('/')[-1]
                    print('  - ECS delete services, ', service_name)
                    ecs_client.update_service(cluster=cluster_name, service=service_name, desiredCount=0)
                    ecs_client.delete_service(cluster=cluster_name, service=service_name)

            print('  + ECS list tasks')
            paginator = ecs_client.get_paginator('list_tasks')
            page_iterator = paginator.paginate(cluster=cluster_name)
            for page in page_iterator:
                for task_arn in page['taskArns']:
                    print("   ", task_arn)
                    task_name = task_arn.split('/')[-1]
                    print('  - ECS delete tasks', task_name)
                    ecs_client.stop_task(cluster=cluster_name, task=task_arn)

            print('  + ECS list containers')
            paginator = ecs_client.get_paginator('list_container_instances')
            page_iterator = paginator.paginate(cluster=cluster_name)
            for page in page_iterator:
                for container_arn in page['containerInstanceArns']:
                    print("   ", container_arn)
                    container_name = container_arn.split('/')[-1]
                    print('  - ECS delete container instance', container_name)
                    ecs_client.deregister_container_instance(cluster=cluster_name, containerInstance=container_arn)


def list_ecs_task_definition(current_session):
    ecs_client = current_session.client('ecs')
    print('=== ECS Task Definition Families ===')
    paginator = ecs_client.get_paginator('list_task_definition_families')
    response_iterator = paginator.paginate()
    for each_page in response_iterator:
        print(each_page['families'])


def delete_ecs_task_definition(current_session):
    ecs_client = current_session.client('ecs')
    print('=== ECS Task Definitions ===')
    paginator = ecs_client.get_paginator('list_task_definitions')
    response_iterator = paginator.paginate()
    for each_page in response_iterator:
        for each_task in each_page['taskDefinitionArns']:
            print(each_task)
            print('  - DELETE taskDefinitionArns, ', each_task)
            response = ecs_client.deregister_task_definition(taskDefinition=each_task)
            # print(json.dumps(response, indent=4, default=str))
            print("   ", response['taskDefinition']['taskDefinitionArn'], response['ResponseMetadata']['HTTPStatusCode'])


def delete_ecs_clusters(current_session):
    ecs_client = current_session.client('ecs')
    print('=== DELETE ECS Clusters ===')
    paginator = ecs_client.get_paginator('list_clusters')
    page_iterator = paginator.paginate()
    for page in page_iterator:
        for cluter_arn in page['clusterArns']:
            cluster_name = cluter_arn.split('/')[1]
            print('  - DELETE cluters, ', cluster_name)
            response = ecs_client.delete_cluster(cluster=cluster_name)
            # print(json.dumps(response, indent=4))
            print("   ", response['cluster']['clusterArn'], response['ResponseMetaata']['HTTPStatusCode'])


if __name__ == "__main__":
    client = setup_bob_track("dev")
    list_ecs(client)
    delete_ecs(client)
    list_ecs_task_definition(client)
    delete_ecs_task_definition(client)
    delete_ecs_clusters(client)
