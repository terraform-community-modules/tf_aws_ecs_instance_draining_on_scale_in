variable "autoscaling_group_name" {}

variable "lambda_enabled" {
  default = true
}

variable "hook_heartbeat_timeout" {
  default = 900
}

variable "hook_default_result" {
  default = "ABANDON"
}
