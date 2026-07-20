output "ec2_public_ip" {
  description = "Public IP address of the EC2 instance (EIP) — used by configure stage for SSH"
  value       = aws_eip.web.public_ip
}

output "ec2_instance_id" {
  description = "EC2 instance ID"
  value       = aws_instance.web.id
}

output "alb_dns_name" {
  description = "ALB DNS name — access the app at http://<alb_dns_name>"
  value       = aws_lb.main.dns_name
}

output "rds_endpoint" {
  description = "RDS PostgreSQL endpoint (host:port) — used by configure stage to build DATABASE_URL"
  value       = aws_db_instance.main.endpoint
}

output "rds_host" {
  description = "RDS hostname only (no port) — for building DATABASE_URL"
  value       = aws_db_instance.main.address
}
