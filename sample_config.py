HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ[1713570])
    API_HASH = environ[720a2350815be240fbaf1b6aebbb03bd]
    SUDO_CHAT_ID = int(environ[1797645753])
    OWNER_ID = int(environ[1759059779])
    SESSION_STRING = environ[BQDEP4PVpvrG9fu7MDj4Ht2sGbK62qiLg5QaOfBGdLaSSRA9NDaCRl3NEO1_cpyHyCWubvDBImwZ_lTKBPsUGw62ouy1KPwIt17adHFLAU_5sMT3VtQ9tiFBrLu-g25e-qI2T5_sz2HraeTmBpxx7DyEnV1fuN_sYs1HbB5zD4veoE27osw5I_QJOj0YfIgeV0bTkGZoFe9P37IVTOojlFs_UmFm_zf7wkED_ZtfdeRVIOnp58_oHKOUl3_qyEzrQKY0KrxaQrSoduzUf9tXr9wLDphctFihh6T2uYtmLeODctLxwLf_jEx4QOwG56y0LKrQmSTE6USOhX1hUXg13OMHaNkfQwA]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    SUDO_CHAT_ID = -1001485876964
    OWNER_ID = 1243703097


# don't make changes below this line
ARQ_API = "http://35.240.133.234:8000"
