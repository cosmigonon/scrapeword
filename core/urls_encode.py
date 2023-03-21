import urllib.parse


def url_parser(translator, tl, sl, text):
     
    services_urls = {
        'Google Translate':
        f'https://translate.google.com/?sl={sl}&tl={tl}&text={text}&op=translate',
        'DeepL Translate':
        f'https://www.deepl.com/es/translator#{sl}/{tl}/{text}',
        'Reverso': 'a',
        'Cambridge Dictionary': 'b'
    }
    
    pass