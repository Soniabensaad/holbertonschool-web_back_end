const getListStudentIds = (students) => {
  if (!Array.isArray(students)) {
    return [];
  }
  return students.map((obj) => obj.id);
};

export default getListStudentIds;
