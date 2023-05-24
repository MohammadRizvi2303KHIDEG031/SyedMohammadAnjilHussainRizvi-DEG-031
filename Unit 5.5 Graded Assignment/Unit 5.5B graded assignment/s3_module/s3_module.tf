resource "aws_s3_bucket" "my_bucket" {
   bucket = var.bucket_name 

}
resource "aws_s3_object" "folder" {
    bucket = "${aws_s3_bucket.my_bucket.id}"
    key    = var.s3_bucket
    source = "/dev/null"
}
