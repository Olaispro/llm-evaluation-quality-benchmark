import unittest
from src.evalbench import summarize
class TestSummary(unittest.TestCase):
 def test_dimension_summary(self):
  r=summarize([{"accuracy":4,"relevance":5},{"accuracy":2,"relevance":3}]); self.assertEqual(r["n"],2); self.assertEqual(r["dimensions"]["accuracy"]["mean"],3); self.assertEqual(r["dimensions"]["accuracy"]["low_score_rate"],.5)
