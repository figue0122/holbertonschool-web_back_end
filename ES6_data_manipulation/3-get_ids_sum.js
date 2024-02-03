function getStudentsIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  const reducer = (accumulator, currentValue) => accumulator + currentValue.id;
  const result = students.reduce(reducer, 0);

  return result;
}

export default getStudentsIdsSum;
