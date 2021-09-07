class Test:
    def __init__(self, data):
        self.data = data
        self.count = 1
        print("self.data is = ", self.data)
        # timer.timeout.connect(self.testData)
        # self.testDisplay()

    def testData(self):
        # print("function testData CALL")
        self.data.setText("\tCalling New test of number {}".format(self.count))
        self.count = self.count + 1

    def testData2(self):
        # print("function testData New Call")
        self.data.setText("\ttest of number call are {}".format(self.count))
        self.count = self.count + 1

    def testDisplay1(self):
        for lp in range(10):
            self.data.setText("number time value udpate is = {}".format(lp))
            thread = DummyThread()
            thread.start()
            thread.finished.connect(
                lambda txt="New updte value of text is", data=self.data: data.setText("%s Done" % txt))
        # time.sleep(5)
        # self.data.setText("testing 2nd value")
        # self.timer.timeout.connect(self.testData)
        # self.data.testData("\tAccount Info\nCushion Margin")
        # self.timer.start(5000)
        # timer.stop()
        # timer.timeout.connect(self.testData2)
        # timer.timeout.connect(self.testData)
        # timer.start(5000)
        # timer.stop()
        # timer.timeout.connect(self.testData)

    def testDisplay(self):
        # time.sleep(5)
        # self.data.setText("testing 2nd value")
        timer.timeout.connect(self.testData)
        # self.data.testData("\tAccount Info\nCushion Margin")
        timer.start(5000)
        # timer.stop()
        timer.timeout.connect(self.testData2)
        # timer.timeout.connect(self.testData)
        # timer.start(5000)
        # timer.stop()
        # timer.timeout.connect(self.testData)

    def startCodeWindow2(self):
        self.acctLabel = acctLabelObject

        # print("Table Data received from window 1 is = {}".format(self.tableData))
        test = Test(self.acctLabel)
        test.testDisplay()