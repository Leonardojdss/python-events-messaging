from ms_management_client.src.app import register_new_client

fake_event = {
"Records": [
{
    "messageId": "6ab313ff-412c-4acd-86be-8b834166ab71",
    "receiptHandle": "AQEB4IJR81NS96isrghYgAs5auZR6PkuNaxG3obXakcXHOdXgkDMF/dfyboY76uKmZ23ynhSLScgkDM1SEzYudVjMtL4K0BK5UheHJno/678Gh22+WnnDSuqklIckWXdZYRbTAP7+MmLDmSkwBNGkedsxPUO0UxEFoZ0ToE5Lb5CYLEjJCgdqzt+RGOxsqMyjxdDb7COgCIAupdiLr34xsefX/oc7N/lfLiZGM3vYmYsjqqp/7i96cH/C1eQ/AFlZj83FKKnw0nKF3Ifh8OiM/4IqY/tcBR98G2n7shnPqG5wviU+mbWOTiJiwxMMLx4DWIlkkhdk/oHawT531oHjRLSGpBh6a8QMg0iXdWGOWqvPAhAJbqRgBsf5kzpOPA5+1Lq1t08s2AzuA9I0btOyYfMjA==",
    "body": "{\n  \"name_costumer\": \"Leonardo\",\n  \"email\": \"leonardo@example.com\",\n  \"phone\": \"+5511999999999\"\n}",
    "attributes": {
    "ApproximateReceiveCount": "1",
    "SentTimestamp": "1754815469280",
    "SenderId": "AIDAIT2UOQQY3AUEKVGXU",
    "ApproximateFirstReceiveTimestamp": "1754815469289"
    },
    "messageAttributes": {},
    "md5OfBody": "c86aae3d17e2f4f6a52e35c3c5962df2",
    "eventSource": "aws:sqs",
    "eventSourceARN": "arn:aws:sqs:us-east-1:154133135350:NewClientFunctionSQS",
    "awsRegion": "us-east-1"
}
]
}

print(register_new_client(fake_event, None))