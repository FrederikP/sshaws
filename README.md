# sshaws

Simply connect to your 'EC2 Instance Connect'-capable AWS EC2 servers using one command.
If you use 'EC2 Instance Connect' as described [in this article](https://aws.amazon.com/blogs/compute/new-using-amazon-ec2-instance-connect-for-ssh-access-to-your-ec2-instances/) you already noticed that it can become a hassle to connect to instances, especially if you frequently connect to different instances. The `sshaws` command allows takes care of gathering the necessary information, calling ec2-instance-connect (to register your public key) and, finally, ssh to the instance.

With sshaws, in the best case, connecting to your instances will look like this:

TODO GIF

## Requirements

- python3 and pip
- configured aws credentials and rights to connect to the instance
- instance needs to support ec2-instance-connect (AWS AMIs support that + you can install it on your servers)

## Installation

```bash
pip install sshaws
```

You might need to use pip3 if you are not in a virtualenv. You might want to install the package in user space (if you don't have sudo rights). E.g.:

```bash
pip3 install --user sshaws
```

## Usage

```bash
sshaws <instance-id>
```

`<instance-id>` should be replaced by something like: `i-074126021e7b3e7f5`. It can be found in the AWS Console (EC2 view, ECS task description, etc.)

By default it will use the default region, your ssh key at ~/.ssh/id_rsa (private) and ~/.ssh/id_rsa.pub (public) and ec2-user as the username used to connect.
See the help output to see how to change these options:

```bash
sshaws --help
```

## More Examples

To look for the instance in two different regions use:

```bash
sshaws <instance-id> --regions eu-central-1 us-east-1
```
