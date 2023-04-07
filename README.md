# Deploy a python application using GIT, Jenkins, Docker, ECR

This project implements a python app and deploy it to using webhook trigger the jenkins pipeline  

## Prerequisite

install jenkins on your EC2 instance
install docker on your EC2 instance

## Setup EKS

This Lab is using Jenkins EC2 instance. Jenkins EC2 instance needs to have following configured:

## Install AWS CLI
- curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" 

- sudo apt install unzip

- sudo unzip awscliv2.zip  

- sudo ./aws/install

- aws --version

## Install eksctl
- curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp 

- sudo mv /tmp/eksctl /usr/local/bin
- eksctl version

## Install kubectl 

- curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
- sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
- chmod +x kubectl
- mkdir -p ~/.local/bin
- mv ./kubectl ~/.local/bin/kubectl
- kubectl version --short --client

- Create IAM Role with Administrator Access policy and assign to your jenkins EC2 instance

## Create EKS cluster
step 1: switch to jenkins user
step 2: create cluster
- eksctl create cluster --name flask-eks --region ap-south-1 --nodegroup-name my-nodes --node-type t3.small --managed --nodes 2

step 3: to see the cluster
- eksctl get cluster --name flask-eks --region ap-south-1

step 4: you can view the kubeconfig file by entering the below command:

- cat  /var/lib/jenkins/.kube/config 

step 5: Copy the content of kubeconfig file and save as a text file

## Deploy the application using webhook trigger
step 1: set credential of github, docker and EKS cluster to jenkins using manage jenkins --> manage credential --> add credentials
step 2: Create Job using pipeline 
step 3: give the path of github, branch name, and jenkinsfile location
step 4: you can take here dev branch first, to deploy application in dev Environment for testing purpose 
