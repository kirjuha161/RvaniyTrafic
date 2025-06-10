import subprocess
import time

WIFI_INTERFACE = "Беспроводная сеть" # Имя интерфейса Wi-Fi
INTERVAL_OFF = 2  # Время ожидания после выключения (в секундах)
INTERVAL_ON = 10  # Время ожидания после включения (в секундах)


def wifi_on(): 
    subprocess.run(
        ["netsh", "interface", "set", "interface", WIFI_INTERFACE, "enable"], check=True
    )


def wifi_off():
    subprocess.run(
        ["netsh", "interface", "set", "interface", WIFI_INTERFACE, "disable"],
        check=True,
    )


if __name__ == "__main__":
    while True:
        print("Отключаю Wi-Fi...")
        wifi_off()
        time.sleep(INTERVAL_OFF)
        print("Включаю Wi-Fi...")
        wifi_on()
        time.sleep(INTERVAL_ON)
