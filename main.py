import aiohttp
import asyncio
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}


async def post(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, headers=headers) as response:
            return await response.json()


async def imgBB(binary, filename):
    url = "https://zh-cn.imgbb.com/json"
    data = aiohttp.FormData()
    data.add_field('source', binary, filename=filename,
                   content_type='img/'+filename.split(".")[-1])
    data.add_field('action', 'upload')
    data.add_field('type', 'file')
    return await post(url, data)


async def main():
    files = os.listdir(".")
    for file in files:
        if os.path.isdir(file):
            continue
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".gif") or file.endswith(".bmp"):
            print(file)
            with open(file, "rb") as f:
                result = await imgBB(f, os.path.basename(file))
            try:
                if result.get("success"):
                    print(result['image']['url'])
                else:
                    print("上传失败")
            except:
                print("error")

asyncio.run(main())
