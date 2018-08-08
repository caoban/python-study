#引用models 目录下面的models.py
from models import models
from conf import settings

def syncdb(argvs):
    print("Syncing DB....")
    #create_engine 在models 目录下面的models.py中已经引用了
    engine = models.create_engine(settings.ConnParams,
        echo=True
    )
    models.Base.metadata.create_all(engine) #创建所有表结构



