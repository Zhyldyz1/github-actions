terraform {
  backend "s3" {
    bucket = "your-terraform-backend-bucket"
    key    = "github-actions/s3-task/terraform.tfstate"
    region = "us-east-1"
  }
}


