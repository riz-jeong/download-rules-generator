import os
import json

# 디렉토리 경로
## my_path 문자열에 사용할 절대 경로를 설정
## docker_path 문자열에 도커상에 마운트한 경로 설정
my_path = "/"
docker_path = "/"
set_dir = input("input dir: ")
dir_path = os.path.join(my_path, set_dir)

# 디렉토리 안의 RSS 포스트
rss_feeds = [
    ""
    ]

# qBittorrent 다운로드 규칙 
download_rule = {
    "addPaused": None,
    "affectedFeeds": [
        ",\n".join(rss_feeds)
    ],
    "assignedCategory": "",
    "enabled": True,
    "episodeFilter": "",
    "ignoreDays": 0,
    "lastMatch": "",
    "mustContain": "",
    "mustNotContain": "",
    "previouslyMatchedEpisodes": [
    ],
    "savePath": os.path.join(docker_path, set_dir),
    "smartFilter": False,
    "torrentContentLayout": None,
    "useRegex": False
}

# 디렉토리 안의 모든 디렉토리 이름 + 다운로드 규칙 저장
dir_dict = {}
for dir_name in os.listdir(dir_path):
    if os.path.isdir(os.path.join(dir_path, dir_name)):
        dir_dict[dir_name] = download_rule
        dir_dict[dir_name]["savePath"] += dir_name

# JSON 파일로 저장
with open('download_rules_%s.json' %set_dir, 'w') as json_file:
    json.dump(dir_dict, json_file, indent=4)