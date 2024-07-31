import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-84ed8-default-rtdb.firebaseio.com/"
})

ref= db.reference('Students')

data={
    "321654":
        {
            "name":"Sagar Susling",
            "major":"computer Science",
            "starting":2021,
            "total_attendance":15,
            "standing":"A",
            "year":3,
            "leat_attandance_time":"2021-11-15 00:55:20"
        },
    "852741":    {
            "name":"Sagar Susling",
            "major":"computer Science",
            "starting":2020,
            "total_attendance":15,
            "standing":"A",
            "year":4,
            "leat_attandance_time":"2022-12-15 00:55:20"
        },

    "963852":
        {
            "name": " Elon Musk",
            "major": " Physic",
            "starting": 2019,
            "total_attendance": 15,
            "standing": "A",
            "year": 5,
            "leat_attandance_time": "2022-12-15 00:55:20"
        }
}
for key,value in data.items():
    ref.child(key).set(value)


