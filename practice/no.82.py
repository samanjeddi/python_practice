def hello():
    import datetime
    now = datetime.datetime.now()
    minute = now.minute
    if minute % 2 == 0:
        return "hissss"
    else:
        return "hello world!"

print(hello())