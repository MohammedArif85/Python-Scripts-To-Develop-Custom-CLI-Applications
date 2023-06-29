# Custom CLI Application
This repository contains a Python script for a custom CLI (Command-Line Interface) application designed for DevOps use cases. The script allows you to deploy and rollback application deployments in different environments.

## Prerequisites
- Python 3.x

## Usage

### Deploying an Application
To deploy an application, use the following command:
```
python CustomCLIApp-script.py deploy [app_name] [environment]
```
- Replace `[app_name]` with the name of the application you want to deploy.
- Replace `[environment]` with the target environment where you want to deploy the application.

### Rolling Back an Application Deployment
To rollback an application deployment, use the following command:
```
python CustomCLIApp-script.py rollback [app_name] [environment]
```
- Replace `[app_name]` with the name of the application you want to rollback.
- Replace `[environment]` with the target environment where the application is deployed.

**Note:** If you don't provide the `[app_name]` and `[environment]` arguments in the command, the script will prompt you to enter them manually.

## Examples
### Deploying an Application Example
```
python CustomCLIApp-script.py deploy MyApp Production
```
This command deploys the application named "MyApp" to the "Production" environment.

### Rolling Back an Application Deployment Example
```
python CustomCLIApp-script.py rollback MyApp Staging
```
This command rolls back the deployment of the application named "MyApp" in the "Staging" environment.
