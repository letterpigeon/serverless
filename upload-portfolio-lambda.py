import boto3
import StringIO
import zipfile
import mimetypes

#if downloading zip file doesn't work, need to configure server-side encryption version like below
#import botocore.client import config
#s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

def handler(event, context):
    s3 = boto3.resource("s3")
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:ap-southeast-1:089181805188:deployPortfolioTopic')

    try:

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

        topic.publish(Subject="Portfolio Deployed", Message="Portfolio Deployed Successfully.  Triggered by S3")
    except:
        topic.publish(Subject="Portfolio Deploy Failed", Message="Portfolio deployment failed")
        raise
