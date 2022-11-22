from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

group_membership_dict = dict()


class AWSRULE6_1(BaseResourceCheck):
    def __init__(self) -> None:
        name = "x"
        id = "CKV_AWS_999"
        supported_resources = ("aws_iam_group_membership",)
        categories = (CheckCategories.KUBERNETES,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'group' in conf.keys() and 'users' in conf.keys():
            group = conf['group'][0]
            users = conf['users'][0]
            if isinstance(group, list):
                group = group[0]
            if isinstance(users, list):
                users = users[0]
            if group in group_membership_dict.keys():
                if users in group_membership_dict[group]:
                    return CheckResult.FAILED
                else:
                    group_membership_dict[group].append(users)
                    return CheckResult.PASSED
            else:
                group_membership_dict[group] = [users]
                return CheckResult.PASSED
        return CheckResult.UNKNOWN


check = AWSRULE6_1()
