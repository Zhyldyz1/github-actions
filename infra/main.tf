provider "aws" {
  region = "us-east-1"
}
resource "aws_s3_bucket" "task_bucket" {
  bucket = var.bucket_name
  force_destroy = true
}
