terraform {
  backend "s3" {
    bucket = "github-actions-tf-task-zhyldyz"
    key    = "github-actions/s3-task/terraform.tfstate"
    region = "us-east-1"
  }
}


