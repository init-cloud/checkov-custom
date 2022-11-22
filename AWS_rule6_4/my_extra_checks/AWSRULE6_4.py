from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

group_membership_dict = dict()


class AWSRULE6_1(BaseResourceCheck):
    def __init__(self) -> None:
        name = "x"
        id = "CKV_AWS_999"
        supported_resources = ("aws_iam_user_group_membership",)
        categories = (CheckCategories.KUBERNETES,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'groups' in conf.keys() and 'user' in conf.keys():
            groups = conf['groups'][0]
            user = conf['user'][0]
            if isinstance(groups, list):
                groups = groups[0]
            if isinstance(user, list):
                user = user[0]
            if user in group_membership_dict.keys():
                if groups in group_membership_dict[user]:
                    return CheckResult.FAILED
                else:
                    group_membership_dict[user].append(groups)
                    return CheckResult.PASSED
            else:
                group_membership_dict[user] = [groups]
                return CheckResult.PASSED
        return CheckResult.UNKNOWN


check = AWSRULE6_1()
