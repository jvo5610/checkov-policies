metadata:
  name: "Check that all resources are tagged with the key - env"
  id: "CKV2_AWS_1"
  category: "GENERAL_SECURITY"
definition:
  cond_type: "attribute"
  resource_types: "all"
  attribute: "tags"
  operator: "exists"