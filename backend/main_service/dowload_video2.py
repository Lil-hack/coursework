import pytube


# where to save
SAVE_PATH = "/Users/Administrator/PycharmProjects/youtube_video"  # to_do

link = "https://www.youtube.com/watch?v=KqD3nZndDI8"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download(SAVE_PATH)