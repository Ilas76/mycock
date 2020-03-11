import sqlite3



#По коду раскидал что и где нужно вызвать, но т.к. у меня эта параша не возвращает значения, код не работающий
#С этим нужно что то делать иначе пизда. Отсавил пояснения для каждой функции

class Sql:

    #Функция ктороя добавляет челиков новых при нажатии старт и сразу накидывает 2 коина
    def start(firstname,chatid,sub,coin,date):
        conn = sqlite3.connect('/root/bot/DeepNude.db')
        cursor = conn.cursor()
        data1 = [chatid,firstname,sub,coin,date]
        sql = 'SELECT * FROM tabel_user WHERE chatid = ?'
        cursor.execute(sql, (chatid,))
        data1 = [firstname,chatid,sub,coin,date]
        print(cursor.fetchall())
        if not cursor.fetchall():
            cursor = conn.cursor()
            sql = 'INSERT INTO tabel_user (chatid, name, sub, coin, date) VALUES (?,?,?,?,?)'
            cursor.execute(sql,data1)
            conn.commit()

    #Фуекция которая добавляет купленные коины
    #вызов будет выглядеть так: module1.Sql.update(message.chat.id,количество купленных коинов,'false','false')
    # sub и date в бд пока что просто так, вдруг со временем понадабяться, пока что просто false
    def update(chatid,coin,sub,date):
        conn = sqlite3.connect('/root/bot/DeepNude.db')
        cursor = conn.cursor()
        sql1 = 'SELECT sub, coin, date FROM tabel_user WHERE chatid = ?'
        cursor.execute(sql1,(chatid,))
        d = cursor.fetchall()
        info = d[0]
        data1 = [sub, info[4]+ coin, date,chatid]
        row = cursor.fetchall()
        sql = 'UPDATE tabel_user SET sub = ?, coin = ?, date = ? WHERE chatid = ?'
        cursor.execute(sql,data1)
        conn.commit()
        conn.close()

    #Функция которая удаляет один или несколько коинов при покупке обработки фотки
    def delete(chatid,coin,sub,date):
        conn = sqlite3.connect('/root/bot/DeepNude.db')
        cursor = conn.cursor()
        sql1 = 'SELECT sub, coin, date FROM tabel_user WHERE chatid = ?'
        cursor.execute(sql1,(chatid,))
        d = cursor.fetchall()
        info = d[0]
        if info[4]-coin>0:
            data1 = [sub,info[4]-coin,date,chatid]
            sql = 'UPDATE tabel_user SET sub = ?, coin = ?, date = ? WHERE chatid = ?'
            cursor.execute(sql,data1)
            conn.commit()
            conn.close()
            return True
        else:
            return False

    #пока что лишняя функция не трогай
    def sub(chatid,sub):
        conn = sqlite3.connect('/root/bot/DeepNude.db')
        cursor = conn.cursor()
        sql1 = 'UPDATE tabel_user SET sub = ? WHERE chatid = ?'
        cursor.execute(sql,(sub,chatid))
        conn.commit()
        conn.close()


    #эта функция возвращает данные для баланса, количество коинов, статус подписки и т.д.
    def select(chatid):
        conn = sqlite3.connect('/root/bot/DeepNude.db')
        cursor = conn.cursor()
        sql = 'SELECT sub, coin, date FROM tabel_user WHERE chatid = ?'
        cursor.execute(sql, (chatid,))
        print(cursor.fetchall())
        row = cursor.fetchall()
        info = row[0]
        return info
