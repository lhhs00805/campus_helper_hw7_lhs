# schedule.py

class StudyWeekPlan:
    """요일별 공부 루틴을 간단히 저장하고 출력하는 클래스"""

    def __init__(self):
        self.tasks = {}

    def add(self, day, task):
        """요일(day)에 할 일(task)을 추가"""
        self.tasks.setdefault(day, []).append(task)

    def summary(self):
        """전체 요약 문자열 생성"""
        lines = []
        for day in sorted(self.tasks):
            joined = ", ".join(self.tasks[day])
            lines.append(f"{day}: {joined}")
        return "\n".join(lines)
