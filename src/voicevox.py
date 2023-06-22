import json
from os import getenv
from pathlib import Path
from threading import Thread
from urllib.parse import urlencode

import requests
from MoeGoe.Main import speech_text
# discord bot feature
from discordbot import ExcuteDiscordWebhook
from dotenv import load_dotenv
# romaji to japanese
from modules.convert_roma_ja import english_to_katakana

from modules.audio_to_device import play_voice
from modules.translator import DoTranslate

load_dotenv()

# Audio devices
SPEAKERS_INPUT_ID = int(getenv('VOICEMEETER_INPUT_ID'))
APP_INPUT_ID = int(getenv('CABLE_INPUT_ID'))

audio_volume = 1

# Voicevox settings
BASE_URL = getenv('VOICEVOX_BASE_URL')
# BASE_URL = 'http://127.0.0.1:50021'
VOICE_ID = int(getenv('VOICE_ID'))
SPEED_SCALE = float(getenv('SPEED_SCALE'))
VOLUME_SCALE = float(getenv('VOLUME_SCALE'))
INTONATION_SCALE = float(getenv('INTONATION_SCALE'))
PRE_PHONEME_LENGTH = float(getenv('PRE_PHONEME_LENGTH'))
POST_PHONEME_LENGTH = float(getenv('POST_PHONEME_LENGTH'))

TTS_WAV_PATH = Path(__file__).resolve().parent.parent / r'audio\tts.wav'


def speak(sentence, tts_settings, other_settings):
    # print("번역전 텍스트: ", sentence)
    language_code = tts_settings["tts_language"]
    voice_volume = tts_settings["voice_volume"]
    discord_print_language = other_settings["discord_print_language"]
    ai_model_language = other_settings["ai_model_language"]     # language that AI Model using ("pygmalion should communicate with  english")

    bot_trans_speech = DoTranslate(sentence, ai_model_language, language_code)  # Translate reply
    if language_code == 'ja':
        bot_trans_speech = english_to_katakana(bot_trans_speech)  # romaji to japanese
    elif language_code == 'ko':
        bot_trans_speech = bot_trans_speech  # TODO: eng to korean
        voice_volume = voice_volume * 0.3

    # synthesize voice as wav file
    speech_text(tts_settings["tts_character_name"], bot_trans_speech, language_code, tts_settings["voice_id"], voice_volume)

    # play voice to app mic input and speakers/headphones
    threads = [Thread(target=play_voice, args=[APP_INPUT_ID]), Thread(target=play_voice, args=[SPEAKERS_INPUT_ID])]

    if other_settings["discord_bot"]:
        # Do translate to discord_print_langage, if it's not same as language_code
        if language_code != discord_print_language:
            discord_sentence = DoTranslate(sentence, ai_model_language, discord_print_language)
        else:
            discord_sentence = bot_trans_speech

        # SendDiscordMessage(discord_sentence)
        ExcuteDiscordWebhook(discord_sentence)

    [t.start() for t in threads]
    [t.join() for t in threads]


def read_text_file(filename):
    # 텍스트 파일 읽기
    with open(filename, 'r') as file:
        data = file.read()

    data = data.strip()

    # JSON 변환
    try:
        json_data = json.loads(data)
    except json.JSONDecodeError:
        print("Invalid JSON format in the text file.")
        return None

    return json_data


if __name__ == '__main__':
    # test if voicevox is up and running

    # print(load_tts_setting())
    print('Voicevox attempting to speak now...')
    # speak('むかしあるところに、ジャックという男の子がいました。ジャックはお母さんと一緒に住んでいました。','ja')
