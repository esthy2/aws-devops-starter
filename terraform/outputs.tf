output "instance_public_ip" {
  value = aws_instance.docker_host.public_ip
}

output "instance_public_dns" {
  value = aws_instance.docker_host.public_dns
}

output "ssh_command" {
  value = "ssh -i <your-key.pem> ec2-user@${aws_instance.docker_host.public_ip}"
}

output "app_url" {
  value = "http://${aws_instance.docker_host.public_ip}:5000"
}

output "prometheus_url" {
  value = "http://${aws_instance.docker_host.public_ip}:9090"
}

output "grafana_url" {
  value = "http://${aws_instance.docker_host.public_ip}:3000"
}