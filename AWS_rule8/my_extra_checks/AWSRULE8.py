from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class AWSRULE8(BaseResourceCheck):
    check_resource_duplicated = False

    def __init__(self) -> None:
        name = "x"
        id = "CKV_AWS_999"
        supported_resources = ("aws_ebs_encryption_by_default",)
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'enabled' in conf.keys() and AWSRULE8.check_resource_duplicated is False:
            AWSRULE8.check_resource_duplicated = True
            return CheckResult.PASSED
        else:
            return CheckResult.FAILED


check = AWSRULE8()
