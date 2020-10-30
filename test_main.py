import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        delr = this_x[1] - this_x[0]
        for i in range( len(this_y) ) :
            pp = np.exp( -lamd*(this_x[i]-0.5*delr) ) - np.exp( -lamd*(this_x[i]+0.5*delr) )
            bar = np.sqrt( pp*(1-pp) )*st.norm.ppf( (0.99 + 1) / 2 )
            self.assertTrue( np.fabs( this_y[i]*delr - pp )<bar, "the y-coordinates in your histogram appear to be incorrect" )
  
    def test_normalised(self) :
        fighand = plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        delr = this_x[1] - this_x[0]
        self.assertTrue( np.fabs( delr*sum(this_y)-1 )<1e-7, "your histogram does not appear to be normalised" )

    def test_xplot(self) : 
        fighand = plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        delr = this_x[1] - this_x[0]
        for i in range(len(this_x)) :
            self.assertTrue( np.fabs( (i+0.5)*delr - this_x[i] )<1e-7, "the x-coordinates of the points in your histogram are not correct" )
