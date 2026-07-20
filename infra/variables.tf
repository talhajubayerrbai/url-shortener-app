variable "project_name" {
  description = "Project name used for resource naming and tagging"
  type        = string
}

variable "ssh_public_key" {
  description = "SSH public key for EC2 key pair"
  type        = string
  sensitive   = true
}

variable "secret_key" {
  description = "Django SECRET_KEY (unused in TF, kept for env parity)"
  type        = string
  sensitive   = true
  default     = ""
}

variable "domain_name" {
  description = "Fully-qualified domain name for the app (e.g. url-shortener-app.udap.dev)"
  type        = string
}
