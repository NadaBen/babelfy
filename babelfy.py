import urllib
import json
import gzip

from io import BytesIO

service_url = 'https://babelfy.io/v1/disambiguate'

text = 'BabelNet is both a multilingual encyclopedic dictionary and a semantic network'
lang = 'EN'
key  = 'your key'

params = {
    'text' : text,
    'lang' : lang,
    'key'  : key
}

url = service_url + '?' + urllib.parse.urlencode(params)
request = urllib.request.Request(url)
request.add_header('Accept-encoding', 'gzip')
response = urllib.request.urlopen(request)

if response.info().get('Content-Encoding') == 'gzip':
    buf = BytesIO(response.read())
    f = gzip.GzipFile(fileobj=buf)
    data = json.loads(f.read().decode('utf-8'))

    # retrieving data
    for result in data:
                # retrieving token fragment
                tokenFragment = result.get('tokenFragment')
                tfStart = tokenFragment.get('start')
                tfEnd = tokenFragment.get('end')
                #print (str(tfStart) + "\t" + str(tfEnd))

        # retrieving char fragment
                charFragment = result.get('charFragment')
                cfStart = charFragment.get('start')
                cfEnd = charFragment.get('end')
                #print (str(cfStart) + "\t" + str(cfEnd))

                # retrieving BabelSynset ID
                synsetId = result.get('babelSynsetID')
                print ('source'+ "\t" +result.get('source'))
                print('DBpediaURL'+ "\t" +result.get('DBpediaURL'))
                print('BabelNetURL'+ "\t" +result.get('BabelNetURL'))
                print('globalScore'+ "\t" +str(result.get('globalScore')))
                print('coherenceScore'+ "\t" +str(result.get('coherenceScore')))
