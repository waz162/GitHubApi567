import unittest
from GitHubApi567 import pull_info

class testGitApi(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testPullTrue(self):
        self.assertEqual(pull_info('waz162'), "Successful", "The pull was succesful")

    def testPullFalse(self):
        self.assertEqual(pull_info('fdjskfdsakf'), "Please enter a valid username", "The pull was failed, the username doesn't work")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
