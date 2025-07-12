terraform {
  backend "s3" {
    bucket = "github-actions-tf-task-zhyldyz"
    key    = "github-actions/infra/terraform.tfstate"
    region = "us-east-1"
  }
}


