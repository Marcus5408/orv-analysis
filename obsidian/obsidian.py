import re
import os
obsidian_path = 'C:/Users/Marcus/iCloudDrive/iCloud~md~obsidian/orv/novel'
# obsidian_path = 'C:/Users/Marcus/Desktop/ORV/Novel' # temp
chapter_list = 'text/chapters_obsidian.txt'

# get chapter list, store as a list
chapters = open(chapter_list, 'r', encoding='utf-8')
chapters = chapters.readlines()

testing = False
if testing:
    chapters = [
    'Chapter 2: Ep. 1 - Starting the Paid Service, I\n',
    'Chapter 3: Ep. 1 - Starting the Paid Service, II\n',
    'Chapter 4: Ep. 1 - Starting the Paid Service, III\n',
    'Chapter 5: Ep. 1 - Starting the Paid Service, IV\n',
    'Chapter 6: Ep. 1 - Starting the Paid Service, V\n',
    '\n',
    'Chapter 7: Ep. 2 - Protagonist, I\n',
    'Chapter 8: Ep. 2 - Protagonist, II\n',
    'Chapter 9: Ep. 2 - Protagonist, III\n',
    'Chapter 10: Ep. 2 - Protagonist, IV\n',
    'Chapter 11: Ep. 2 - Protagonist, V\n',
    '\n'
    ]

def process_episode(episode_list: list):
    # process episode name
    episode_full = str((re.search(r'(?<=: )(.*)(?= -)', episode_list[0])).group(1))
    episode_number = f"{int(str(re.search(r'[0-9]+', episode_full).group(0))):02d}"
    episode_name = f"{(re.search(r'(?<=- )(.*)(?=,)', episode_list[0])).group(0)}"
    # check if episode_name contains 'Ep. ' or 'Epilogue'
    if 'Ep.' in episode_full:
        episode = f"{episode_number} {episode_name}"
    else:
        episode = f"E{int(episode_number):01d} {episode_name}"
    
    processed = []
    for i in range(len(episode_list)):
        processed.append('')
        i += 1

    for current_chapter, chapter in enumerate(episode_list):
        # 1. use regex to get chapter number    re.search(r'(?<=Chapter )(.*)(?=:)', chapter)
        # 2. convert to int                     int( ... )
        # 3. convert to 3-digit string          f"{ ... :03d}"
        chapter_number = f"{(int(re.search(r'(?<=Chapter )(.*)(?=:)', chapter).group(0))):03d}"

        chapter.replace('\n', '')                               # remove trailing newline
        roman = (re.search(r'(?<=, )(.*)', chapter)).group(0)   # roman numeral

        processed[current_chapter] = f"{chapter_number} {roman}"

        # chapter.replace('Chapter ', '')
    
    return episode, processed

current_line = 0
total_episodes = 0
# iterate through lines in chapters_list, using double line breaks as separators
while current_line != len(chapters):
    # count number of '\n' in chapters
    if chapters[current_line] == '\n':
        total_episodes += 1
    current_line += 1

episode = []
current_episode = 0
current_line = 0
while current_episode < total_episodes:
    # get current_line of chapter list, then increment
    # and get next line until a double line break is found
    # double line breaks show up as ['...\n', '\n', ...]
    # print(f"current_line: {current_episode}\n chapter: {chapters[current_episode]}")
    # print(f"chapter: {chapters[current_episode]}")
    while chapters[current_line] != '\n':
        if chapters[current_line] != '\n':
            episode.append(chapters[current_line])
            current_line += 1
        else:
            break
    
    # print(current_episode)
    # once double line break is found, process current_episode
    episodes, processed = process_episode(episode)
    # make directory using episode, put md files in it using processed
    os.makedirs(f"{obsidian_path}/{episodes}", exist_ok=True)
    for chapter in processed:
        open(f"{obsidian_path}/{episodes}/{chapter}.md", 'w', encoding='utf-8')

    current_line += 1
    current_episode += 1
    episode = []