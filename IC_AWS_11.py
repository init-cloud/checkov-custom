from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class IC_AWS_11(BaseResourceCheck):
    user_list = list()

    def __init__(self) -> None:
        name = "Do not declare the same user and policy repeatedly"
        id = "IC_AWS_11"
        supported_resources = ("aws_iam_user_policy_attachment",)
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'user' in conf.keys() and 'policy_arn' in conf.keys():
            user_name = conf['user'][0]
            policy_arn = conf['policy_arn'][0]
            if IC_AWS_11.user_list is not None:
                for user in IC_AWS_11.user_list:
                    if user_name in user['user_name'] and policy_arn in user['policy_arn']:
                        return CheckResult.FAILED
            user_dict = {'user_name': user_name, 'policy_arn': policy_arn}
            IC_AWS_11.user_list.append(user_dict)
            return CheckResult.PASSED


check = IC_AWS_11()
