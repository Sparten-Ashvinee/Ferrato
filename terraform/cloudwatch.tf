resource "aws_cloudwatch_log_group" "recipe_log_group" {
  name              = "/aws/lambda/RecipeRecommendationFunction"
  retention_in_days = 14
}
