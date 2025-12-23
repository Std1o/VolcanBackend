import injector
from volcan.data.image_repository_impl import ImageRepositoryImpl
from volcan.domain.image_repository import ImageRepository


class ImageModule(injector.Module):

    def configure(self, binder):
        binder.bind(ImageRepository, to=ImageRepositoryImpl)

        @injector.provider
        def provide_image_repository() -> ImageRepository:
            return ImageRepositoryImpl()