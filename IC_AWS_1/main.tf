resource "aws_iam_policy_attachment" "pass1_1" {
  name       = "test-policy-attchment"
  policy_arn = module.IAM.iam_policy_cand1_id
  groups     = [module.IAM.iam_group_cand0_id]
}

resource "aws_iam_policy_attachment" "pass1_2" {
  name       = "test-policy-attchment"
  policy_arn = module.IAM.iam_policy_cand2_id
  groups     = [module.IAM.iam_group_cand0_id]
}

resource "aws_iam_group_policy_attachment" "pass2_1" {
  group      = module.IAM.iam_group_cand0_id
  policy_arn = module.IAM.iam_policy_cand1_id
}

resource "aws_iam_group_policy_attachment" "pass2_2" {
  group      = module.IAM.iam_group_cand0_id
  policy_arn = module.IAM.iam_policy_cand2_id
}
resource "aws_iam_policy_attachment" "pass1_1" {
  name       = "test-policy-attchment"
  policy_arn = module.IAM.iam_policy_cand1_id
  groups     = [module.IAM.iam_group_cand0_id]
}

resource "aws_iam_policy_attachment" "pass1_2" {
  name       = "test-policy-attchment"
  policy_arn = module.IAM.iam_policy_cand2_id
  groups     = [module.IAM.iam_group_cand0_id]
}

resource "aws_iam_group_policy_attachment" "pass2_1" {
  group      = module.IAM.iam_group_cand0_id
  policy_arn = module.IAM.iam_policy_cand1_id
}

resource "aws_iam_group_policy_attachment" "pass2_2" {
  group      = module.IAM.iam_group_cand0_id
  policy_arn = module.IAM.iam_policy_cand2_id
}
resource "aws_iam_policy_attachment" "fail" {
  name       = "test-policy-attchment"
  policy_arn = module.IAM.iam_policy_cand2_id
  groups     = [module.IAM.iam_group_cand0_id]
}
resource "aws_iam_group_policy_attachment" "fail" {
  group      = module.IAM.iam_group_cand0_id
  policy_arn = module.IAM.iam_policy_cand1_id
}

