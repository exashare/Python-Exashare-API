import json
from urllib.request import urlopen

class ExashareAPI:
    def __init__(self):
        self.result = False;

    def AccountInfo(self, **kwargs):
        values = {}
        values['op'] = 'account_info'
        values['key'] = kwargs.pop('key')
        self.Request(**values)
        return self.result
    
    def UploadURL(self, **kwargs):
        values = {}
        values['op'] = 'upload_url'
        values['key'] = kwargs.pop('key')
        values['url'] = kwargs.pop('url')
        folder = kwargs.pop('folder', None)
        if folder:
            values['folder'] = folder
        self.Request(**values)
        return self.result
    
    def CheckUploadURL(self, **kwargs):
        values = {}
        values['op'] = 'check_upload_url'
        values['key'] = kwargs.pop('key')
        values['id'] = kwargs.pop('id')
        self.Request(**values)
        return self.result
    
    def GetUploadServer(self, **kwargs):
        values = {}
        values['op'] = 'get_upload_server'
        values['key'] = kwargs.pop('key')
        self.Request(**values)
        return self.result
    
    def CheckFiles(self, **kwargs):
        values = {}
        values['op'] = 'check_files'
        values['key'] = kwargs.pop('key')
        files = kwargs.pop('files')
        if type(files) is list:
            files = ','.join(files)
        values['list'] = files
        self.Request(**values)
        return self.result
    
    def RenewFile(self, **kwargs):
        values = {}
        values['op'] = 'file_renew'
        values['key'] = kwargs.pop('key')
        values['file_code'] = kwargs.pop('file_code');
        self.Request(**values)
        return self.result
    
    def CloneFile(self, **kwargs):
        values = {}
        values['op'] = 'file_clone'
        values['key'] = kwargs.pop('key')
        values['file_code'] = kwargs.pop('file_code')
        folder = kwargs.pop('folder', None)
        if folder:
            values['folder'] = folder
        new_title = kwargs.pop('new_title', None)
        if new_title:
            values['new_title'] = new_title
        self.Request(**values)
        return self.result
    
    def CheckFilesDMCA(self, **kwargs):
        values = {}
        values['op'] = 'files_dmca'
        values['key'] = kwargs.pop('key')
        date = kwargs.pop('date', None)
        if date:
            values['date'] = date
        order = kwargs.pop('order', None)
        if order:
            values['order'] = order
        self.Request(**values)
        return self.result
    
    def Request(self, **kwargs):
        param = '?version=0.02'
        for key, value in kwargs.items():
            if param:
                param += '&' + key + '=' + value
            else:
                param += '?' + key + '=' + value
        url = 'http://exashare.com/api'
        url += param if param else ''
        response = urlopen(url)
        self.result = json.loads(response.read().decode('utf8'))
