import httpx
import json

def dlvdo(yt):
        if 'watch?v=' in yt:
                vdo = yt.split('watch?v=')[1].strip()
        else:
                vdo = yt.split('/')[-1].strip()
        with httpx.Client() as c:
                c.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
                c.headers["Referer"] = "https://mp3-convert.org/"
                c.get("https://mp3-convert.org")
                c.get("https://mp3-convert.org/p/")
                #print(vdo)
                res = c.get(f"https://mp3-convert.org/get.php?r=hudar1255&id={vdo}&t=1676037634792", follow_redirects=False)
                #print(f'Status: {res.status_code}')
                #print(res.content)
                try:
                        dlurl = json.loads(res.content.decode('utf-8'))['download_url']
                        sngttl = json.loads(res.content.decode('utf-8'))['title']
                        print(f'Dowload url: {dlurl}')
                        c.get("https://mp3-convert.org/p/")
                        res = c.get(dlurl)
                        with open(f'{sngttl}.mp3', 'wb') as f:
                                f.write(res.content)
                        print(f'File name: {sngttl}.mp3')
                except Exception:
                        print('Failed to download. Check for errors in the input url. Otherwise contact me, I may have to fix the code. Or if you fixed it, just make a pull request')

if __name__ == "__main__":
        yt = input("Enter yt url: ")
        dlvdo(yt)