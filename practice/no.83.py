def run_on_zoj(f):
    def wrapper():
        import datetime
        now = datetime.datetime.now()
        minute = now.minute
        
        if minute % 2 == 0:
            f()
        else:
            print("hissss")
    return wrapper

@run_on_zoj
def say_hello():
    print("hello i'm here")

@run_on_zoj
def say_bye():
    print("goodbye...")

say_hello()
say_bye()