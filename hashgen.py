import sys
import os
import hashlib

class CheckSum:
    def md5Checksum(filePath):
        with open(filePath, 'rb') as fh:
            m = hashlib.md5()
            while True:
                data = fh.read(8192)
                if not data:
                    break
                m.update(data)
            return m.hexdigest()

    def sha256Checksum(filePath):
        with open(filePath, 'rb') as fh:
            m = hashlib.sha256()
            while True:
                data = fh.read(8192)
                if not data:
                    break
                m.update(data)
            return m.hexdigest()

    def sha1Checksum(filePath):
        with open(filePath, 'rb') as fh:
            m = hashlib.sha1()
            while True:
                data = fh.read(8192)
                if not data:
                    break
                m.update(data)
            return m.hexdigest()