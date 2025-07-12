resource "aws_s3_bucket" "name" {
  bucket = var.bucket_name

  tags = {
    Environment = "Dev"
    Project     = "GitHub Actions Demo"
    Owner       = "Zhyldyz1"
  }
}