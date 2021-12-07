package com.example.pinkie_pie;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class FireData {
    private DatabaseReference myDatabase;
    public String SMS = "PUSH";
    public FireData(){
        myDatabase = FirebaseDatabase.getInstance().getReference(SMS);
    }
    public DatabaseReference DataBase(){
        return myDatabase;
    }
}


