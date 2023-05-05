""" Required modules for WATSON API """
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
                        version='2023-05-03',
                        authenticator=authenticator
)

language_translator.set_service_url(url)

def englishtofrench(englishtext):
    """ Function for english to french translation """
    frenchtranslation = language_translator.translate(
                                text=englishtext,
                                model_id='en-fr'
                                ).get_result()
    return frenchtranslation.get("translations")[0].get("translation")

def frenchtoenglish(frenchtext):
    """ Function for french to english translation """
    englishtranslation = language_translator.translate(
                                text=frenchtext,
                                model_id='fr-en'
                                ).get_result()
    return englishtranslation.get("translations")[0].get("translation")
