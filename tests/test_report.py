# coding: utf-8
#

import uiautomator2 as u2
import easyhtmlreport as htmlreport

d = u2.connect()
hrp = htmlreport.HTMLReport(d)
hrp.patch_click()

d.click(0.4, 0.4)
