import simplejson
import urllib.parse, urllib.request

class Report:
    def retriveReport(md5):
        url = "https://www.virustotal.com/vtapi/v2/file/report"
        parameters = {"resource": md5,
                      "apikey": "880a070ce2c6b798c7bf7d80a485b44762b1c80a559c38a2ea5e19e1dffc7d8g"}
        data = urllib.parse.urlencode(parameters).encode('ascii')
        req = urllib.request.Request(url, data)
        response = urllib.request.urlopen(req)
        json = response.read()
        return json
