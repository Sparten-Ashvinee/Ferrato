Install terraform
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform

terraform --version
terraform init
terraform plan        #show you what changes will be made to your infrastructure without actually applying them
terraform apply       
terraform show        #keeps track of your infrastructure in a state file (terraform.tfstate)
terraform destroy     #tear down the infrastructure
