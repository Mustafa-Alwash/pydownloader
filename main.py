from pytube import YouTube

def completed(stream ,filepath):
    print('download finished')

def progressing(stream ,chunk ,bytes_remaining):
    progress = f'{round(100 - ((bytes_remaining / stream.filesize )*100), 2 )}%'
    print(progress)

link = input('enter the youtube link: ')
yt= YouTube ( link , on_complete_callback= completed ,on_progress_callback= progressing)

print(f'title: {yt.title}')
print(f'length: {round((yt.length/60),1)} ')
print(yt.author)
if yt.views < 1000000:
    print(f'views: {yt.views/1000}K ')
elif yt.views > 1000000:
    print(f'views: {yt.views/1000000}M')


print('download (b)best_res | (w)worst_res | (a)audio')
choices = input('choices :')

match choices:
    case 'b':
        yt.streams.get_highest_resolution().download()
    case 'w':
        yt.streams.get_lowest_resolution().download()
    case 'a':
        yt.streams.get_audio_only().download()
    