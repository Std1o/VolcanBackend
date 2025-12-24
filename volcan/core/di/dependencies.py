from volcan.core.di import DIContainer


def inject_upload_use_case():
    return DIContainer.get_upload_use_case()