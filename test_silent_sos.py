import time
from silent_sos import SilentSOS


silent_sos = SilentSOS()


print("Testing Silent SOS...")
print()


for i in range(3):

    print("SOS button click:", i + 1)

    triggered = silent_sos.register_click()

    if triggered:

        print("🚨 SILENT SOS ACTIVATED!")
        break

    time.sleep(0.3)