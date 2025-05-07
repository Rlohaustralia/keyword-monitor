
import re
from collections import Counter

def analyze_emphasis(texts):
    emoji_pattern = re.compile("[\U00010000-\U0010ffff]", flags=re.UNICODE) 
    exclamations = re.compile(r"[!]{2,}")  
    questions = re.compile(r"[?]{2,}")     
    laughter = re.compile(r"(ㅋ|ㅎ){2,}")   
    really = re.compile(r"[진짜]{2,}")

    emoji_counter = Counter()
    emphasis_counter = Counter()

    for text in texts:
        emojis = emoji_pattern.findall(text)
        emoji_counter.update(emojis)

        if exclamations.search(text):
            emphasis_counter['exclamation'] += 1
        if questions.search(text):
            emphasis_counter['question'] += 1
        if laughter.search(text):
            emphasis_counter['laughter'] += 1
        if really.search(text):
            emoji_counter['really'] += 1

    return emoji_counter.most_common(5), emphasis_counter

texts = [
    "성심당 빵 진짜 맛있어요!!! 😍😍",
    "이 가격 실화야?? ㅋㅋㅋㅋㅋ",
    "튀김소보로는 사랑입니다🔥🔥",
    "대전가면 무조건 사야지ㅎㅎㅎ"
]

emoji_top, emphasis_stat = analyze_emphasis(texts)
print("이모지 TOP 5:", emoji_top)
print("강조 표현 수:", emphasis_stat)