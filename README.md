# download-rules-generator

qBittorrent RSS 자동 다운로드 json 규칙을 생성합니다.

규칙 생성을 원하는 디렉토리에 py 파일을 넣고 실행합니다.

download_rules_generator.py

디렉토리에 존재하는 모든 디렉토리의 이름을 기준으로 해당 폴더에 저장하는 json 규칙을 생성합니다.

download_rules_generator_docker.py

도커 환경의 qBittorrent용. py파일을 편집기로 실제 경로와 마운트된 경로를 수정하여 json 규칙을 생성합니다.