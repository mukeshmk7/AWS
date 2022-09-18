locals {
    output_folder = "outputs/lambda_app.zip"
}

data "archive_file" "lambda_app" {
  type        = "zip"
  source_file = "lambda_app.py"
  output_path = "${local.output_folder}"
}

resource "aws_lambda_function" "test_lambda" {
  filename      = "${local.output_folder}"
  function_name = "lambda_app"
  role          = "${aws_iam_role.lambda_role.arn}"
  handler       = "lambda_app.lambda_handler"

  source_code_hash = "${filebase64sha256(local.output_folder)}"

  runtime = "python3.7"
}