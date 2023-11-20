const getStudentIdsSum = (students) => students
    .reduce((sum, obj) => sum + obj.id , 0);
export default getStudentIdsSum;
