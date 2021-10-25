dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)
#another way to do it
dict3 = {**dict1, **dict2}
print(dict3)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

sampleDict = dict(zip(keys, values))
print(sampleDict)

sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}
print(sampleDict ["class"] ["student"] ["marks"] ["history"])

sampleDict1 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}

remove(sampleDict1("name", "age"))
print(sampleDict1)

