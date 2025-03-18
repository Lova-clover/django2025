secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class cl:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

class1 = cl(secret_code,meeting_point,time)
print(f"secret code : {class1.secret_code}")
print(f"meeting point : {class1.meeting_point}")
print(f"time : {class1.time}")