// 1-make_classrooms.js
// eslint-disable-next-line import/extensions
import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
  const roomSizes = [19, 20, 34];
  const classrooms = roomSizes.map((size) => new ClassRoom(size));
  return classrooms;
}
