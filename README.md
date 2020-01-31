# snapshotalyzer-300000
Demo project to manage AWS EC2 snapshot

#About

this project is a demo and uses boto3 to manage AWS EC2 instance snapshots


#cofniguration
shotty uses the configuration file created by the AWS CLI

'aws configure --profile shotty'

##Running

'pipenv run python shotty/shotty.py <command> <--project=PROJECT-->'

*command* is list,start and stop
*project* is optional
