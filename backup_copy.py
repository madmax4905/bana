import shutil
import os
from datetime import datetime

# 레디스의 RDB 백업 파일을 여러개 저장하기 위해 파일을 복사하고 타임스탭프를 붙여서 이동및 리텐션 관리
# Redis RDB 파일의 경로
REDIS_RDB_FILE = "/root/stress.yml"

# 이동할 디렉토리
DEST_DIR = "/tmp"

# 현재 날짜와 시간을 prefix로 사용하기 위한 포맷
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# 복사할 파일명 생성
dest_file = os.path.join(DEST_DIR, f"stress_{timestamp}.yml")

# 파일 복사
shutil.copy(REDIS_RDB_FILE, dest_file)

# 복사 후 로그 출력 (선택 사항)
print(f"Copied {REDIS_RDB_FILE} to {dest_file}")
