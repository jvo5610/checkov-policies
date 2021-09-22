from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class variables(BaseResourceCheck):
    def __init__(self):
        name = "Ensure all data stored in the RDS is securely encrypted at rest"
        id = "CKV_AWS_16"
        supported_resources = ['variable']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

def scan_resource_conf(self, conf):
    """
        Looks for encryption configuration at aws_db_instance:
        https://www.terraform.io/docs/providers/aws/d/db_instance.html
    :param conf: aws_db_instance configuration
    :return: <CheckResult>
    """
    if 'type' in conf.keys()
      return CheckResult.PASSED
    return CheckResult.FAILED

check = variables()