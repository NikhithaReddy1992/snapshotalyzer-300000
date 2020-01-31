# snapshotalyzer-300000
Demo project to manage AWS EC2 snapshot

#About

this project is a demo and uses boto3 to manage AWS EC2 instance snapshots


#cofniguration
shotty uses the configuration file created by the AWS CLI

'aws configure --profile shotty'





##Running
'pipenv run python shotty/shotty.py <command> <sub-command> <--project=PROJECT'-->

*command* is instances and volumes
*sub-command* list for volumes and list, start, stop and snapshot for instances
*project* is optional
