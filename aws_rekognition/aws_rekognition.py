import boto3
import json

PHOTO = "/home/rrg11/Desktop/c.jpeg"

rekognition = boto3.client("rekognition")

with open(PHOTO, 'rb') as file:
    response = rekognition.detect_faces(
        Image={
            'Bytes': file.read(),
        },
        Attributes=['ALL']
    )
with open('data.txt', 'w') as outfile:
    json.dump(response, outfile)

person_count = len(response['FaceDetails'])
print('\nThere are {} persons in the image'.format(person_count))

for i, face in enumerate(response['FaceDetails']):
    print('\nPerson: {}'.format(i+1))
    gender = face['Gender']['Value']
    if (gender == 'Male'):
        salute = 'He'
    elif (gender == 'Female'):
        salute = 'She'

    print('The person is {} with confidence {:.2f}%'.format(
        face['Gender']['Value'], face['Gender']['Confidence']))
    print('{} is between {}-{} years old'.format(salute,
        face['AgeRange']['Low'], face['AgeRange']['High']))
    print('{} is {} with confidence {:.2f}%'.format(salute,
        face['Emotions'][0]['Type'], face['Emotions'][0]['Confidence']))
    if (face['Beard']['Value'] == True):
        print('{} has Beard with confidence {:.2f}%'.format(salute, face['Beard']['Confidence']))
    if (face['Mustache']['Value'] == True):
        print('{} has Mustache with confidence {:.2f}%'.format(salute, face['Mustache']['Confidence']))
    if (face['Sunglasses']['Value'] == True):
        print('{} has wore Sunglasses with confidence {:.2f}%'.format(salute, face['Sunglasses']['Confidence']))
