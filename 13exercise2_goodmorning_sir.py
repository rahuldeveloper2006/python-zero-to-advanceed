import time
import win32com.client
speaker=win32com.client.Dispatch('SAPI.spvoice')
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hour=int(time.strftime('%H'))
print(hour)
name=input("enter your name")
if(hour>5 and hour<11):
    print(f"good morning {name}")
    speaker.speak(f"good morning {name}")
elif(hour>10 and hour<15):
    print(f"good after noon {name}")
    speaker.speak(f"good after noon {name}")
elif(hour>14 and hour<19):
    print(f" good evening {name}")
    speaker.speak(f"good evening {name}")
else:
    print(f" good night {name}")
    speaker.speak(f" good night {name}")


# import win32com.client
# speaker=win32com.client.Dispatch('SAPI.spvoice')

# speaker.speak(input("enter your name"))






# import win32com.client
# speaker=win32com.client.Dispatch('SAPI.spvoice')

# name=[]
# count=int(input("enter how much name you enter"))
# for i in range(count):
#     name.append(input("enter name"))
# for i in name:
#     print(i)
#     speaker.speak(i)