const updateStudentGradeByCity = (students, city, newGrades) =>
  students
    .filter((obj) => obj.location === city)
    .map((student) => {
      const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);

      return {
        id: student.id,
        firstName: student.firstName,
        location: student.location,
        grade: matchingGrade ? matchingGrade.grade : 'N/A',
      };
    });

export default updateStudentGradeByCity;
