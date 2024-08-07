from __future__ import print_function
import httplib2
from googleapiclient import discovery
from oauth2client import tools
import argparse
import io
import autharize
from googleapiclient import http
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()

scps = 'https://www.googleapis.com/auth/drive'
csf = 'client_secret.json'
an = 'Drive API Python Quickstart'

ais = autharize.autharize(scps,csf,an)
cd  =ais.get_c()
http = cd.autharize(httplib2.Http())
svc = discovery.build('drive', 'v3', http=http)

def df(fid, filename):
        request = svc.files().get_media(fileId=fid)
        fib = io.BytesIO()
        ml = MediaIoBaseDownload(fib, request)
        flg = False
        while flg is False:
            status, flg = ml.next_chunk()
        with io.open("download/" + filename, 'wb') as f:
            fib.seek(0)
            f.write(fib.read())

def uf(filename):
        fmd = {'name': filename}
        fp = "F/"+filename
        mpd = MediaFileUpload(fp,
                                mimetype="text/plain")
        f = svc.files().create(body=fmd,
                                            media_body=mpd,
                                            fields='id').execute()
        fid = f.get('id')
        print(fid )

def fid1(q):
    res = svc.files().list(
    pageSize=100,fields="nextPageToken, files(id, name)", q="name contains '" + q +"'").execute()
    itm = res.get('files', [])
    if not itm:
        print('nothing')
    else:
        for i in itm:
            return i['id']

def sfl(q):
    res = svc.files().list(
    pageSize=100,fields="nextPageToken, files(id, name)", q="name contains '" + q +"'").execute()
    itm = res.get('files', [])
    if not itm:
        print('nothing')
    else:
        for item in itm:
            print(item['name'])