import requests

import urllib2

import urllib

import hashlib

import hmac

import base64

 

request={}

 

url = 'https://api.ucloudbiz.olleh.com/watch/v1/client/api?'

apikey = '6vfdMtfS6ZXmi4VyCxcBDcNM27jeHUMDDBTZQju81Z2a9FNC_tpzO2c5WQLWO7ypq8VFtPyn-gmjl5wPQK8XHg'

secretkey = 'JCfSPy0d7JwttWGevNeNji1Ktr_trXZ2caJHLTGf_obvjPtsBmYZr5-_u010JWUVBokls98tTMZeT8NiiUSPaQ'

 

 

request['command']='listMetrics'

#request['signature']=secretkey

request['response']='xml'

request['apiKey']=apikey

 

request_str='&'.join(['='.join([k,urllib.quote_plus(request[k])]) for k in request.keys()])

sig_str='&'.join(['='.join([k,urllib.quote_plus(request[k]).replace('+','%20').lower()]) for k in sorted(request.iterkeys())])

sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())

 

req = url+request_str+'&signature='+sig

requests.get(req)

