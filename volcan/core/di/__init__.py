import injector
from volcan.domain.upload_image_use_case import UploadImageUseCase
from volcan.core.di.di import ImageModule


class DIContainer:
    _injector = injector.Injector([ImageModule()])

    @classmethod
    def get_upload_use_case(cls):
        return cls._injector.get(UploadImageUseCase)