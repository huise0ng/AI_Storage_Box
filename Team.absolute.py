import time
import schedule
import platform
import ctypes
import pyttsx3
from pynotifier import Notification

class AI:
    def __init__(self, name):
        self.name = name
        
        # TTS 초기화
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  
        self.engine.setProperty('volume', 1.0)

    def remind_medicine(self):
        message = "약을 먹을 시간입니다."
        print(f"{self.name}: {message}")

        # TTS 실행
        self.engine.say(message)
        self.engine.runAndWait()

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
    ai = AI("어시스턴트")

    schedule.every().day.at("09:00").do(ai.remind_medicine)
    schedule.every().day.at("15:45").do(ai.remind_medicine)
    schedule.every().day.at("19:00").do(ai.remind_medicine)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
