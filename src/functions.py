

# Inicialización de Tokens

def init_tokens():
    import os
    import tweepy as tw
    from dotenv import load_dotenv

    #Tokens

    load_dotenv()
    Access_Token = os.getenv("TWITTER_TOKEN")
    Access_Secret = os.getenv("TWITTER_SECRET_TOKEN")
    Consumer_Key = os.getenv("TWITTER_API")
    Consumer_secret = os.getenv("TWITTER_SECRET_API")

    #Autenticación de API

    auth = tw.OAuthHandler(Consumer_Key,Consumer_secret)
    auth.set_access_token(Access_Token, Access_Secret)
    api = tw.API(auth)
    
    # public_tweets = api.home_timeline(count=2)
    # for tweet in public_tweets:
    #     print(tweet.text)

    return api



#Traducción de palabras vía online:

def translation_deprecated(word):
    import goslate
    gs = goslate.Goslate()

    return gs.translate(f'{word}', 'es')



#Traducción de palabras vía local:

dict_translations = {"Action":"Accion", "Adventure":"Aventura", "Fighting":"Lucha", "Misc":"Etc", "Platform":"Plataformas", "Puzzle":"Puzzles", "Racing":"Carreras", "Role-Playing":"Rol", "Shooter":"Disparos", "Simulation":"Simulacion", "Sports":"Deportes", "Strategy":"Estrategia"}
def local_translation(word):

    return dict_translations[word]


dict_business = {"X360":"Microsoft","XB":"Microsoft", "XOne":"Microsoft", "3DS":"Nintendo", "DS":"Nintendo", "DC":"Sega", "PC":"Ordenador", "PS2":"Sony", "PS3":"Sony","PS4":"Sony", "PSP":"Sony","PSV":"Sony","Wii":"Nintendo","WiiU":"Nintendo"}
def changeToBusiness(word):

    return dict_business[word]




#Contador de Tweets:

def twitt_counts(nombre):

    # try:

    import time
    import tweepy as tw


    api = init_tokens()


    pages = tw.Cursor(api.search,q=nombre,lang="es",count=100,wait_on_rate_limit=True, wait_on_rate_limit_notify=True).pages()

    count = 0
    for page in pages:
        for tweet in page:
            count +=1
    return count


    # except:

    #     time.sleep(15 * 60)

    #     twitt_counts(nombre)





#Creación de Dataframe con dimensiones adaptadas al uso de API gratuita de Twitter:

Fechas = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]

def estructure_df(df4):

    import pandas as pd

    size = 3

    dfMicrosoft = df4[df4['Empresa']=='Microsoft'].loc[df4['Fecha']==2008].iloc[-size:]

    for element in Fechas:

        dfMicrosoft_builder = df4[df4['Empresa']=='Microsoft'].loc[df4['Fecha']==element].iloc[-size:]

        dfMicrosoft = pd.concat([dfMicrosoft,dfMicrosoft_builder])



    dfSony = df4[df4['Empresa']=='Sony'].loc[df4['Fecha']==2008].iloc[-size:]

    for element in Fechas:

        dfSony_builder = df4[df4['Empresa']=='Sony'].loc[df4['Fecha']==element].iloc[-size:]

        dfSony = pd.concat([dfSony,dfSony_builder])


    dfNintendo = df4[df4['Empresa']=='Nintendo'].loc[df4['Fecha']==2008].iloc[-size:]

    for element in Fechas:

        dfNintendo_builder = df4[df4['Empresa']=='Nintendo'].loc[df4['Fecha']==element].iloc[-size:]

        dfNintendo = pd.concat([dfNintendo,dfNintendo_builder])



    dfOrdenador = df4[df4['Empresa']=='Ordenador'].loc[df4['Fecha']==2008].iloc[-size:]

    for element in Fechas:

        dfOrdenador_builder = df4[df4['Empresa']=='Ordenador'].loc[df4['Fecha']==element].iloc[-size:]

        dfOrdenador = pd.concat([dfOrdenador,dfOrdenador_builder])



    dfSega = df4[df4['Empresa']=='Sega'].loc[df4['Fecha']==2008].iloc[-size:]

    for element in Fechas:

        dfSega_builder = df4[df4['Empresa']=='Sega'].loc[df4['Fecha']==element].iloc[-size:]

        dfSega = pd.concat([dfSega,dfSega_builder])

    
    df5 = pd.concat([dfMicrosoft,dfSony,dfNintendo,dfOrdenador,dfSega])

    return df5


#Selector de apoyo en 'Main.py':


    


    









