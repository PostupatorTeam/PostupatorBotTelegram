from ranepa.get_position import get_position, Student, Program

student = Student()
program = Program()

program.departament = "Московский(ПКАкадемии)"
program.approval = "Государственноеимуниципальноеуправление"
program.form = "Очная"
program.program = "Государственнаяимуниципальнаяслужба;Управлениетерриториальнымразвитием(многопрофильныйбакалавриат)"

student.name = "Данир"
student.surname = "Надбитов"
student.lastname = "Русланович"
student.program = program

print(get_position(student))
