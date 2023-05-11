import random

from django.shortcuts import render
from django.http import JsonResponse
from .models import Cateory, Content, GetNum
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.utils.six import BytesIO
import json
import time
import os
import psutil
import hashlib
from PIL import Image, ImageDraw
import base64

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

CRYPTO_API = 'aeb442d4-d2fd-4703-82d6-0e13ebae0726'
import redis
import requests
from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError


# Create your views here.

def get_realtime_price(request):
    CRYPTO_API = 'aeb442d4-d2fd-4703-82d6-0e13ebae0726'
    COINS = 'BTC,ETH,BNB,ADA,USDT'
    coin_list = COINS.split(',')
    cmc = CoinMarketCapAPI(CRYPTO_API)
    r = cmc.cryptocurrency_quotes_latest(symbol='BTC,ETH,BNB,ADA,USDT')
    print("rrssss")
    print(r)
    coins_latest_info = {}
    for coin in coin_list:
        coins_latest_info[coin] = r.data[coin]['quote']['USD']['price']

    crypto_price_data = json.dumps(coins_latest_info)
    print("crypto_price_data")
    print(crypto_price_data)
    return JsonResponse({
        # "data": data
        'crypto_price_data': crypto_price_data
    })


def get_history_data(request):
    if request.method == "POST":
        crypto_type = request.GET.get("cryptocurrency")
        # data={"BTC":0.2,"ETH":0.4,"BNB":0.5,"ADA":0.2,"USDT":0.7}

    crypto_type = str(request.body, encoding="utf-8")
    print("crypto_type")
    print(crypto_type)
    # r = redis.StrictRedis(host='localhost', port=6379, db=0)
    today_millis = int(round(time.time() * 1000))
    age_90_millis = today_millis - 90 * 24 * 60 * 60 * 1000
    today_timeStamp = today_millis / 1000
    timeArray = time.localtime(today_timeStamp)
    today_date = time.strftime("%Y-%m-%d", timeArray)
    r_key = crypto_type + str(today_date)
    request_currency = ''
    if crypto_type == 'BTC':
        request_currency = 'BITFINEX:BTCUSD'
    elif crypto_type == 'ETH':
        request_currency = 'bitmex:ETHUSD'
    elif crypto_type == 'BNB':
        request_currency = 'bitfinex:EOSUSD'

    url = 'http://api.bitdataset.com/v1/ohlcv/history/' + request_currency + '?period=d1&start=' + str(
        age_90_millis) + '&limit=99'
    headers = {'apikey': 'a4c7f4f4-6506-451a-b35c-631e7a2949b9'}
    response = requests.get(url, headers=headers)
    # r.set(r_key, response.text)
    hi = json.loads(response.text)

    return JsonResponse({
        # "data": data
        'history_data': hi
    })


def get_sentiment_data(request):
    if request.method == "GET":
        crypto_list = request.GET.get("crypto_list")
    redis_sentiment = redis.StrictRedis(host='localhost', port=6379, db=1)

    btc_score = abs(float(redis_sentiment.get('btc_avg_score')))
    eth_score = abs(float(redis_sentiment.get('eth_avg_score')))
    bnb_score = abs(float(redis_sentiment.get('bnb_avg_score')))
    ada_score = abs(float(redis_sentiment.get('ada_avg_score')))
    usdt_score = abs(float(redis_sentiment.get('usdt_avg_score')))
    btc_score=btc_score+random.random()/60
    usdt_score=usdt_score+random.random()/70

    return JsonResponse({
        # "data": data
        "BTC": btc_score, "ETH": eth_score, "BNB": bnb_score, "ADA": ada_score, "USDT": usdt_score
    })


def get_crypto_list_data(request):
    """
    用于提供数据
    :param request: HttpRequest
    :return: Json
    """
    if request.method == "GET":
        crypto_list = request.GET.get("crypto_list")


# /apis/get_info
def get_info(request):
    """
    用于提供数据
    :param request: HttpRequest
    :return: Json
    """

    if request.method == "GET":
        # 如果是要获取分类列表则加上这个参数  需要提供的内容为: 1ds2ppJu2I9dl1
        cateory_list = request.GET.get("cateory")
        user_list = request.GET.get("users")
        get_access_num = request.GET.get("num")
        get_blog_list = request.GET.get("blog_list")
        get_mp3 = request.GET.get("mp3")
        get_status = request.GET.get("status")

        # 获取分类列表
        if cateory_list is not None and cateory_list == "1ds2ppJu2I9dl1":
            return JsonResponse({
                "status_code": 0,
                "data": [i[0] for i in list(Cateory.objects.values_list("cateory_name"))]
            })

        if user_list is not None and user_list == "2ds2ppJu2I9dl1":
            return JsonResponse({
                "status_code": 0,
                "data": [i[0] for i in list(User.objects.values_list("username"))]
            })

        if get_access_num is not None and get_access_num == "true":
            db = GetNum.objects.get(date=time.strftime("%Y-%m-%d"))
            return JsonResponse({
                "status_code": 0,
                "num": int(db.number)
            })

        if get_blog_list is not None and get_blog_list == "true":
            db = Content.objects.all()
            data = [
                {
                    "title": i.title,
                    "content": i.content,
                    "cateory": i.cateory.cateory_name,
                    "user": i.user.username,
                    "time": i.time
                }
                for i in db]

            return JsonResponse({
                "status_code": 0,
                "data": data
            })
        if get_mp3 is not None:
            data = []
            for i in os.listdir("static/mp3"):
                data.append({"url": f"/apis/static/mp3/{i}",
                             "name": i})

            return JsonResponse({
                "status_code": 0,
                "data": data
            })

        def getMemorystate():
            phymem = psutil.virtual_memory()
            line = "Memory: %5s%% %6s/%s" % (
                phymem.percent,
                str(int(phymem.used / 1024 / 1024)) + "M",
                str(int(phymem.total / 1024 / 1024)) + "M"
            )
            return line

        if get_status is not None:
            data = {}
            data["status_code"] = 0
            # data["cpu_status"] = int(math.fsum(psutil.cpu_percent(interval=1, percpu=True)) // 4)  # 获得cpu当前使用率
            data["cpu_status"] = max(psutil.cpu_percent(interval=1, percpu=True))  # 获得cpu当前使用率
            data["memory_status"] = int(psutil.virtual_memory().percent)  # 获取当前内存使用情况
            data["disk_status"] = int(psutil.disk_usage("/").percent)

            return JsonResponse(data)

        # =====================================================================================
        return JsonResponse({
            "status_code": 1,
            "error": "not data"
        })


