from .appversion import AppVersionConfig


class UserAgentConfig(object):
    def __init__(self,
                 platform,
                 app_version,
                 mcc, mnc,
                 os_version, manufacturer, device, os_build_number,
                 phone_id,
                 locale_lang,
                 locale_country
                 ):
        """
        :param platform:
        :type platform: int
        :param app_version:
        :type app_version: AppVersionConfig
        :param mcc:
        :type mcc: str
        :param mnc:
        :type mnc: str
        :param os_version:
        :type os_version: str
        :param manufacturer:
        :type manufacturer: str
        :param device:
        :type device: str
        :param os_build_number:
        :type os_build_number:
        :param phone_id:
        :type phone_id:
        :param locale_lang:
        :type locale_lang: str
        :param locale_country:
        :type locale_country: str
        """
        self._platform = platform
        self._app_version = app_version
        self._mcc = mcc
        self._mnc = mnc
        self._os_version = os_version
        self._manufacturer = manufacturer
        self._device = device
        self._os_build_number = os_build_number
        self._phone_id = phone_id
        self._locale_lang = locale_lang
        self._locale_country = locale_country

    @property
    def platform(self):
        return self._platform

    @property
    def app_version(self):
        return self._app_version
    @property
    def mcc(self):
        return self._mcc

    @property
    def mnc(self):
        return self._mnc

    @property
    def os_version(self):
        return self._os_version

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def device(self):
        return self._device

    @property
    def os_build_number(self):
        return self._os_build_number

    @property
    def phone_id(self):
        return self._phone_id

    @property
    def locale_lang(self):
        return self._locale_lang

    @property
    def locale_country(self):
        return self._locale_country
