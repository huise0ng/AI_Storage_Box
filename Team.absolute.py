import time
import schedule
import platform
import ctypes
import pyttsx3
from pynotifier import Notification

class AI:
    def __init__(self, name):
        self.name = name

    def remind_medicine(self):
        message = f"{self.name}: 약을 먹을 시간입니다!"
        print(message)

        engine = pyttsx3.init()
        engine.setProperty('rate', 200) 
        engine.setProperty('volume', 1.0)
        engine.say(message)
        engine.runAndWait()
        
        if platform.system() == "Windows":
            ctypes.windll.user32.MessageBoxW(0, message, "알림", 0)
        elif platform.system() in ["Linux", "Darwin"]:
            Notification(
                title="알림",
                description=message,
                duration=5,
                urgency=Notification.URGENCY_CRITICAL,
            ).send()
        else:
            print("팝업 알림이 지원되지 않는 시스템입니다.")


def main():
    ai = AI("희성")

    schedule.every().day.at("09:00").do(ai.remind_medicine)
    schedule.every().day.at("12:27").do(ai.remind_medicine)
    schedule.every().day.at("19:00").do(ai.remind_medicine)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
