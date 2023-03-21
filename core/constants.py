#Language codes supported by translation services like Google Translate and Deepl.

LANGUAGE_CODES = {
    "bulgarian": "bg",
    "czech": "cs",
    "danish": "da",
    "german": "de",
    "greek": "el",
    "english": "en",
    "spanish": "es",
    "estonian": "et",
    "finnish": "fi",
    "french": "fr",
    "hungarian": "hu",
    "indonesian": "id",
    "italian": "it",
    "japanese": "ja",
    "lithuanian": "lt",
    "latvian": "lv",
    "dutch": "nl",
    "polish": "pl",
    "portuguese": "pt",
    "romanian": "ro",
    "russian": "ru",
    "slovak": "sk",
    "slovenian": "sl",
    "swedish": "sv",
    "turkish": "tr",
    "ukrainian": "uk",
    "chinese": "zh",
}


#Different DOM elements of each web translator and their corresponding selectors.


DEEPL_TARGET_AREA = {
    'selector': '#panelTranslateText > div.lmt__sides_container > div.lmt__sides_wrapper > section.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container > div.lmt__inner_textarea_container > d-textarea > div',
    'XPath': '//*[@id="panelTranslateText"]/div[1]/div[2]/section[2]/div[3]/div[1]/d-textarea/div',
    'jspath': 'document.querySelector("#panelTranslateText > div.lmt__sides_container > div.lmt__sides_wrapper > section.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container > div.lmt__inner_textarea_container > d-textarea > div")'
}

DEEPL_COPY_BUTTON = {
    'selector':'#panelTranslateText > div.lmt__sides_container > div.lmt__sides_wrapper > section.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container > div:nth-child(6) > div > div > div:nth-child(5) > span:nth-child(2) > span > span > button',
    'XPath': '//*[@id="panelTranslateText"]/div[1]/div[2]/section[2]/div[3]/div[6]/div/div/div[2]/span[2]/span/span/button',
    'jspath': 'document.querySelector("#panelTranslateText > div.lmt__sides_container > div.lmt__sides_wrapper > section.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container > div:nth-child(6) > div > div > div:nth-child(5) > span:nth-child(2) > span > span > button")'
}

GOOGLETRANSLATE_TARGET_AREA = {
    'selector': '#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb.EjH7wc > div.AxqVh > div.OPPzxe > c-wiz.sciAJc > div > div.usGWQd > div > div.lRu31',
    'XPath': '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]',
    'jspath': 'document.querySelector("#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb.EjH7wc > div.AxqVh > div.OPPzxe > c-wiz.sciAJc > div > div.usGWQd > div > div.lRu31")'
}

GOOGLETRANSLATE_COPY_BUTTON = {
    'selector': '#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb.EjH7wc > div.AxqVh > div.OPPzxe > c-wiz.sciAJc > div > div.usGWQd > div > div.VO9ucd > div.YJGJsb > span:nth-child(2) > button > div.VfPpkd-Bz112c-RLmnJb',
    'XPath': '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[4]/div[2]/span[2]/button/div[3]',
    'jspath': 'document.querySelector("#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb.EjH7wc > div.AxqVh > div.OPPzxe > c-wiz.sciAJc > div > div.usGWQd > div > div.VO9ucd > div.YJGJsb > span:nth-child(2) > button > div.VfPpkd-Bz112c-RLmnJb")'
} 


