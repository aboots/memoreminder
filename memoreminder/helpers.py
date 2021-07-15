import os
from uuid import uuid4

from django.utils.deconstruct import deconstructible


@deconstructible
class OnUploadRename:

    def __init__(self, dir_name):
        self.dir_name = dir_name

    def __call__(self, instance, file_name):
        _, extension = os.path.splitext(file_name)
        return '{}{}{}'.format(self.dir_name, uuid4(), extension)
