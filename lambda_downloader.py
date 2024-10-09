import os
import boto3
import base64

s3_client = boto3.client('s3')


def download_img(data):
    bucket_name = os.environ['BUCKET_NAME']
    s3_key = f'perfil/donatario-{data['nome']}.png'

    try:
        s3_object = s3_client.get_object(
            Bucket=bucket_name,
            Key=s3_key)

        image_bytes = s3_object['Body'].read()

        print(f'Download concluido no bucket s3://{bucket_name}/{s3_key}')
    except Exception as e:
        print(f'Erro no download da imagem a s3: {e}')
        return return_status(500, None)

    return image_bytes


def image_to_base64(img):
    return base64.b64encode(img).decode('utf-8')


def return_status(status, data):
    return {
        "status": status,
        "image": data
    }


def lambda_handler(event, context):
    image_b = download_img(event)
    image_64 = image_to_base64(image_b)

    return return_status(200, image_64)
