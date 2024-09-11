resource "aws_lambda_function" "recipe_function" {
  function_name = "RecipeRecommendationFunction"
  s3_bucket     = aws_s3_bucket.mlops_bucket.bucket
  s3_key        = "lambda_function.zip" # Your zipped Lambda code
  handler       = "index.handler"
  runtime       = "python3.8"

  role          = aws_iam_role.lambda_exec.arn
}

resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action    = "sts:AssumeRole"
        Effect    = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
