from speak_module import speak
import speedtest
def InternetSpeed():
        speak("Wait a few seconds boss, checking your internet speed")
        st = speedtest.Speedtest()
        dl = st.download()
        dl = dl/(1000000) #converting bytes to megabytes
        up = st.upload()
        up = up/(1000000)
        print(dl,up)
        speak(f"Boss, we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")