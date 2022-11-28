resource "aws_iam_user" "cand1" {
  name = "cand1"
}


#fail
resource "aws_iam_user_policy" "fail1_1" {
  name = "cand1"
  user = "${aws_iam_user.cand1.id}"

  policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [
      {
        Action = [
          "ec2:*",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}


resource "aws_iam_user_policy" "fail1_2" {
  name = "cand1"
  user = "${aws_iam_user.cand1.id}"

  policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [
      {
        Action = [
          "*",
        ]
        Effect   = "Deny"
        Resource = "*"
      },
    ]
  })
}


#pass
resource "aws_iam_user_policy" "pass" {
  name = "cand1"
  user = aws_iam_user.cand1.id

  policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [
      {
        Action = [
          "ec2:*",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
      {
        Action = [
          "*",
        ]
        Effect   = "Deny"
        Resource = "*"
      }
    ]
  })
}