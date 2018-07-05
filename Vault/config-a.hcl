storage "dynamodb" {
  ha_enabled = "true"
  max_parallel = 128
  region = "us-east-1"
  table = "Vault-Backend"
  read_capacity  = 10
  write_capacity = 15
  recovery_mode=1
}
listener "tcp" {
 address = "10.0.11.94:8200"
 tls_disable = 1
}
disable_mlock = true
api_addr = "http://10.0.11.94:8200"
