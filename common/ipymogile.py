#!/usr/bin/env python
import time
from pymogilefs.client import Client


def catch_error(func):
    def wrap(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as data:
            sdata = '%s' % (data)
            time.sleep(3)
            return func(self, *args, **kwargs)
    return wrap


class mogileclient(object):
    def __init__(self, mogdomain, trackers):
        self.mogdomain = mogdomain
        self.trackers = [trackers]
        if self.mogdomain and self.trackers:
            self.datastore = Client(domain=self.mogdomain, trackers=self.trackers)

    @catch_error
    def upload_file(self, key_id, file):
        self.datastore.store_file(file, key_id)
        # with wf as wft:
        # 	with open(file) as rf:
        # 		wft.write(rf.read())
        return True

    def get_path(self, key_id):
        return self.datastore.get_paths(key_id)

    @catch_error
    def get_data(self,key_id):
        return self.datastore.get_file(key_id)

    @catch_error
    def get_list_keys(self, prefix=None, after=None, limit=None):
        keys = list()
        keys = self.datastore.list_keys(prefix, after, limit)
        return keys

    # @catch_error
    # def keys(self,prefix=None):
    # 	keylst=list()
    # 	keylst=self.datastore.keys(prefix)
    # 	return keylst

    def delete(self, key_id):
        return self.datastore.delete_file(key_id)

    # def copy(self,src,dest):
    #     dat=self.datastore.get_file(src)
    #     if dat:
    #         try:
    #             wf = self.datastore.new_file(dest)
    #             with wf as wft:
    #                 wft.write(dat)
    #         except Exception as data:
    #             return False
    #         return True

#
# def is_same(self,src,dest):
# 	return self.get_data(src)==self.get_data(dest)


if __name__ == "__main__":
    cli = mogileclient('images', '106.13.104.237:7001')
    a=cli.get_path('1.png')
    print(a.data.get('paths'))
    # with open('/home/joe/Desktop/111.jpg', 'rb') as f:
    #     cli.upload_file('54f5gh.jpg', f)


