import boto3
import StringIO
import zipfile
import mimetypes
#if downloading zip file doesn't work, need to configure server-side encryption version like below
#import botocore.client import config
#s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

s3 = boto3.resource("s3")

portfolio_bucket = s3.Bucket("portfolio.culnab.com")
build_bucket = s3.Bucket('portfoliobuild.culnab.com')

serverless_zip = StringIO.StringIO()
build_bucket.download_fileobj('serverlessbuild.zip', serverless_zip)

with zipfile.ZipFile(serverless_zip) as myzip:
    for name in myzip.namelist():
        obj = myzip.open(name)
        portfolio_bucket.upload_fileobj(obj, name,
            ExtraArgs={'ContentType': mimetypes.guess_type(name)[0]})
        portfolio_bucket.Object(name).Acl().put(ACL='public-read')
