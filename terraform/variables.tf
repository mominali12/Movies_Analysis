variable "credentials" {
  description = "My Credentials"
  default     = "../secrets/dtc-de-410416-22f86805c390.json"
}


variable "project" {
  description = "Google Cloud Project ID"
  default     = "dtc-de-410416"
}

variable "region" {
  description = "Google Cloud Region"
  default     = "europe-north1"
}

variable "location" {
  description = "Google Cloud Project Location"
  default     = "EU"
}

variable "dataset_id" {
  description = "BigQuery Dataset ID"
  default     = "imdb_dataset"
}

variable "table_id" {
  description = "BigQuery Table ID"
  default     = "imdb_tbl"
}

variable "bucket_name" {
  description = "Google Cloud Bucket Name"
  default     = "dtc-de-410416-imdb_bucket"
}

variable "bucket_storage_class" {
  description = "Google Cloud Bucket Storage Class"
  default     = "STANDARD"
}