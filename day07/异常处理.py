

except (IndexError,KeyError) as e :
    print("没有这个ket",e)
except IndexError as e:
    print("列表操作错误",e)
except Exception as e:
    print("未知错误",e)

else:
    print("一切正常")

finally:
    print("不管有没有错都执行")



