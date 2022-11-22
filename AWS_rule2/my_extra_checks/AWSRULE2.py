from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

group_list = list()


class AWSRULE2(BaseResourceCheck):
    def __init__(self) -> None:
        name = ""
        id = "CKV_AWS_999"
        supported_resources = ("aws_iam_group_policy_attachment",)
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'group' in conf.keys() and 'policy_arn' in conf.keys():
            group_name = conf['group'][0]
            policy_arn = conf['policy_arn'][0]
            # if isinstance(group_name, list):
            #     group_name = group_name[0]
            # if isinstance(policy_arn, list):
            #     policy_arn = policy_arn[0]
            if group_list is not None:
                for group in group_list:
                    if group_name in group['group_name'] and policy_arn in group['policy_arn']:
                        return CheckResult.FAILED
            group_dict = {'group_name': group_name, 'policy_arn': policy_arn}
            group_list.append(group_dict)
            return CheckResult.PASSED


check = AWSRULE2()
