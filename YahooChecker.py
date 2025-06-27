import requests
import time
from user_agent import *

lst = open("email.txt","r")
print("""
    ███████╗███╗   ███╗ █████╗ ██╗██╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
    ██╔════╝████╗ ████║██╔══██╗██║██║     ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
    █████╗  ██╔████╔██║███████║██║██║     ██║     ███████║█████╗  ██║     █████╔╝ 
    ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
    ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
    ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
by @7snhacker""")
print("Yahoo Version ")
sleep = float(input("sleep : "))
while True:
    email = lst.readline().split('\n')[0]

    cookies = {
        'A3': 'd=AQABBASO6mcCEOkUhPBRz-_nH2BXUwi3etsFEgEBAQHf62f0ZwAAAAAA_eMCAA&S=AQAAAi4Aseywr8u0hrfaIaFFcxk',
        'A1': 'd=AQABBASO6mcCEOkUhPBRz-_nH2BXUwi3etsFEgEBAQHf62f0ZwAAAAAA_eMCAA&S=AQAAAi4Aseywr8u0hrfaIaFFcxk',
        'axids': 'gam=y-vQK39cBE2uK0Jp9Xk_Oxk2iAb4Bps3P6~A&dv360=eS1RM1d0bWc1RTJ1SHlhLjFIN0hIazFKcmRWd3E0Y2E4UX5B&ydsp=y-QQOWazRE2uI_3Kcimg3_g9BWAZ09GXJ2~A&tbla=y-vDcY945E2uIvE5NwZf4XUYOnKqvvTvGB~A',
        '_ga': 'GA1.1.988658873.1750297818',
        'tbla_id': 'cc2a681a-51e1-4ab9-92ce-dc2331d6b1bc-tuctee53392',
        'A1S': 'd=AQABBASO6mcCEOkUhPBRz-_nH2BXUwi3etsFEgEBAQHf62f0ZwAAAAAA_eMCAA&S=AQAAAi4Aseywr8u0hrfaIaFFcxk',
        'GUCS': 'ARMjPMWj',
        'cmp': 't=1750988728&j=0&u=1---',
        'gpp': 'DBAA',
        'gpp_sid': '-1',
        'AS': 'v=1&s=MgKQt25C&d=A685f4937|.Ul5vbD.2SoU2Ux2H1vgYYuFy.bU6_lBOkme16.XWzpNyIN5UcTk99nr5nBIIAGiaevE1i06.Lnb8q5IlAFaVMdLYUViVONXiTB.vNdZLVF3r2mT9v__NQiJU_gt..eV0Bzw8zO_SQ1r2sBRvny2tsTQ_USTAOzIfSjP5spkRBEufs8YAuPrc9zUYwU5e1RmGPJ_UFVQevqNpKjtCgoy7YtCggwYQ1BYs.sO1wlDWaMOzjNZf_HG1fpNOA1_7t6JtlViKIsOG.ERXMAJe1qF6TCwnFd8P1gYKGbYBWsrwjNkavlbjllL6JVx3YEuDh7__upDKYmxFUWcU2_rSpF9X.hK7rNZm6wRh6DAweAzFNPYHVe723wlk9aSsE0VQ2Lff8Ej.ca7WJm2DuvIcLAXJIr.GjxGGV2ByypZ1FeCAY76e8UwTaxF3JsI2wlaIRvO68lJV9wAKtfKEuqMo9D0nbsvriofTiqg6._a8aE6HhlkQY_7owi55V04LWCl0FDP1eqlYWkxLWn1SZ9dbsf416L2QQFjS_i.zvFf9kDNTiqAz0rshlTEKUkogqpM8DXUTp8VA5wC7p0PaLeOGuu7ofWIK8nIiIHCv1a2mOApnFFwxWyU7RUsPJOgpfY.gBTfa8pXuJbDFcXuMHKPAaqz4dP1fvePjVoaRc89W6F8cXDuQyCGoZywZoCX5l.jgij3VoTISUwV_K9q71iPfTkDeJ4poBTKCS5Ap.Hr46t_O3aGNBlxmHRZfvWUBP5jBonUfDTH5HG9z1CIqUSh0Br4NeWTapgvld3EUVnWb9.MHqMQSrOEzJEboJFH75if46irnzzI5Q36_TU4kboh7X_PSh6xipW4qY7zgM5u9pYXTpaciHgUwzdffwFu.XizvCTKhg--~A|B685f493b|DUlT8Tz.2TosAVf2uPNJ9Exc4vsib3UgXymIwvB4bhnB6vmoExdLy_QB7QqCuOQd9EyKBAIZ15U3NyHCBG9ZVovoWMjy5PC2oNWB_Fbvuxkb9359i7IcWRJZap6qYSL0_QyqoTgd_2kCQIRbB2sB_8pLL9Mi43ncXKNx7Gz4dpMNImcz5lSJAp9mOobtdVU66aMVL6I.9lbi4MaFW8U7hTdMxJK2mgGPKwaC.p2r77840VkXne2t.paCPn3oaIXR8NNSRRYeZmB__yO3W.ZFqkajSV.fEwzweQyameW.R_.IvGRI_Pory7r5Gv8y_8IS20YLc2mq1qA.5SOgxhk0eX_epOSWwd_xRvmdAL43YETosqkBmzbF38nTQkw7g9xiskx.sD8Ed.mXU6WjYyLXHVaVs8Zrn7v4CcGAcDJhBI3HHZV5LvQji_o1OzgqOhTsG2velr23Fye9rT67rD45giPxu5vv4tm6IZ_Jm0_qa_ZVIy_KgA2szGHSwzrO38PAr13BOnjtuFgzKB3o_SZbSsT6SQf.jaLJF9eBdrcmgDPW0_21e_iLTl910STuLKJHyXBIIUa_VgH.eawb.5qEScdaAQ5Ux5fxhfQstqagAxwHLWaJr574WP.CH_3eL81Q8QbwZ5AnOXYCW54pTf.47wAHRWcy7SiR.Y5iSNbTe1tWSL7HGCwXNzsflWRDtkZLTbTfmkArQXAsW6no_avbWOl7vmhOEyK3ptTH1obnjF6i55eM8_qvEelhSuYpbLAdrpeDm9uzJVrF7PiCzVLwGfYr4h3W3Y39q6uWOk5Dz1gophDcPZvwjD.YGMMr6mtPCx.x3BOcmLUu4zbh0ZtA_2_eWnRBxlN87eWaHRU468h0HLaN6HrSvCtWOkL9Seur6W1jfEjb.tzNjgQxZhjyZj2LCRKUso24rJoqF5IBy8JhDeghHA37vF_q25wFfaUr14U4HZNb2KDjEKw511ztZiF4Wr6xVcOF_SNZO9N8ac3lk.UcS738iiZYqRE_JB5StBg1VwniqrMjNQB31vu9vATdn_yE22dr4De5DsojnuaZ5a.lwx1ozjOR7p.PZPyFUsoAV4I-~A',
        '_ga_P9C3W3ESF1': 'GS2.1.s1750988728$o2$g1$t1750988784$j4$l0$h0',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://login.yahoo.com',
        'priority': 'u=0, i',
        'referer': 'https://login.yahoo.com/account/create?lang=en-US&src=ym&specId=yidregsimplified&done=https%3A%2F%2Fmail.yahoo.com%2F%3Fguce_referrer%3DaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8%26guce_referrer_sig%3DAQAAACv_n8NfkIBhVgSVcNq6Lx976rdumjIjnxjOJ5hGbvAYtn_NVM2j9w07NonXCEpxwiC8AfRR3UwLYHCEc5Bv5eUSl23LuoYN-8pi7qElCC9RJ3mp137BqJGGu6X4DxYZwOGjkTsNcVuhcUo8qS141H8iyck21qQzqgZNT9dV34cM&intl=xa&context=reg',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': f'{generate_user_agent()}',
    }

    params = {
        'intl': 'xa',
        'lang': 'en-US',
        'src': 'ym',
        'specId': 'yidregsimplified',
        'done': 'https://mail.yahoo.com/?guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAACv_n8NfkIBhVgSVcNq6Lx976rdumjIjnxjOJ5hGbvAYtn_NVM2j9w07NonXCEpxwiC8AfRR3UwLYHCEc5Bv5eUSl23LuoYN-8pi7qElCC9RJ3mp137BqJGGu6X4DxYZwOGjkTsNcVuhcUo8qS141H8iyck21qQzqgZNT9dV34cM',
        'context': 'reg',
    }

    data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A8%2C%22timezoneOffset%22%3A-180%2C%22timezone%22%3A%22Asia%2FBahrain%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas+winding%3Ayes%7Ecanvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google+Inc.+%28NVIDIA%29%7EANGLE+%28NVIDIA%2C+NVIDIA+GeForce+GTX+1060+3GB+%280x00001C02%29+Direct3D11+vs_5_0+ps_5_0%2C+D3D11%29%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A48%2C%22hash%22%3A%2262d5bbf307ed9e959ad3d5ad6ccd3951%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221920%22%2C%22h%22%3A%221080%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%221040%22%2C%22h%22%3A%221920%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1750988750229%2C%22render%22%3A1750988750524%7D%7D&specId=yidregsimplified&context=REGISTRATION&cacheStored=&crumb=zw7mhGj6eftGdSumO6SJ1g&acrumb=MgKQt25C&sessionIndex=Qg--&done=https%3A%2F%2Fmail.yahoo.com%2F%3Fguce_referrer%3DaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8%26guce_referrer_sig%3DAQAAACv_n8NfkIBhVgSVcNq6Lx976rdumjIjnxjOJ5hGbvAYtn_NVM2j9w07NonXCEpxwiC8AfRR3UwLYHCEc5Bv5eUSl23LuoYN-8pi7qElCC9RJ3mp137BqJGGu6X4DxYZwOGjkTsNcVuhcUo8qS141H8iyck21qQzqgZNT9dV34cM&googleIdToken=&authCode=&attrSetIndex=0&specData=&deviceCapability=%7B%22pa%22%3A%7B%22status%22%3Atrue%7D%2C%22isWebAuthnSupported%22%3Atrue%7D&tos0=oath_freereg%7Cxa%7Cen-JO&multiDomain=&asId=1a411006-cb4f-4d29-8b43-93237b23aa78&fingerprintCaptured=&firstName=egrhgre&lastName=egrhgre&userid-domain=yahoo&userId={email}&password=erSgerg2ergregrgeg&mm=3&dd=3&yyyy=1999&signup='

    response = requests.post('https://login.yahoo.com/account/create', params=params, cookies=cookies, headers=headers, data=data).text
    if ("Add your phone number") in response:
        print(f"Available Email : {email}@yahoo.com")
        with open("Available.txt","a") as Available:
            Available.write(email +"\n")
    elif ("This email address is not available for sign up") in response:
        print(f"NotAvailable Email : {email}@yahoo.com")
        with open("NotAvailable.txt","a") as NotAvailable:
            NotAvailable.write(email +"\n")
    else:
        print(f"Error Email : {email}@yahoo.com")
