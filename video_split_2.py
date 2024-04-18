from moviepy.editor import VideoFileClip
from concurrent.futures import ThreadPoolExecutor

def split_video(input_video, output_prefix, num_parts):
    video = VideoFileClip(input_video)
    duration = video.duration
    part_duration = duration / num_parts

    def process_part(part_num):
        start_time = part_num * part_duration
        end_time = (part_num + 1) * part_duration if part_num < num_parts - 1 else duration
        output_path = f"{output_prefix}_part{part_num + 1}.mp4"

        part = video.subclip(start_time, end_time)
        part.write_videofile(output_path, codec='libx264')
        part.close()

    with ThreadPoolExecutor(max_workers=num_parts) as executor:
        executor.map(process_part, range(num_parts))

    video.close()

# Example usage:
split_video('input_video.mp4', 'output_video_part', 4)
