import os
import boto3
import base64

s3_client = boto3.client('s3')


def store_img(data):
    bucket_name = os.environ['BUCKET_NAME']
    s3_key = f'perfil/donatario-{data['nome']}.png'

    try:
        img_data = data['img']

        img_bytes = base64.b64decode(img_data)

        s3_client.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=img_bytes,
            ContentType='image/png')

        print(f'Upload concluido no bucket s3://{bucket_name}/{s3_key}')
    except Exception as e:
        print(f'Erro no upload para a s3: {e}')
        return return_status(500, None)

    return return_status(201, data)


def return_status(status, data):
    return {
        "status": status,
        "data": data
    }


def lambda_handler(event, context):
    return store_img(event)
