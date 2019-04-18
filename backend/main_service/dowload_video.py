import  pytube
import time
import threading

def worker(url):
    start_time = time.time()
    SAVE_PATH = "/Users/Administrator/PycharmProjects/youtube_video"  # to_do
    print(url)
    yt = pytube.YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download(SAVE_PATH)
    print('i end')
    print("--- %s seconds ---" % (time.time() - start_time))
    return

if __name__ == '__main__':
    start_time = time.time()
    llist_url=[]
    llist_url.append('https://www.youtube.com/watch?v=jQcN57VFITA')
    llist_url.append('https://www.youtube.com/watch?v=kS2t0kvIMmw')
    llist_url.append('https://www.youtube.com/watch?v=UFMEwkj64ms')
    llist_url.append('https://www.youtube.com/watch?v=oxaAjgfYMc4')
    llist_url.append('https://www.youtube.com/watch?v=4CL05r-Q6Ew')
    llist_url.append('https://www.youtube.com/watch?v=LQHIwQyk4aQ')
    llist_url.append('https://www.youtube.com/watch?v=M2neO3Fydn4')
    llist_url.append('https://www.youtube.com/watch?v=iF3oJh2ex34')
    llist_url.append('https://www.youtube.com/watch?v=Qh_cR9laQGc')
    llist_url.append('https://www.youtube.com/watch?v=4RbiyNOOrnk')

    threads = []
    for i in range(1):
        t = threading.Thread(target=worker, args=(llist_url[i],))
        threads.append(t)
        t.start()



    # SAVE_PATH = "/Users/Administrator/PycharmProjects/youtube_video"  # to_do
    #
    # link = "https://www.youtube.com/watch?v=kS2t0kvIMmw"
    # yt = pytube.YouTube(link)
    # stream = yt.streams.first()
    # stream.download(SAVE_PATH)
    print("--- %s seconds ---" % (time.time() - start_time))
