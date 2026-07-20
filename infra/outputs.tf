output "ec2_public_ip" {
  description = "Public IP address of the EC2 instance (EIP) — used by configure stage for SSH"
  value       = aws_eip.web.public_ip
}

output "ec2_instance_id" {
  description = "EC2 instance ID"
  value       = aws_instance.web.id
}

output "alb_dns_name" {
  description = "ALB DNS name (internal AWS hostname)"
  value       = aws_lb.main.dns_name
}

output "app_url" {
  description = "Public HTTPS URL of the application"
  value       = "https://${var.domain_name}"
}
