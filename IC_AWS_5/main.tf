module "IAM" {
  source     = "../Module/IAM"
  user_name  = "cand5"
  group_name = "cand5"
}

resource "aws_iam_policy_attachment" "pass1" {
  name       = "test-policy-attchment"
  policy_arn = module.IAM.iam_policy_cand1_id
  roles = [module.IAM.iam_role_cand1_id]
}
resource "aws_iam_policy_attachment" "pass2" {
  name       = "test-policy-attchment"
  policy_arn = module.IAM.iam_policy_cand1_id
  roles = [module.IAM.iam_role_cand1_id]
}

resource "aws_iam_role_policy_attachment" "fail" {
  policy_arn = module.IAM.iam_policy_cand1_id
  role = module.IAM.iam_role_cand1_id
}

resource "aws_iam_policy_attachment" "fail" {
  name       = "test-policy-attachment"
  policy_arn = module.IAM.iam_policy_cand1_id
  roles = [module.IAM.iam_role_cand1_id]
}