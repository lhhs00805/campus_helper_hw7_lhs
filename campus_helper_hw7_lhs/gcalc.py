# gcalc.py

def calc_needed_final(midterm, final_weight, target):
    
    #중간고사 점수(midterm)와 목표 점수(target)를 바탕으로 기말고사에서 받아야 하는 최소 점수를 계산합니다.
    
    current = midterm * 0.35  # 중간고사 35%
    need = (target - current) / final_weight
    return need
