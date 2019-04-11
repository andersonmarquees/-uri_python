k = ''
n = list(map(str, input()))
for i in n:
    k += i
if len(k) <= 140:
    print("TWEET")
else:
    print("MUTE")

print(len(k))
