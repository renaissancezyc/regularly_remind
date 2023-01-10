# 语音播报模块
import pyttsx3 

# 使用windows的弹窗模块
import win32api,win32con

# 导入aoscheduler里的调度器
from  apscheduler.schedulers.blocking import BlockingScheduler

# 配置调度器的语言和时区
sche = BlockingScheduler(timezone="Asia/Shanghai")

# 日期模块
import datetime


# 捕获用户输入
affair = input("请输入您的代办事项：")

times = input("请输入事项执行时间(min): ")


# 任务函数
def my_job(affair):
    # 初始化pyttsx3
    engine= pyttsx3.init() 
    
    # 播放文字语言/默认女生
    engine.say(f"滴滴滴滴滴滴滴滴！您的{affair}事项以到达执行时间")
    
    # 执行缓存的命令并等待完成
    engine.runAndWait()
    
    # 弹窗提示
    win32api.MessageBox(0,f"您的{affair}事项已到达执行时间","这是周奕呈的闹钟脚本",win32con.MB_OK)
    
    # 关闭apscheduler调度器
    sche.shutdown(wait=False)

# 定时函数
def timing():
    
    if affair=="" or times=="":
        
        engine = pyttsx3.init() 
    
        engine.say("输入错误")

        engine.runAndWait()
        
        win32api.MessageBox(0,"请输入正确的代办事项以及执行时间","这是周奕呈的闹钟脚本",win32con.MB_ICONWARNING)
        
    
    else:
        
        try:
            # 添加定时任务 date:某个特定时间仅运行一次 args:以tuple的形式传参
            sche.add_job(my_job,'date',run_date=datetime.datetime.now()+datetime.timedelta(minutes=times),args=[affair]) #若想修改定时时间类型则修改minutes 例：seconds=times
            # 启动调度器
            sche.start()
            
        except Exception as e:
            print(e)
            
            engine = pyttsx3.init()
            
            engine.say("输入错误")

            engine.runAndWait()
            
            win32api.MessageBox(0,"请输入正确的代办事项以及执行时间","这是周奕呈的闹钟脚本",win32con.MB_ICONWARNING)

            
    
if __name__=="__main__":
    timing()


