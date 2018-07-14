storage "dynamodb" {
  ha_enabled = "true"
  max_parallel = 128
  region = "us-east-1"
  table = "Vault-Production-Backend"
  read_capacity  = 10
  write_capacity = 15
}
listener "tcp" {
 address = "IPADDRESS:8200"
 tls_disable = 1
}
disable_mlock = true
api_addr = "http://IPADDRESS:8200"
