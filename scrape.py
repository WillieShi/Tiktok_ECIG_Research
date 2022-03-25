from TikTokApi import TikTokApi

with TikTokApi() as api:
    video = api.video(url="https://www.tiktok.com/@mephistg/video/7062605722005064966").info()
    print(video)

