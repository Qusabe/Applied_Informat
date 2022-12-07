current_session_record = 0
record = 0
with open('record',encoding = 'utf-8') as rd:
    record = int(rd.read())

def update_record():
    with open("record.txt",encoding='utf-8',mode='w') as rec:
        rec.write(str(record))