# /apis/add
def add_data(request):
    if request.method == "POST":
        add_blog = request.GET.get("add_data")
        add_access = request.GET.get("access")
        # 添加blog
        if add_blog is not None and add_blog == "1bs2ppJu2I9dl1":
            # 将json转换为python dict格式
            data = json.loads(request.body)
            if data.get("title") is not None and data.get("content") is not None and data.get(
                    "cateory") is not None and data.get("author") is not None:

                # try:
                cateory = Cateory.objects.get(cateory_name=data["cateory"])
                user = User.objects.get(username=data["author"])
                db = Content(title=data["title"], content=data["content"], cateory=cateory, user=user)
                db.save()
                # except:
                #     return JsonResponse({
                #         "status_code": 1,
                #         "error": "save define"
                #     })

                return JsonResponse({
                    "status_code": 0,
                    "data": "success"
                })
            else:
                return JsonResponse({
                    "status_code": 1,
                    "error": "data is vaild"
                })
        # 添加访问数
        if add_access is not None and add_access == "add_access":
            try:
                db = GetNum.objects.get(date=time.strftime("%Y-%m-%d"))
                db.number += 1
                db.save()
                return JsonResponse({
                    "status_code": 0,
                    "data": "first user access"
                })
            except:
                db = GetNum()
                db.number = 1
                db.save()
                return JsonResponse({
                    "status_code": 0,
                    "data": "access success!"
                })

        return JsonResponse({
            "status_code": 1,
            "error": "not done"
        })


# /apis/face  0d62f4e0ccdf47c235e34ba512a882c388f667eae540169c7bfd9a415de303494eea5076f90f21cb2ca0299de4cb3bb2
# def checkface(request):
#     try:
#         files = request.FILES.get("file")
#         type_image = files.name.split('.')[-1]
#         filename = "./upload/" + hashlib.sha3_384(files.name.encode()).hexdigest() + f".{type_image}"
#         with open(filename, "ab+") as fp:
#             fp.write(files.read())
#         img = BytesIO()
#         image = face_recognition.load_image_file(filename)
#         locations = face_recognition.face_locations(img=image)
#         result_image = Image.fromarray(image)
#         for pos in locations:
#             d = ImageDraw.Draw(result_image, 'RGBA')
#             d.rectangle((pos[3], pos[0], pos[1], pos[2]))
#         result_image.save(img, 'png')
#
#         return JsonResponse({
#             "status": 0,
#             "filename": files.name,
#             "face_count": len(locations),
#             "resultImg_base": str(base64.b64encode(img.getvalue()).decode())
#         })
#     except:
#         return JsonResponse({
#             "status": 1,
#             "message": "重试一下吧. 你的照片有问题哦."
#         })

class Users:
    @staticmethod
    def get_status(request):
        if request.user.is_authenticated:
            return JsonResponse({
                "status": 0,
                "username": str(request.user),
                "email": str(request.user.email),
            })
        else:
            return JsonResponse({
                "status": 1
            })

    @staticmethod
    def login_user(request):
        if request.method == "POST":
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
            if username is not None and password is not None:
                islogin = authenticate(request, username=username, password=password)
                if islogin:
                    login(request, islogin)
                    return JsonResponse({
                        "status": 0,
                        "message": "Login Success",
                        "username": username
                    })
                else:
                    return JsonResponse({
                        "status": 1,
                        "message": "登录失败, 请检查用户名或者密码是否输入正确."
                    })
            else:
                return JsonResponse({
                    "status": 2,
                    "message": "参数错误"
                })

    @staticmethod
    def logout_user(request):
        logout(request)
        return JsonResponse({
            "status": 0
        })

    @staticmethod
    def register(request):
        if request.method == "POST":
            data = json.loads(request.body)

            if request.GET.get("select") is not None:
                select_username = data.get("select_username")
                print(select_username)
                try:
                    User.objects.get(username=select_username)
                    return JsonResponse({
                        "status": 0,
                        "is_indb": 1
                    })
                except:
                    return JsonResponse({
                        'status': 0,
                        "is_indb": 0
                    })
            username = data.get("username")
            password = data.get("password")
            email = data.get("email")
            if username is not None and password is not None and email is not None:
                try:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    login_user = authenticate(request, username=username, password=password)
                    if login_user:
                        login(request, login_user)
                        return JsonResponse({
                            "status": 0,
                            "message": "Register and Login Success"
                        })

                except:
                    return JsonResponse({
                        "status": 2,
                        "message": "注册失败, 该用户名已经存在."
                    })

        else:
            return JsonResponse({
                "status": 1,
                "message": "error method"
            })
