#--*--coding:utf-8 --*--

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice

device = MonkeyRunner.waitForConnection(5,'9999SKOFRC6TN7SO')

device.installPackage('G:\\packages\\app-debug1130.apk')
MonkeyRunner.sleep(3)

device.startActivity(component='net.skjr.tdqc.rebateanycity/.StartActivity')
MonkeyRunner.sleep(8)

result = device.takeSnapshot()
result.writeToFile('G:\\test.png','png')

