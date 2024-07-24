import unittest
from main import app

class TestStudentEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Initial data setup
        self.initial_data = {'name': 'Jane Doe', 'matric_number': '54321'}
        self.app.post('/api/v1/students/', json=self.initial_data)

    def tearDown(self):
        # Clean up by deleting all students
        response = self.app.get('/api/v1/students/')
        students = response.get_json()
        for student in students:
            self.app.delete(f"/api/v1/students/{student['id']}")

    def test_get_students(self):
        response = self.app.get('/api/v1/students/')
        self.assertEqual(response.status_code, 200)
        students = response.get_json()
        self.assertIsInstance(students, list)
        self.assertGreater(len(students), 0)
        # Add more assertions based on the expected JSON response

    def test_add_student(self):
        data = {'name': 'John Doe', 'matric_number': '12345'}
        response = self.app.post('/api/v1/students/', json=data)
        self.assertEqual(response.status_code, 201)
        message = response.get_json()
        self.assertIn('message', message)
        self.assertEqual(message['message'], 'Student added successfully')
        # Optionally retrieve the student list and verify the new student is present
        response = self.app.get('/api/v1/students/')
        students = response.get_json()
        self.assertTrue(any(student['name'] == 'John Doe' for student in students))

    def test_get_student(self):
        # Assuming student with ID 1 exists
        response = self.app.get('/api/v1/students/1')
        self.assertEqual(response.status_code, 200)
        student = response.get_json()
        self.assertEqual(student['name'], 'Jane Doe')
        self.assertEqual(student['matric_number'], '54321')
        # Add more assertions based on expected data

    def test_update_student(self):
        # Assuming student with ID 1 exists
        data = {'name': 'Updated Name', 'matric_number': '12345'}
        response = self.app.put('/api/v1/students/1', json=data)
        self.assertEqual(response.status_code, 200)
        message = response.get_json()
        self.assertIn('message', message)
        self.assertEqual(message['message'], 'Student record updated successfully')
        # Retrieve the student to verify the update
        response = self.app.get('/api/v1/students/1')
        updated_student = response.get_json()
        self.assertEqual(updated_student['name'], 'Updated Name')
        self.assertEqual(updated_student['matric_number'], '12345')

    def test_delete_student(self):
        # Assuming student with ID 1 exists
        response = self.app.delete('/api/v1/students/1')
        self.assertEqual(response.status_code, 200)
        message = response.get_json()
        self.assertIn('message', message)
        self.assertEqual(message['message'], 'Student deleted successfully')
        # Verify the student was deleted
        response = self.app.get('/api/v1/students/1')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
