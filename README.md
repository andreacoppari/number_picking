# number_picking

Can picking a random number — *the De Paolis way* — converge to a fixed distribution?

---

## 📚 Table of Contents

- [The De Paolis Way](#the-de-paolis-way)
- [Is the Method Fair?](#is-the-method-fair)
- [Symmetry!](#symmetry)

---

## The De Paolis Way

Prof. De Paolis is a high school physics teacher who used to pick a "random" number by:

1. Opening a book to a random page  
2. Taking the page number  
3. Summing the digits of that number  
4. Using the resulting sum to select a student (ordered alphabetically) for an oral test

---

## Is the Method Fair?

**Realistically: no.**

As shown in the image below, assuming a book has an absurd number of pages (9,999,998), the maximum possible digit sum is 63. The resulting distribution of digit sums forms a bell-shaped curve — **symmetric** in this specific case. (More on that in the next section.)

![Distribution with 9,999,998 pages](/img/Figure_1.png)

Since we were only 18 students, the professor would map the result using modulo 18:

```python
student_index = digit_sum % 18
```

This wrapping creates bias. The mod operation skews the distribution in favor of students near the center of the list, **but only when using large enough numbers**.

### Comparison Example

| 9,999,998 Pages        | 400 Pages              |
| ---------------------- | ---------------------- |
| ![](/img/Figure_2.png) | ![](/img/Figure_3.png) |

The smaller the page range, the more uneven the distribution becomes.

---

## Symmetry!

Interestingly, for certain upper bounds, the digit sum distribution is nearly **perfectly symmetric**, but only **before** a new maximum digit sum is introduced.

The sequence of numbers that produce symmetric distributions can be described by:

![Symmetry sequence formula](/img/image.png)

Where:

* `Sₙ` is the n-th number in the sequence that keeps symmetry
* `floor(log₁₀(Sₙ₋₁ + 2))` is the number of digits of `Sₙ₋₁ + 2`

These numbers (e.g., 18, 28, ..., 998, 1998) act as **symmetry breakpoints**. As soon as the next digit sum appears (e.g. 64 for `9999999`), the distribution becomes slightly unbalanced.

---