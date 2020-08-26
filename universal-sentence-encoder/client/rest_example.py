import json
import requests
import pprint

SERVER_URL = 'http://localhost:8501/v1/models/universal-sentence-encoder:predict'

pp = pprint.PrettyPrinter(indent=1)
def main():
    test_string = 'You must understand the whole of life, not just one little part of it. That is why you must read, that is why you must look at the skies, that is why you must sing, and dance, and write poems, and suffer, and understand, for all that is life.'
    req = { 'inputs': [test_string], 'signature_name': 'serving_default'}
    res = requests.post(SERVER_URL, data=json.dumps(req))
    res.raise_for_status()
    pp.pprint(res.json())

if __name__ == '__main__':
    main()