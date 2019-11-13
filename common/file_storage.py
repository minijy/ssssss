#!/usr/bin/env python
from common.ipymogile import mogileclient
from common import osfunc
import os
from conf import confg


class MogileFileSys:
    def __init__(self, domain, tracker):
        self.domain = domain
        self.client = mogileclient(domain, tracker)

    def _uploadFile(self, key,  file_handle):
        res = self.client.upload_file(key, file_handle)
        if res:
            return confg.file_http_path%(self.domain, key)
        return False

    def upload_file(self, key, src):
        if hasattr(src, 'str'):
            with open(src, 'rb') as fr:
                return self._uploadFile(key, fr)
        else:
            return self._uploadFile(key, src)

