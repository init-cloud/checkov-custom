from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

user_list = list()
users_list = list()


class AWSRULE4(BaseResourceCheck):
    def __init__(self) -> None:
        name = ""
        id = "CKV_AWS_999"
        supported_resources = ("aws_iam_policy_attachment", "aws_iam_user_policy_attachment")
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'users' in conf.keys():
            users = conf['users'][0]
            users_list.append(users)
            for user in users:
                if user in user_list:
                    return CheckResult.FAILED
            return CheckResult.PASSED
        if 'user' in conf.keys():
            user = conf['user'][0]
            user_list.append(user)
            for users in users_list:
                if user in users:
                    return CheckResult.FAILED
            return CheckResult.PASSED


check = AWSRULE4()
