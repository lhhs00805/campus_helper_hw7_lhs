from gcalc import calc_needed_final   
from schedule import StudyWeekPlan

print("=== 성적 계산 ===")
need = calc_needed_final(midterm=83, final_weight=0.4, target=90)
print(f"기말 최소 필요 점수: {need:.2f}점")

print("\n=== 공부 루틴 ===")
plan = StudyWeekPlan()
plan.add("Mon", "미적분 복습")
plan.add("Thu", "프로그래밍 과제")
plan.add("Sun", "다음 주 계획 세우기")

print(plan.summary())
