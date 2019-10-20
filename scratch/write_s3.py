import boto3
import pandas as pd
import io
import s3fs

from io import StringIO # python3; python2: BytesIO


def write_df_to_s3(dataFrame, bucketName, full_path):
    csv_buffer = StringIO()

    dataFrame.to_csv(csv_buffer)

    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucketName, full_path).put(Body=csv_buffer.getvalue())

def read_df_from_s3(bucketName, full_path):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucketName, Key=full_path)
    return pd.read_csv(io.BytesIO(obj['Body'].read()))

bucketName="sam-app-data"
key="outputFile.csv"

boto3.setup_default_session(profile_name='personal')
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucketName)
for obj in bucket.objects.filter(Prefix=''):
    print (obj.key)

# Create a sample dataframe
data = [['tom', 10], ['nick', 15], ['juli', 14]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df.head())

write_df_to_s3(df,bucketName,key)

finalDF=read_df_from_s3(bucketName,key)
print('DF after reading back in:')
print(finalDF)
