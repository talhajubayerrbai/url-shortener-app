output "ec2_public_ip" {
  description = "Public IP address of the EC2 instance (EIP)"
  value       = aws_eip.web.public_ip
}

output "ec2_instance_id" {
  description = "EC2 instance ID"
  value       = aws_instance.web.id
}
