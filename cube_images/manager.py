from django.core.files.storage import default_storage as django_default_storage
from django.db.models.fields.files import ImageFieldFile
from pathlib import Path


def get_upload_path_cube(base, filename):
    '''Builds the path of a cube image given the original filename and the final part.'''
    base = Path(base)
    components = list(base.parts)
    components[-1] = '%s_%s' % (base.stem, filename)

    return str(Path(*components))


class CubeImagesManager(object):
    '''Attach a field to the model that has the 6 faces of the cube.'''

    def __init__(self, field_name, files_extension='jpeg'):  # maybe ext in a settings
        self.field_name = field_name
        self.files_extension = files_extension

    def contribute_to_class(self, model, name):
        setattr(model, name, CubeImagesDescriptor(self.field_name, self.files_extension))


class CubeImagesDescriptor(object):

    def __init__(self, field_name, files_extension):
        self.files_extension = files_extension
        self.field_name = field_name

    def __get__(self, instance, value):
        field = getattr(instance, self.field_name)
        return CubeImages(
            instance,
            field,
            self.files_extension
        )


class CubeImages(object):

    def __init__(self, instance, field_image_instance, files_extension):
        self.instance = instance
        self.field_image_instance = field_image_instance
        self.files_extension = files_extension
        self.format = 'tile_%s'

        self.allowed_attributes = [
            self.format % _ for _ in ('f', 'b', 'l', 'r', 'u', 'd')
        ]

    def __getattr__(self, item):
        if item in self.allowed_attributes:
            complete_filename = "%s.%s" % (item, self.files_extension)  # THE EXTENSION IS FIXED?
            return ImageFieldFile(self.instance, self.field_image_instance, get_upload_path_cube(self.field_image_instance.name, complete_filename))

        raise AttributeError('You call this object with wrong attribute name \'%s\', allowed %s' %
                             (item, self.allowed_attributes))


class CubeImage(object):

    def __init__(self, path):
        self.path = path
        self.storage = django_default_storage

    def _storage_attr(self, attr, *args, **kwargs):
        fn = getattr(self.storage, attr)
        return fn(self.path, *args, **kwargs)

    def save(self, content, **kwargs):
        return self._storage_attr('save', content, **kwargs)

    @property
    def url(self):
        return self._storage_attr('url')
