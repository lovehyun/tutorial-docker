import boto3
import json

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html

def setup_bob_track(track=None):
    dev_session = boto3.session.Session(profile_name='kitribob.dev')
    vapt_session = boto3.session.Session(profile_name='kitribob.vapt')    
    consult_session = boto3.session.Session(profile_name='kitribob.consult')
    df_session = boto3.session.Session(profile_name='kitribob.df')

    # boto3.setup_default_session(profile_name='kitribob.vapt')

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


def region_check(current_session, region=["ALL"]):
    ec2_client = current_session.client('ec2')
    all_regions = ec2_client.describe_regions()

    region_boundary = []
    if region[0] == "ALL":
        for r in all_regions['Regions']:
            region_boundary.append(r['RegionName'])
    else:
        region_boundary = region
    
    return region_boundary


def list_ec2_lowlevel(current_session, region=["ALL"]):
    region_boundary = region_check(current_session, region)
    print('=== EC2 List instances ===')
    for region_name in region_boundary:
        print(f'region_name: {region_name}')
        ec2 = current_session.resource('ec2', region_name=region_name)
        instances = ec2.meta.client.describe_instances()            
        for instance in instances['Reservations']:
            for inst in instance['Instances']:
                if "InstanceId" in inst:
                    print(inst['InstanceId'], end=" ")

                if "KeyName" in inst:
                    print(inst['KeyName'], end=" ")
                else:
                    print('-', end=" ")

                if "State" in inst:
                    print(inst['State'])


# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances
def list_ec2(current_session, region=["ALL"]):
    region_boundary = region_check(current_session, region)
    print('=== EC2 List instances ===')
    for region_name in region_boundary:
        print(f'region_name: {region_name}')
        ec2 = current_session.resource('ec2', region_name=region_name)
        for instance in ec2.instances.all():
            # print(instance)
            print("Id: {0}, Type: {1}, PublicIP: {2}, State: {3}".format(
                instance.id, instance.instance_type, instance.public_ip_address, instance.state))


def list_keypairs(current_session, region="ALL"):
    region_boundary = region_check(current_session, region)
    print('=== EC2 List keypairs ===')
    for region_name in region_boundary:
        print(f'region_name: {region_name}')
        ec2 = current_session.resource('ec2', region_name=region_name)
        for keypairs in ec2.key_pairs.all():
            # print(keypairs)
            print("Name: {0}".format(keypairs.key_name))


if __name__ == "__main__":
    client = setup_bob_track("dev")
    # REGION=['ALL']
    REGION=['ap-northeast-2']
    list_ec2(client, region=REGION)
    list_keypairs(client, region=REGION)
