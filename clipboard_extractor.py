import win32clipboard
import time

loop_count = 0

while True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    same_entry_count = 0

    loop_count += 1

    if loop_count > 1:
        if data != last_entry:
            print(data)
            with open('cliplog.txt', 'a+') as f:
                f.write(data + '\n')

    last_entry = data

    time.sleep(5)
