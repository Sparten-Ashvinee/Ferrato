output "api_url" {
  value = "${aws_api_gateway_rest_api.recipe_api.execution_arn}/recipes"
}

output "s3_bucket_name" {
  value = aws_s3_bucket.mlops_bucket.bucket
}
