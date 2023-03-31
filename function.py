import pymysql
import config


def DelLastReq(id):
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    req = f"DELET FROM `ready-requests` WHERE id = {id}"
    cur.execute(req)
    db.commit()
    
    cur.close()
    db.close()

def GetReq(value):
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    req = f"SELECT {value} FROM `requisites`"
    cur.execute(req)
    db.commit()
    
    reqi = cur.fetchone()
    print(reqi)
    
    cur.close()
    db.close()
    
    return reqi


def GetCom():
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    req = f"SELECT * FROM `comission`"
    cur.execute(req)
    db.commit()
    
    com = cur.fetchall()
    
    cur.close()
    db.close()
    
    return com


def GetData(id):
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    req = f"SELECT * FROM `ready-requests` WHERE id = {id}"
    cur.execute(req)
    db.commit()
    
    data = cur.fetchone()
    com = GetCom()
    
    type = data[1]
    kripto = data[2]
    amount_kripto = data[4]
    amount_rub = data[5]
    payload = data[6]
    
    cur.close()
    db.close()
    
    return [type, kripto, amount_kripto, amount_rub, payload, com]

def GetTypeReq(id):
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    req = f"SELECT type FROM `ready-requests` WHERE id = {id}"
    cur.execute(req)
    db.commit()
    
    type = cur.fetchone()  

    cur.close()
    db.close()
    
    return type
    
    
    
def GetUser(id):
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    req = f"SELECT name FROM `users` WHERE id = {id}"
    cur.execute(req)
    db.commit()
    
    data = cur.fetchone()
    
    cur.close()
    db.close()
    
    return data



def GetMode(id):
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    req1 = f"SELECT global_mode FROM `users` WHERE id = {id}"
    cur.execute(req1)
    db.commit()
    
    data1 = cur.fetchone()
    
    req2 = f"SELECT local_mode FROM `users` WHERE id = {id}"
    cur.execute(req2)
    db.commit()
    
    data2 = cur.fetchone()
    
    cur.close()
    db.close()
    
    return [data1, data2]


def RegNewUser(id, username, FullName):
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    req = f"INSERT INTO users(id, username, name, language, global_mode, local_mode) VALUES({id}, '{username}', '{FullName}', 'ru', 'Menu', 'Menu')"
    cur.execute(req)
    db.commit()
    
    cur.close()
    db.close()
    



def ToMenu(id):
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    req1 = f"UPDATE users SET global_mode = 'Menu' WHERE id = {id}"
    req2 = f"UPDATE users SET local_mode = 'Menu' WHERE id = {id}"
    
    cur.execute(req1)
    db.commit()
    cur.execute(req2)
    db.commit()
    
    cur.close()
    db.close()



def GetLanguage(id):
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    req = f"SELECT language FROM `users` WHERE id = {id}"
    cur.execute(req)
    db.commit()
    
    data = cur.fetchone()
    
    cur.close()
    db.close()
    
    return data




def GetFeedBack(type, data):
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    if type == "read":
        req1 = f"UPDATE users SET global_mode = 'FeedBack' WHERE id = {data}"
        req2 = f"UPDATE users SET local_mode = 'part1' WHERE id = {data}"
            
        cur.execute(req1)
        db.commit()
        cur.execute(req2)
        db.commit()
        
        
    if type == "send_text":
        req = f"INSERT INTO `feedback`(id, text) VALUES ({data[0]}, '{data[1]}')"
        cur.execute(req)
        db.commit()
        
    cur.close()
    db.close()       
    
    
    
def ResetLanguage(type, id, new_lang):
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    if type == "part_1":
        req1 = f"UPDATE users SET global_mode = 'ResetLanguage' WHERE id = {id}"
        req2 = f"UPDATE users SET local_mode = 'part1' WHERE id = {id}"
                
        cur.execute(req1)
        db.commit()
        cur.execute(req2)
        db.commit()
        
    elif type == "part_2":
        req = f"UPDATE users SET language = '{new_lang}' WHERE id = {id}"             
        cur.execute(req)
        db.commit()
    
    cur.close()
    db.close() 
    
    
    
    
