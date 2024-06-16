import boto3
import json

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html

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


def list_ecr(current_session):
    ecr_client = current_session.client('ecr')
    response = ecr_client.describe_repositories()

    print('=== ECR ===')
    for repository in response['repositories']:
        print("  ", repository['repositoryArn'])


def delete_ecr(current_session, force=False):
    ecr_client = current_session.client('ecr')
    response = ecr_client.describe_repositories()

    print('=== ECR Repos ===')
    for repository in response['repositories']:
        print(repository['repositoryArn'])
        repo_name = repository['repositoryName']
        print('  + List ECR repo images')
        images = ecr_client.list_images(repositoryName=repo_name)
        imageTags = [tag['imageTag'] for tag in images['imageIds']]
        print("   ", imageTags)
        print('  - Delete ECR repository, ', repo_name)
        ecr_client.delete_repository(repositoryName=repo_name, force=force)


if __name__ == "__main__":
    client = setup_bob_track("dev")
    list_ecr(client)
    delete_ecr(client, force=True)
