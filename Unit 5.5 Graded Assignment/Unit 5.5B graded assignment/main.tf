terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.39"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-central-1"
}

module "s3_module" {
  source      = "./s3_module"
  bucket_name = "huzefa-anver-bucket"
}

output "s3_bucket_id" {
  value = module.s3_module.bucket_id
}
