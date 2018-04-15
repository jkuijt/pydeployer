# pydeployer

Simple library for deploying local project files to a remote machine

### Installation
`pip install pydeployer`

### Usage
To upload your project to a server

`pydeployer <root dir>` for example: `pydeployer .`

This will run pydeployer from the folder where you are currently in. Pydeployer will automaticly create a user and project file if there is none. 

### Parameters

Parameter     | Description
------------- | -------------
`-v --version`| Check the version of pydeployer
`-r --remove` | Not yet implemented
`-n --renew`  | Renew the contents of the deploy file
