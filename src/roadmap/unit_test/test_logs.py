import unittest

class TestInMemoryTaskRepository(unittest.TestCase):
  def setUp(self) -> None:
    self.repo = self.InMemoryTaskRepository()

  def test_create_task(self) -> None:
    self.repo.create_task('Task1', 'Description1')
    tasks = self.repo.get_tasks()
    self.assertEqual(tasks, {'Task1': 'Description1'})

  def test_remove_task(self) -> None:
    self.repo.create_task('Task1', 'Description1')
    result = self.repo.remove_task('Task1')
    self.assertTrue(result)
    tasks = self.repo.get_tasks()
    self.assertEqual(tasks, {})

  def test_remove_non_existing_task(self) -> None:
    result = self.repo.remove_task('NonExistingTask')
    self.assertFalse(result)

  def test_get_tasks(self) -> None:
    self.repo.create_task('Task1', 'Description1')
    self.repo.create_task('Task2', 'Description2')
    tasks = self.repo.get_tasks()
    self.assertEqual(tasks, {'Task1': 'Description1', 'Task2': 'Description2'})


class TestTaskManager(unittest.TestCase):
  def setUp(self) -> None:
    self.repo = self.InMemoryTaskRepository()
    self.manager = self.TaskManager(self.repo)

  def test_create_task(self) -> None:
    self.manager.create_task('Task1', 'Description1')
    tasks = self.repo.get_tasks()
    self.assertEqual(tasks, {'Task1': 'Description1'})

  def test_remove_task(self) -> None:
    self.repo.create_task('Task1', 'Description1')
    self.manager.remove_task('Task1')
    tasks = self.repo.get_tasks()
    self.assertEqual(tasks, {})

  def test_remove_non_existing_task(self) -> None:
    with self.assertLogs('root', level='WARNING') as log:
      self.manager.remove_task('NonExistingTask')
      self.assertIn('No se encontro la tarea: NonExistingTask', log.output[0])


class TestTaskUtils(unittest.TestCase):
  def setUp(self) -> None:
    self.repo = self.InMemoryTaskRepository()
    self.utils = self.TaskUtils(self.repo)

  def test_show_tasks(self) -> None:
    self.repo.create_task('Task1', 'Description1')
    self.repo.create_task('Task2', 'Description2')
    with self.assertLogs('root', level='INFO') as log:
      self.utils.show()
      self.assertIn('Nombre: Task1, Descripcion: Description1', log.output[0])
      self.assertIn('Nombre: Task2, Descripcion: Description2', log.output[0])

  def test_show_no_tasks(self) -> None:
    with self.assertLogs('root', level='WARNING') as log:
      self.utils.show()
      self.assertIn('No hay tareas', log.output[0])


if __name__ == '__main__':
  unittest.main()
