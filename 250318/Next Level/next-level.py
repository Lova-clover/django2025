user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class NextLevel:
    def __init__(self, user2_id, user2_level):
        self.user2_id = user2_id
        self.user2_level = user2_level

NextLevel1 = NextLevel(user2_id,user2_level)
NextLevel2 = NextLevel(user2_id,user2_level)

NextLevel1.user2_id = "codetree"
NextLevel1.user2_level = 10

print(f"user {NextLevel1.user2_id} lv {NextLevel1.user2_level}")
print(f"user {NextLevel2.user2_id} lv {NextLevel2.user2_level}")
