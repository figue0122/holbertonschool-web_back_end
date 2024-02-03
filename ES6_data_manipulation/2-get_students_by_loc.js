function getStudentsByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
  }
  const result = students.filter((student) => student.location === city);

  return result;
}

export default getStudentsByLocation;
