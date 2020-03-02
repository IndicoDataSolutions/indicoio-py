class IndicoError(Exception):
    pass


class IndicoRequestError(IndicoError):
    def __init__(self, error, code, extras=None):
        super().__init__(f"Status: {code}, Error: {error}\n\tExtras: {extras}")


class IndicoDecodingError(IndicoError):
    def __init__(self, mime, charset, content):
        super().__init__(f"Failed to decode with {mime}:{charset}. Content {content}")


class IndicoInputError(IndicoError):
    def __init__(self, msg):
        super().__init__(msg)

class IndicoInvalidConfigSetting(IndicoError):
    def __init__(self, setting_name,):
        super().__init__(f"{setting_name} is not a valid configuration setting")
