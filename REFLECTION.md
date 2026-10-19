# Part B: Reflection

1. In Part A, I wrote 8 test functions. The current `kitchen.py` has 38 nonblank production lines, so the ratio is about 1 test per 4.75 lines. However, this ratio may not be very meaningful because tests and code lines are different things.

2. The mixed-unit addition test took the longest to pass. Even after storing the rates, the sum still returned the wrong amount. I needed to convert both quantities to the requested unit before adding them.

3. I used Fake It when `plus` returned `grams(500)` and `Converter.reduce` returned its source. This helped pass the first test but was only temporary. I used Triangulation by adding a test for 2 ounces to check that the conversion was correct. For `Quantity.times`, I used Obvious Implementation because multiplying the amount and keeping the same unit was straightforward.

4. Two items in the test list are already covered by existing tests, so their checkboxes should be updated. Next, I would test `(200 g + 1 oz) × 2`. I would remove the `__eq__` and `__hash__` item for now because it is not a necessary requirement for this system.

5. If I planned everything first, I might have thought of a reduction method, but probably not the exact role of `Quantity.reduce`. It came from the need to reduce both a quantity and a `Sum` in the same way.

6. Writing tests after the Part 0 code felt like checking what I had already made. Writing tests first in Part A helped me decide what the code should do. The mixed-unit tests also helped me decide how to handle conversion before addition.