def Obmen32(part, data, id):
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    if part == "Ready":
        req1 = f"UPDATE users SET global_mode = 'Obmen' WHERE id = {id}"
        req2 = f"UPDATE users SET local_mode = 'part1' WHERE id = {id}"
                
        cur.execute(req1)
        db.commit()
        cur.execute(req2)
        db.commit()
        
    if part == "SelectType":
        req = f"UPDATE users SET local_mode = 'part2' WHERE id = {id}"        
        cur.execute(req)
        db.commit()
        
        req = f"INSERT INTO `ready-requests`(id, type, kripto, curenty, amount_kripto, amount_cur, user_payload, ready) VALUES ({id}, '{data}', 'n', 'n', 0, 0, 'n', 0)"
        cur.execute(req)
        db.commit()
        
        
    if part == "SelectKripto":
        req = f"UPDATE users SET local_mode = 'part3' WHERE id = {id}"        
        cur.execute(req)
        db.commit()
        
        req = f"UPDATE `ready-requests` SET kripto = '{data}' WHERE id = {id}"
        cur.execute(req)
        db.commit()
        
        req = f"UPDATE `ready-requests` SET curenty = 'rub' WHERE id = {id}"
        cur.execute(req)
        db.commit()
        
        
    if part == "EnterRub" or part == "EnterKripto":
        req = f"UPDATE users SET local_mode = 'part4' WHERE id = {id}"        
        cur.execute(req)
        db.commit()
        
        req = f"SELECT kripto FROM `ready-requests` WHERE id = {id}"
        cur.execute(req)
        db.commit() 
        title = cur.fetchone()
        print(title)

        req = f"SELECT price FROM `rates`"
        cur.execute(req)
        db.commit()
        rate = cur.fetchall()
        print(rate)
        
        if title[0] == "bitcoin":
            price = rate[0][0]
        if title[0] == "ethereum":
            price = rate[1][0]
        if title[0] == "litecoin":
            price = rate[2][0]
        
        
        if part == "EnterRub":
            req = f"SELECT comission_input FROM `comission`"
            cur.execute(req)
            db.commit()  
            comission_input = cur.fetchone()

            value = data / float(price)
            PerSent = value / 100 * float(comission_input[0])
            value_output = value - PerSent
  
            req = f"UPDATE `ready-requests` SET amount_kripto = {value_output} WHERE id = {id}"
            cur.execute(req)
            db.commit()
            
            req = f"UPDATE `ready-requests` SET amount_cur = {data} WHERE id = {id}"
            cur.execute(req)
            db.commit()   
        
        elif part == "EnterKripto":        
            req = f"SELECT comission_output FROM `comission`"
            cur.execute(req)
            db.commit()   
            comission_output = cur.fetchone()
  
            value = data * float(price)
            PerSent = value / 100 * float(comission_output[0])
            value_output = value - PerSent        
                
            req = f"UPDATE `ready-requests` SET amount_kripto = {data} WHERE id = {id}"
            cur.execute(req)
            db.commit()
                
            req = f"UPDATE `ready-requests` SET amount_cur = {value_output} WHERE id = {id}"
            cur.execute(req)
            db.commit()
        
        
        
    if part == "EnterPayload":
        req = f"UPDATE users SET local_mode = 'part5' WHERE id = {id}"        
        cur.execute(req)
        db.commit()
        
        req = f"UPDATE `ready-requests` SET user_payload = '{data}' WHERE id = {id}"
        cur.execute(req)
        db.commit()
        
    if part == "AddToTable":
        data = GetData(id)
        
        req = f"INSERT INTO `now-reqests`(id, type, kripto, curenty, amount_kripto, amount_cur, user_payload, ready) VALUES ({id}, '{data[0]}', '{data[1]}', 'rub', {data[2]}, {data[3]}, '{data[4]}', 0)"
        cur.execute(req)
        db.commit()
        
        req = f"DELETE FROM `ready-requests` WHERE id = {id}"
        cur.execute(req)
        db.commit()
        
        
    cur.close()
    db.close()
    
    
  
def GetAdmins():
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    req = f"SELECT * FROM `admin`"
    cur.execute(req)
    db.commit()
    
    resp = cur.fetchall()
    data = []
    
    for item in resp:
        data.append(item[0])
    
    
    cur.close()
    db.close()
    
    return data
    
    

def SendNewReq(username, bot):
    data = GetAdmins()
    
    for item in data:
        bot.send_message(item, f"Пришёл запрос на обмен от пользователя: @{username}")
        

def SendFeedback(username, bot):
    data = GetAdmins()
    
    for item in data:
        bot.send_message(item, f"Пришёл новый feedback от пользователя: @{username}")
        
        
        
        
def GetRates():
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    req = f"SELECT price FROM `rates`"
    cur.execute(req)
    db.commit()
    
    rates = cur.fetchall()
    rate = []
    
    for i in rates:
        rate.append(i[0])
    
    cur.close()
    db.close()
    
    return rate


def GetComission():
    db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
    cur = db.cursor()
    
    req = f"SELECT * FROM `comission`"
    cur.execute(req)
    db.commit()
    
    com = cur.fetchall()
    commission = []
    
    commission.append(com[0][0])
    commission.append(com[0][1])
    
    cur.close()
    db.close()
    print(commission)
    
    return commission