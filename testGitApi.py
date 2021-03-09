class testGitApi(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testInvalidInput(self): 
        self.assertEqual(classifyTriangle(-1,1,1),'InvalidInput','-1,1,1 is Invalid')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(10,15,30),'Scalene','Should be Scalene')

    def testIsocelesTriangle(self):
        self.assertEqual(classifyTriangle(4,4,10),'Isoceles','4,4,10 should be Isoceles')