import json

def execute(event, context):
    print("===== execute ====")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda2!!!')
    }
