import asyncio
import random
import openpyxl
import youtube_dl
import urllib
import urllib.request
import bs4
import sys
import json
import selenium
import time
import datetime
import re
import aiohttp
import discord
import os
from discord.ext import commands
from discord.utils import get
import html
import openpyxl
from discord import Member
from discord.ext import commands
from urllib.request import urlopen, Request
from selenium import webdriver
import nekos

client = discord.Client()
pre='.'

# 생성된 토큰을 입력해준다.
token = ""

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("================")
    game = discord.Game('히유야 설명')
    await client.change_presence(status=discord.Status.online, activity=game)

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == '!hello':
        await message.channel.send('Hello {0.author.mention}'.format(message))

    if message.content == "히유야 설명":
        embed = discord.Embed(title="히유봇 설명", description="히유봇의 명령어입니다.", color=0x00ff56)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/726479512803606611/774216089584009266/1656af8704103ed8.png")
        embed.add_field(name="히유야 명령어", value="명령어 목록을 출력합니다.", inline=False)
        embed.add_field(name="히유야 네코", value="랜덤으로 네코 사진을 출력합니다. (수위는 책임 못져요 ㅎ)", inline=False)
        embed.add_field(name="히유야 강아지", value="랜덤으로 강아지 사진을 출력합니다.", inline=False)
        embed.add_field(name="히유야 고양이", value="랜덤으로 고양이 사진을 출력합니다.", inline=False)
        embed.add_field(name="히유야 랜덤사진", value="랜덤으로 사진을 출력합니다.", inline=False)
        embed.add_field(name="히유야 오늘날짜", value="오늘 날짜를 알려줍니다.", inline=False)
        embed.add_field(name="히유야 정보", value="명령어를 입력한 사람의 정보를 출력합니다.", inline=False)
        embed.add_field(name="히유야 지금시간", value="현재시간을 출력합니다.", inline=False)
        embed.add_field(name="히유야 날씨", value="오늘의 날씨를 알려줍니다.", inline=False)
        embed.add_field(name="/청소 [지울 메시지의 수]", value="메시지를 지정한 개수만큼 삭제해줍니다.", inline=False)
        embed.add_field(name="히유야 초대코드", value="히유봇 초대코드.", inline=False)
        embed.set_footer(text="제작: 히유#7112")
        await message.channel.send(embed=embed)

    if message.content == '히유야 지금시간': #수정완료
        time = datetime.datetime.today()
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name='지금시간이에요', value=str(time.hour) + '시' + str(time.minute) + '분' + str(time.second) + '초', inline=True)
        await message.channel.send(embed=embed)

    if message.content == '히유야 안녕':
        channel = message.channel
        await channel.send('반가워요')

    if message.content == '히유야 네코':
        channel = message.channel
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed2 = discord.Embed(
            colour=discord.Colour.green()
        )
        embed3 = discord.Embed(
            colour=discord.Colour.green()
        )
        randomnumber = random.randrange(100, 407)
        randomgiho = random.randrange(1,3)
        print('?번째사진 : '+str(randomnumber))
        print('기호 : '+str(randomgiho))
        strandomnumber = str(randomnumber)
        file1 = '.png'
        file2 = '.jpg'
        file3 = '.jpeg'
        giho = '_'
        if randomgiho==1:
            urlbase1 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file1
            urlbase2 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file2
            urlbase3 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file3
            embed.set_image(url=urlbase1)
            embed2.set_image(url=urlbase2)
            embed3.set_image(url=urlbase3)
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await channel.send(embed=embed3)
        else:
            urlbase_1 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file1
            urlbase_2 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file2
            urlbase_3 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file3
            embed.set_image(url=urlbase_1)
            embed2.set_image(url=urlbase_2)
            embed3.set_image(url=urlbase_3)
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await channel.send(embed=embed3)

    if message.content == '히유야 고양이':
        await message.channel.send(nekos.cat())

    if message.content == '히유야 강아지':
        channel = message.channel
        embed = discord.Embed(
            title='랜덤으로 강아지 사진을 골라봤어요!',
            description='',
            colour=discord.Colour.green()
        )

        urlBase = 'https://loremflickr.com/320/240/dog?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await channel.send(embed=embed)

    if message.content == '히유야 랜덤사진':
        channel = message.channel
        embed = discord.Embed(
            title='랜덤으로 사진을 골라봤어요!',
            description='',
            colour=discord.Colour.green()
        )

        urlBase = 'https://loremflickr.com/320/240/'
        randomNum = random.randrange(1, 100)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await channel.send(embed=embed)

    if message.content == '히유야 오늘날짜':
        date = datetime.datetime.today()
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name='오늘날짜야!', value=str(date.year) + '년' + str(date.month) + '월' + str(date.day) + '일', inline=True)
        await message.channel.send(embed=embed)

    if message.content == '히유야 정보':
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일",inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        
    if message.content == '히유야 오늘배그':
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="배그각입니다.", color=discord.Color.blue()))
        else:
            await message.channel.send(embed=discord.Embed(title="자러갑시다....", color=discord.Color.red()))

    if message.content == '히유야 날씨':
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location+'날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()  # 온도
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지

        embed = discord.Embed(
            title=learn[1]+ ' 날씨 정보',
            description=learn[1]+ '날씨 정보입니다.',
            colour=discord.Colour.gold()
        )
        embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)  # 현재온도
        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)  # 체감온도
        embed.add_field(name='현재상태', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)  # 오늘날씨 # color=discord.Color.blue()
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)  # 구분선
        embed.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)  # 내일오전날씨
        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태
        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태

        await message.channel.send(embed=embed)

    elif message.content.startswith(f'/청소'):
            if message.author.guild_permissions.administrator or message.author.guild_permissions.manage_messages or message.author.id == 445529063528857611:
                varrr=message.content.split(' ')
                await message.channel.purge(limit=int(varrr[1])+1)
                now=datetime.datetime.now()
                msg=await message.channel.send(embed=discord.Embed(title=f'메시지 {str(int(varrr[1]))}개 삭제 완료!', descirption=f'{client.user.name}이 삭제했어요!!', colour=discord.Colour.blue()).set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일'))
                await asyncio.sleep(5)
                await msg.delete()
            else:
                await message.channel.send(f'{message.author.mention} 현재의 권한으로는 사용 불가합니다.')
                return None

    async def makeembed(title, description):
        now=datetime.datetime.now()
        embed=discord.Embed(
            title=title,
            description=description,
            colour=discord.Colour.green()
        )
        embed.set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
        await message.channel.send(embed=embed)
    try:
        if message.author.bot:
            return None

        elif message.content.startswith(f'{pre}제재기록'):
            if message.author.guild_permissions.administrator:
                reported=message.content.split(' ')[0][6:]
                steamurl=message.content.split(' ')[1]
                banduration=message.content.split(' ')[2]
                reason=message.content.split(' ')[3]
                embed=discord.Embed(
                    title=f'제재 기록',
                    description=f'제재 대상 : {reported}\n스팀 Url : https://steamcommunity.com/profiles/{steamurl}/\n제재 기간 : {banduration}\n제재 사유 : {reason}',
                    colour=discord.Colour.red()
                ).add_field(name=f'억울한 점이 있으시다면...', value=f'aqpzm#8934 또는 히유#7112 에게DM보내주세요.', inline=True)
                embed.add_field(name=f'자신의 잘못을 인정하시면...', value=f'<#775314831519252480>을 이용해주세요.', inline=True)
                await client.get_channel(int(774984557522190367)).send(embed=embed)

    except ZeroDivisionError:
        None
    except discord.errors.Forbidden:
        None
    except IndexError:
        await makeembed('입력형식을 맞게 적어주세요!', '에러 감지 기능')
    except SyntaxError:
        await makeembed('오타를 확인해주세요!', '에러 감지 기능')

    bad = message.content.find("ㅅㅂ")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("시발")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("씨발")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("좆")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("엄마")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("꺼져")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("느금마")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("보지")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("자지")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("ㅂㅈ")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("ㅈㅈ")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("히토미")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("폰허브")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("개새")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("ㄳㄲ")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("병신")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("ㅄ")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    bad = message.content.find("ㅂㅅ")
    if bad >= 0:
        await message.channel.send(f"욕설 자동 검열\n바르고 고운말을 사용합시다. {message.author.mention}")
        await message.delete()

    if message.content == "히유야":
        await message.channel.send("네 온라인이에요!")

    if message.content == "히유야 초대코드":
        message.channel.send("https://discord.com/api/oauth2/authorize?client_id=487555965655318528&permissions=8&scope=bot")

client.run(token)
