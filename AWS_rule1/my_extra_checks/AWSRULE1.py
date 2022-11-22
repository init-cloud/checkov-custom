from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

group_list = list()
groups_list = list()


class AWSRULE1(BaseResourceCheck):
    def __init__(self) -> None:
        name = ""
        id = "CKV_AWS_999"
        supported_resources = ("aws_iam_policy_attachment", "aws_iam_group_policy_attachment")
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'groups' in conf.keys():
            groups = conf['groups'][0]
            groups_list.append(groups)
            for group in groups:
                if group in group_list:
                    return CheckResult.FAILED
            return CheckResult.PASSED
        if 'group' in conf.keys():
            group = conf['group'][0]
            group_list.append(group)
            for groups in groups_list:
                if group in groups:
                    return CheckResult.FAILED
            return CheckResult.PASSED


check = AWSRULE1()
