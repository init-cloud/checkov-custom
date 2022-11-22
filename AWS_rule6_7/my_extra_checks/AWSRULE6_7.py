from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

role_list = list()


class AWSRULE6_6(BaseResourceCheck):
    def __init__(self) -> None:
        name = "x"
        id = "CKV_AWS_999"
        supported_resources = ("aws_iam_role_policy_attachment",)
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'role' in conf.keys() and 'policy_arn' in conf.keys():
            role_name = conf['role'][0]
            policy_arn = conf['policy_arn'][0]
            # if isinstance role_name, list):
            #       role_name = role_name[0]
            # if isinstance(policy_arn, list):
            #     policy_arn = policy_arn[0]
            if role_list is not None:
                for role in role_list:
                    if role_name in role['role_name'] and policy_arn in role['policy_arn']:
                        return CheckResult.FAILED
            role_dict = {'role_name': role_name, 'policy_arn': policy_arn}
            role_list.append(role_dict)
            return CheckResult.PASSED


check = AWSRULE6_6()
