import pyrebase
from django.core.files.storage import Storage
from django.conf import settings
from django.core.files.base import ContentFile
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import pathlib
from os import path
from django.core.files.uploadedfile import InMemoryUploadedFile
import uuid


class FirebaseStorage(Storage):
    def __init__(self):

        self.cred = credentials.Certificate(
            path.join(
                pathlib.Path().resolve(),
                "store_app",
                "config",
                "serviceAccountKey.json",
            )
        )
        # # Initialize the app with a service account, granting admin privileges
        self.app = firebase_admin.initialize_app(
            self.cred, {"storageBucket": "thread-butterfly.appspot.com"}
        )
        self.bucket = storage.bucket(name="thread-butterfly")
        self.storage = storage

    def _open(self, name, mode="rb"):
        url = self.url(name)
        print("----- name", name)
        return ContentFile(self.storage.child(name).get().content, name=name)

    def _save(self, name, content:InMemoryUploadedFile):
        file_blob = self.bucket.blob(f'{uuid.uuid4()}_{content.name}')
        # bb=self.bucket.list_blobs()
        # for b in bb:
        #     print(b.name)
        
        print("Saving in Firebase...")
        file_blob.upload_from_file(content, content_type=content.content_type)
        file_blob.make_public()
        file_url=file_blob.public_url

        return file_blob.public_url
        

    def delete(self, name):
        self.storage.child(name).delete()

    def exists(self, name):
        try:
            self.storage.child(name).get()
            return True
        except:
            return False

    def url(self, name):
        # print("here", name)
        return name

    def size(self, name):
        return self.storage.child(name).get().info().size

    def get_available_name(self, name, max_length=None):
        print("available name")
        return name
