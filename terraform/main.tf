terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "mlops/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "terraform-lock"
    encrypt        = true
  }
}
