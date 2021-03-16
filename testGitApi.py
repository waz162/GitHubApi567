import unittest
from GitHubApi567 import pull_info
from unittest import mock


class testGitApi(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testPullTrue(self):
        with mock.patch('GitHubApi567.pull_info', return_value=b'Successful\nPlease enter a valid username\n'):
            actual_result = pull_info('waz162')

        expected_result = 'Successful'
        self.assertIn(expected_result, actual_result)
        

    def testPullFalse(self):
        with mock.patch('GitHubApi567.pull_info', return_value=b'Successful\nPlease enter a valid username\n'):
            actual_result = pull_info('fdjskfdsakf')
        
        expected_result = 'Please enter a valid username'
        self.assertIn(expected_result, actual_result)
    


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
