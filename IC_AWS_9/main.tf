#fail
resource "aws_iam_user_group_membership" "fail1_1" {
  groups = [aws_iam_group.cand1.id, aws_iam_group.cand2.id]
  user   = aws_iam_user.cand1.id
}
resource "aws_iam_user_group_membership" "fail1_2" {
  groups = [aws_iam_group.cand3.id]
  user   = aws_iam_user.cand1.id
}
#pass
resource "aws_iam_user_group_membership" "pass" {
  groups = [aws_iam_group.cand1.id, aws_iam_group.cand2.id, aws_iam_group.cand3.id]
  user   = aws_iam_user.cand1.id
}
