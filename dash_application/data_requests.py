#%%
from urllib import response
from matplotlib.pyplot import get
import requests
import pandas as pd


def get_kpi1():
    response = requests.get("https://ge4af66d0f4a88a-db26012022.adb.eu-milan-1.oraclecloudapps.com/ords/tip/kpi1/incvol/")
    return response.json()



def get_kpi2():
    response = requests.get("https://g90184408d17efa-db.adb.eu-milan-1.oraclecloudapps.com/ords/tip/kpi2/incsolved/")
    return response.json()


def get_kpi3():
    response = requests.get("https://g90184408d17efa-db.adb.eu-milan-1.oraclecloudapps.com/ords/tip/kpi3/inccrit/")
    return response.json()


def get_kpi4():
    response = requests.get("https://g90184408d17efa-db.adb.eu-milan-1.oraclecloudapps.com/ords/tip/kpi4/inccause/")
    return response.json()


def get_kpi5():
    response = requests.get("https://g90184408d17efa-db.adb.eu-milan-1.oraclecloudapps.com/ords/tip/kpi5/inc-closed/")
    return response.json()

def get_kpi6():
    response = requests.get("https://g90184408d17efa-db.adb.eu-milan-1.oraclecloudapps.com/ords/tip/kpi6/inccause/")
    return response.json()
# %%
