from moviepy.editor import VideoFileClip

def split_video_into_equal_parts(input_file, output_prefix, num_parts):
    video = VideoFileClip(input_file)
    duration = video.duration
    
    # Calculate duration for each part
    part_duration = duration / num_parts
    
    start = 0
    end = part_duration
    
    segment_num = 1
    while end <= duration:
        output_file = f"{output_prefix}_{segment_num}.mp4"
        video_clip = video.subclip(start, end)
        video_clip.write_videofile(output_file, codec='libx264')
        
        start += part_duration
        end += part_duration
        segment_num += 1

# Usage: Provide the input video file, output prefix, and the number of parts to split
split_video_into_equal_parts('vikram.mkv', 'vikram', 4)  # Split into 4 equal parts
