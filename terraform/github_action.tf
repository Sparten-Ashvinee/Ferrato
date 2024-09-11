resource "aws_iam_role" "github_actions_role" {
  name = "github_actions_role"

  assume_role_policy = jsonencode({
    Version = "2022-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = {
          Service = "codebuild.amazonaws.com"
        }
        Action    = "sts:AssumeRole"
      }
    ]
  })
}
