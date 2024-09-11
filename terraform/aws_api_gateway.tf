resource "aws_api_gateway_rest_api" "recipe_api" {
  name        = "RecipeRecommendationAPI"
  description = "API Gateway for the recipe recommendation system"
}

resource "aws_api_gateway_resource" "recipe_resource" {
  rest_api_id = aws_api_gateway_rest_api.recipe_api.id
  parent_id   = aws_api_gateway_rest_api.recipe_api.root_resource_id
  path_part   = "recipes"
}

resource "aws_api_gateway_method" "get_recipes" {
  rest_api_id   = aws_api_gateway_rest_api.recipe_api.id
  resource_id   = aws_api_gateway_resource.recipe_resource.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "lambda" {
  rest_api_id = aws_api_gateway_rest_api.recipe_api.id
  resource_id = aws_api_gateway_resource.recipe_resource.id
  http_method = aws_api_gateway_method.get_recipes.http_method

  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.recipe_function.invoke_arn
}
