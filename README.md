# number_picking

Can picking a random number — *the De Paolis way* — converge to a fixed distribution?


## 📚 Table of Contents

- [The De Paolis Way](#the-de-paolis-way)
- [Usage](#usage)
- [Is the Method Fair?](#is-the-method-fair)
- [Symmetry!](#symmetry)


## The De Paolis Way

Prof. De Paolis is a high school physics teacher who used to pick a "random" number by:

1. Opening a book to a random page  
2. Taking the page number  
3. Summing the digits of that number  
4. Using the resulting sum to select a student (ordered alphabetically) for an oral test

## Usage

Install packages:

```
pip install -r requirements.txt
```

and run `main.py`:

```
python main.py
```

## Is the Method Fair?

**Realistically: no.**

As shown in the image below, assuming a book has an absurd number of pages (9,999,998), the maximum possible digit sum is 62. The resulting distribution of digit sums forms a bell-shaped curve — **symmetric** in this specific case. (More on that in the next section.)

![Distribution with 9,999,998 pages](/img/Figure_1.png)

Since we were only 18 students, the professor would map the result using modulo 18:

```python
student_index = digit_sum % 18
```

This wrapping creates bias. **When there's no overflow** (i.e., digit sums aren't wrapped with a modulo), students in the middle of the list are more likely to be selected — the distribution is peaked around mid-range values.

Applying a modulo (e.g., % 18) helps flatten the distribution by spreading the bias more evenly across the list — **but this only works well when the range of numbers is large enough to populate the entire digit sum space uniformly**.

### Comparison Example

| 9,999,998 Pages        | 400 Pages              |
| ---------------------- | ---------------------- |
| ![](/img/Figure_2.png) | ![](/img/Figure_3.png) |

The smaller the page range, the more uneven the distribution becomes.


## Symmetry!

Interestingly, for certain upper bounds, the digit sum distribution becomes **perfectly symmetric** — but only **until a new maximum digit sum appears**. You can print a list of the first N elements by running `symmetric_numbers.py`

The numbers at which this symmetry holds form a special sequence, defined recursively as:

![Symmetry sequence formula](/img/image.png)

Where:

- `S_n` is the *n*-th number in the sequence that maintains symmetry
- The number of digits of `S_{n-1} + 2` is given by:
$$⌊log₁₀(Sₙ₋₁ + 2)⌋ + 1$$

- At each step, we increment the current value by:

  $$10^{\text{digits} - 1} = 10^{\left\lfloor \log_{10}(S_{n-1} + 2) \right\rfloor}$$

This leads to the known sequence:

```

18, 28, 38, ..., 98, 198, 298, ..., 998, 1998, ...

```

Each of these values represents a **symmetry breakpoint** — a point up to which the digit sum distribution remains balanced and bell-shaped.

Once the next possible digit sum is introduced (e.g., 63 when reaching `9999999`), the symmetry breaks, and the distribution begins to shift.

These breakpoints occur just before new digit sums become possible — making them a natural boundary in the growth of the digit sum space.

---
#### Hope you enjoyed, Andrea Coppari :)