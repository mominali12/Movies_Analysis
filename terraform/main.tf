terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}


resource "google_storage_bucket" "imdb_bucket" {
  name          = var.bucket_name
  location      = var.region
  storage_class = var.bucket_storage_class
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 5
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "imdb_dataset" {
  dataset_id = var.dataset_id
  location   = var.region
}