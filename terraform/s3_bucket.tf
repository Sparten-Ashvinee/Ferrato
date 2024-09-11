resource "aws_s3_bucket" "mlops_bucket" {
  bucket = "mlops-recipe-dataset"
  acl    = "private"
}

resource "aws_s3_bucket" "dvc_bucket" {
  bucket = "mlops-recipe-dvc-storage"
  acl    = "private"
}
