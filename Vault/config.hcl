storage "dynamodb" {
  ha_enabled = "true"
  max_parallel = 128
  region = "us-east-1"
  table = "Vault-Backend"
  read_capacity  = 10
  write_capacity = 15
}
listener "tcp" {
 address     = "127.0.0.1:8200"
 tls_disable = 1
}
disable_mlock = true
