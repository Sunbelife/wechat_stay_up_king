from wxpy import *
import random
import time

def is_enable(start_time, end_time):
	start_time_stamp = time.mktime(time.strptime(start_time,"%H:%M"))
	end_time_stamp = time.mktime(time.strptime(end_time,"%H:%M"))
	
	cur_time = time.strftime("%H:%M", time.localtime())
	cur_time_stamp = time.mktime(time.strptime(cur_time,"%H:%M"))
	
	if (start_time_stamp <= cur_time_stamp and cur_time_stamp <= end_time_stamp):
		return True
	else:
		return False
	
def is_the_time(send_time):
	cur_time = time.strftime("%H:%M", time.localtime())
	
	if (cur_time == send_time):
		return True
	else:
		return False

def update_the_time(send_time):
	send_time_stamp = time.mktime(time.strptime(send_time,"%H:%M"))
	
	print(time.strftime("%H:%M", time.localtime(send_time_stamp)))
	
	# 随机加半小时到 60 分钟之内的时间
	add_the_time = random.randint(30, 60)
	# 新时间戳
	send_time_stamp = send_time_stamp + add_the_time * 60
	
	return time.strftime("%H:%M", time.localtime(send_time_stamp))

# 机器人实例
bot = Bot()

# 包含 'xx' 的群都开启
keywords = ['瞎折腾的小团伙', '交流群']
wxpy_groups = []

for keyword in keywords:
	wxpy_groups = wxpy_groups + bot.groups().search(keyword)

# 找到的群
print("这是找到的群：")
print(wxpy_groups)

# 开启熬夜冠军模式
start_time = '1:30'
end_time = '5:30'

# 第一次发送时间是当前时间（如果满足区间的话）
send_time = time.strftime("%H:%M", time.localtime())

# 包含在熬夜冠军模式中
while (is_enable(start_time, end_time)):
	if (is_the_time(send_time)):
		# 发送消息
		for group in wxpy_groups:
			group.send_image("./res/card.jpeg")
		
		send_time = update_the_time(send_time)
		
		print("下一次发送时间：" + send_time)
	else:
		# 再睡一会儿
		time.sleep(1)
bot.join()