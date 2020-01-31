import boto3
import click

session=boto3.Session(profile_name='shotty')
ec2=session.resource('ec2')

def filter_instances(project):
    instances=[]
    if project:
        filters=[{'Name':'tag:project','Values':[project]}]
        instances=ec2.instances.filter(Filters=filters)
    else:
        instances= ec2.instances.all()
    return instances
@click.group()
def instances():
    """commands for instances"""

@instances.command('list')
@click.option('--project',default=None,help="only instances for project(tag project:<name>)")
def list_instances(project):
    "List Ec2 instances"
    instances=filter_instances(project)
    for i in instances:
        tags={t['Key']:t['Value'] for t in i.tags or[]}
        print(','.join((i.id,
        i.instance_type,
        i.placement['AvailabilityZone'],
        i.state['Name'],
        i.public_dns_name,
        tags.get('project','<no project>'))))
@instances.command('stop')
@click.option('--project',default=None,help="only instances for project(tag project:<name>)")
def stop_instances(project):
    "Stop Ec2 instances"
    instances=filter_instances(project)
    for i in instances:
        print("Stopping {0}....".format(i.id))
        i.stop()
@instances.command('start')
@click.option('--project',default=None,help="only instances for project(tag project:<name>)")
def start_instances(project):
    "Start EC2 instances"
    instances=filter_instances(project)
    for i in instances:
        print("Starting {0}....".format(i.id))
        i.start()
if __name__ =='__main__':
    instances()
