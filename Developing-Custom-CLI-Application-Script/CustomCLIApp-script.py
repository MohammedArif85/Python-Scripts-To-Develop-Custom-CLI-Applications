import argparse

def deploy(args):
    print(f"Deploying {args.app_name} to {args.environment} environment...")
    # Add your deployment logic here

def rollback(args):
    print(f"Rolling back {args.app_name} in {args.environment} environment...")
    # Add your rollback logic here

def main():
    parser = argparse.ArgumentParser(prog="CustomCLIApp-script.py", description="Custom CLI Application")

    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    deploy_parser = subparsers.add_parser("deploy", help="Deploy an application")
    deploy_parser.add_argument("app_name", nargs="?", help="Name of the application")
    deploy_parser.add_argument("environment", nargs="?", help="Target environment")

    rollback_parser = subparsers.add_parser("rollback", help="Rollback an application deployment")
    rollback_parser.add_argument("app_name", nargs="?", help="Name of the application")
    rollback_parser.add_argument("environment", nargs="?", help="Target environment")

    args = parser.parse_args()

    if not args.subcommand:
        args.subcommand = input("Enter a subcommand (deploy/rollback): ")

    if args.subcommand == "deploy":
        args.app_name = input("Enter the name of the application: ")
        args.environment = input("Enter the target environment: ")
        deploy(args)
    elif args.subcommand == "rollback":
        args.app_name = input("Enter the name of the application: ")
        args.environment = input("Enter the target environment: ")
        rollback(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
