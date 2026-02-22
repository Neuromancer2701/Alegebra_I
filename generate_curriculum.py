#!/usr/bin/env python3
"""
Algebra I Curriculum Generator
Generates printable PDFs for 10 lessons + answer keys using fpdf2.
Uses Unicode math symbols for correct rendering without LaTeX.
"""

from fpdf import FPDF
import os

CURRICULUM_DIR = os.path.join(os.path.dirname(__file__), "curriculum")
ANSWERS_DIR = os.path.join(os.path.dirname(__file__), "answer_keys")
os.makedirs(CURRICULUM_DIR, exist_ok=True)
os.makedirs(ANSWERS_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Lesson Data
# ---------------------------------------------------------------------------
# Each lesson: title, intro, example_title, example_body, problems, answers
# problems is a list of strings; answers is a parallel list of strings.

LESSONS = []

# ── Lesson 1 ──────────────────────────────────────────────────────────────
LESSONS.append(dict(
    number=1,
    title="Variables and Algebraic Expressions",
    intro=(
        "In algebra, we use letters called variables to represent unknown numbers. "
        "An algebraic expression is a combination of numbers, variables, and operations "
        "(like +, -, *, /). For example, 3x + 5 means \"three times some number, plus five.\"\n\n"
        "To evaluate an expression, substitute the given value for the variable and compute."
    ),
    example_title="Example: Evaluate  2x + 7  when  x = 4",
    example_body=(
        "Step 1:  Replace x with 4\n"
        "            2(4) + 7\n\n"
        "Step 2:  Multiply first\n"
        "            8 + 7\n\n"
        "Step 3:  Add\n"
        "            = 15"
    ),
    problems=[
        "1)  Evaluate  3x + 2  when  x = 5.",
        "2)  Evaluate  4y - 9  when  y = 6.",
        "3)  Evaluate  x/2 + 10  when  x = 8.",  # using / for division
        "4)  Evaluate  5a - 2a + 7  when  a = 3.",
        "5)  Evaluate  2(n + 4)  when  n = 6.",
        "6)  Write an algebraic expression: \"seven more than twice a number.\"",
        "7)  Write an algebraic expression: \"a number decreased by four, then tripled.\"",
    ],
    answers=[
        "1)  3(5) + 2 = 15 + 2 = 17",
        "2)  4(6) - 9 = 24 - 9 = 15",
        "3)  8/2 + 10 = 4 + 10 = 14",
        "4)  5(3) - 2(3) + 7 = 15 - 6 + 7 = 16",
        "5)  2(6 + 4) = 2(10) = 20",
        "6)  2x + 7   (where x is the number)",
        "7)  3(x - 4)   (where x is the number)",
    ],
))

# ── Lesson 2 ──────────────────────────────────────────────────────────────
LESSONS.append(dict(
    number=2,
    title="Order of Operations (PEMDAS)",
    intro=(
        "When an expression has several operations, we follow a specific order:\n\n"
        "  P - Parentheses first\n"
        "  E - Exponents (powers)\n"
        "  M/D - Multiplication and Division (left to right)\n"
        "  A/S - Addition and Subtraction (left to right)\n\n"
        "This rule ensures everyone gets the same answer for the same expression."
    ),
    example_title="Example: Simplify  3 + 4 * (2^2 - 1)",
    example_body=(
        "Step 1:  Parentheses first -- evaluate the exponent inside\n"
        "            3 + 4 * (4 - 1)\n\n"
        "Step 2:  Finish parentheses\n"
        "            3 + 4 * 3\n\n"
        "Step 3:  Multiply before adding\n"
        "            3 + 12\n\n"
        "Step 4:  Add\n"
        "            = 15"
    ),
    problems=[
        "1)  Simplify:  5 + 3 * 2",
        "2)  Simplify:  (5 + 3) * 2",
        "3)  Simplify:  4^2 - 3 * 2 + 1",
        "4)  Simplify:  (10 - 4)^2 / 9",
        "5)  Simplify:  2 * (3 + 5) - 4^2",
        "6)  Simplify:  18 / (2 + 4) + 3^2",
        "7)  Simplify:  5 * 2^3 - (12 - 7)",
    ],
    answers=[
        "1)  5 + 6 = 11",
        "2)  8 * 2 = 16",
        "3)  16 - 6 + 1 = 11",
        "4)  6^2 / 9 = 36 / 9 = 4",
        "5)  2(8) - 16 = 16 - 16 = 0",
        "6)  18/6 + 9 = 3 + 9 = 12",
        "7)  5(8) - 5 = 40 - 5 = 35",
    ],
))

# ── Lesson 3 ──────────────────────────────────────────────────────────────
LESSONS.append(dict(
    number=3,
    title="Solving One-Step Equations",
    intro=(
        "An equation is a statement that two expressions are equal. "
        "To solve an equation, we find the value of the variable that makes it true.\n\n"
        "The key idea: whatever you do to one side, you must do to the other side.\n\n"
        "  - If a number is added, subtract it from both sides.\n"
        "  - If a number is subtracted, add it to both sides.\n"
        "  - If multiplied, divide both sides.\n"
        "  - If divided, multiply both sides."
    ),
    example_title="Example: Solve  x + 8 = 15",
    example_body=(
        "We need to isolate x. Since 8 is added to x, subtract 8 from both sides:\n\n"
        "    x + 8 - 8 = 15 - 8\n"
        "    x = 7\n\n"
        "Check: 7 + 8 = 15  [correct]"
    ),
    problems=[
        "1)  Solve:  x + 12 = 20",
        "2)  Solve:  y - 7 = 15",
        "3)  Solve:  3m = 27",
        "4)  Solve:  n / 4 = 6",
        "5)  Solve:  x - 15 = -3",
        "6)  Solve:  5p = -35",
        "7)  Solve:  w / 3 = -8",
    ],
    answers=[
        "1)  x = 20 - 12 = 8",
        "2)  y = 15 + 7 = 22",
        "3)  m = 27 / 3 = 9",
        "4)  n = 6 * 4 = 24",
        "5)  x = -3 + 15 = 12",
        "6)  p = -35 / 5 = -7",
        "7)  w = -8 * 3 = -24",
    ],
))

# ── Lesson 4 ──────────────────────────────────────────────────────────────
LESSONS.append(dict(
    number=4,
    title="Solving Two-Step Equations",
    intro=(
        "Many equations require two steps to solve. The general strategy:\n\n"
        "  1. Undo addition or subtraction first.\n"
        "  2. Then undo multiplication or division.\n\n"
        "Think of it as \"unwrapping\" the variable -- reverse the order of operations."
    ),
    example_title="Example: Solve  2x + 5 = 17",
    example_body=(
        "Step 1:  Subtract 5 from both sides\n"
        "            2x + 5 - 5 = 17 - 5\n"
        "            2x = 12\n\n"
        "Step 2:  Divide both sides by 2\n"
        "            x = 12 / 2\n"
        "            x = 6\n\n"
        "Check: 2(6) + 5 = 12 + 5 = 17  [correct]"
    ),
    problems=[
        "1)  Solve:  3x + 4 = 19",
        "2)  Solve:  5y - 8 = 22",
        "3)  Solve:  x/3 + 7 = 12",
        "4)  Solve:  4n - 10 = -2",
        "5)  Solve:  -2w + 9 = 1",
        "6)  Solve:  m/5 - 3 = 4",
        "7)  Solve:  6a + 11 = -1",
    ],
    answers=[
        "1)  3x = 15,  x = 5",
        "2)  5y = 30,  y = 6",
        "3)  x/3 = 5,  x = 15",
        "4)  4n = 8,  n = 2",
        "5)  -2w = -8,  w = 4",
        "6)  m/5 = 7,  m = 35",
        "7)  6a = -12,  a = -2",
    ],
))

# ── Lesson 5 ──────────────────────────────────────────────────────────────
LESSONS.append(dict(
    number=5,
    title="The Distributive Property and Combining Like Terms",
    intro=(
        "The Distributive Property lets us remove parentheses:\n\n"
        "    a(b + c) = ab + ac\n\n"
        "Like terms are terms with the same variable raised to the same power. "
        "We simplify expressions by combining like terms:\n\n"
        "    3x + 5x = 8x        (add the coefficients)\n"
        "    7y - 2y = 5y"
    ),
    example_title="Example: Simplify  3(2x + 4) - 5x",
    example_body=(
        "Step 1:  Distribute the 3\n"
        "            6x + 12 - 5x\n\n"
        "Step 2:  Combine like terms (6x and -5x)\n"
        "            x + 12"
    ),
    problems=[
        "1)  Simplify:  4(x + 3) + 2x",
        "2)  Simplify:  5(2y - 1) + 3y",
        "3)  Simplify:  2(3a + 4) - (a + 5)",
        "4)  Simplify:  -3(x - 6) + 2x",
        "5)  Solve:  2(x + 3) = 16",
        "6)  Solve:  4(2n - 1) + 3 = 19",
        "7)  Solve:  3(y + 5) - 2y = 20",
        "8)  Simplify:  6(x - 2) + 3(x + 1)",
        "9)  Simplify:  -(3x - 4) + 5x",
        "10)  Simplify:  4(2m - 3) - 2(m + 1)",
        "11)  Simplify:  3(a + 2b) - 2(a - b)",
        "12)  Solve:  5(x - 4) = 0",
        "13)  Solve:  3(2x + 1) - 5 = 22",
        "14)  Solve:  -2(x - 4) = 10",
        "15)  Solve:  4(3x + 2) = 2(5x + 8)",
        "16)  Simplify:  7a - 3(2a - 1) + 5",
        "17)  Simplify:  2(4x - 3) - (3x + 1) + 8",
        "18)  Solve:  6(x + 2) - 3(x - 1) = 27",
        "19)  A rectangle has length (3x + 4) and width 2.\n"
        "     Write and simplify an expression for its perimeter.",
        "20)  Simplify:  5(2x - 1) - 3(x + 2) + 4(x - 3)",
    ],
    answers=[
        "1)  4x + 12 + 2x = 6x + 12",
        "2)  10y - 5 + 3y = 13y - 5",
        "3)  6a + 8 - a - 5 = 5a + 3",
        "4)  -3x + 18 + 2x = -x + 18",
        "5)  2x + 6 = 16,  2x = 10,  x = 5",
        "6)  8n - 4 + 3 = 19,  8n - 1 = 19,  8n = 20,  n = 5/2 = 2.5",
        "7)  3y + 15 - 2y = 20,  y + 15 = 20,  y = 5",
        "8)  6x - 12 + 3x + 3 = 9x - 9",
        "9)  -3x + 4 + 5x = 2x + 4",
        "10)  8m - 12 - 2m - 2 = 6m - 14",
        "11)  3a + 6b - 2a + 2b = a + 8b",
        "12)  5x - 20 = 0,  5x = 20,  x = 4",
        "13)  6x + 3 - 5 = 22,  6x - 2 = 22,  6x = 24,  x = 4",
        "14)  -2x + 8 = 10,  -2x = 2,  x = -1",
        "15)  12x + 8 = 10x + 16,  2x = 8,  x = 4",
        "16)  7a - 6a + 3 + 5 = a + 8",
        "17)  8x - 6 - 3x - 1 + 8 = 5x + 1",
        "18)  6x + 12 - 3x + 3 = 27,  3x + 15 = 27,  3x = 12,  x = 4",
        "19)  P = 2(3x + 4) + 2(2) = 6x + 8 + 4 = 6x + 12",
        "20)  10x - 5 - 3x - 6 + 4x - 12 = 11x - 23",
    ],
))

# ── Lesson 6 ──────────────────────────────────────────────────────────────
LESSONS.append(dict(
    number=6,
    title="Solving Equations with Variables on Both Sides",
    intro=(
        "Sometimes the variable appears on both sides of the equation. Strategy:\n\n"
        "  1. Simplify each side (distribute and combine like terms if needed).\n"
        "  2. Move all variable terms to one side by adding or subtracting.\n"
        "  3. Move all constant terms to the other side.\n"
        "  4. Solve the resulting one- or two-step equation."
    ),
    example_title="Example: Solve  5x + 3 = 2x + 18",
    example_body=(
        "Step 1:  Subtract 2x from both sides\n"
        "            3x + 3 = 18\n\n"
        "Step 2:  Subtract 3 from both sides\n"
        "            3x = 15\n\n"
        "Step 3:  Divide by 3\n"
        "            x = 5\n\n"
        "Check: 5(5) + 3 = 28  and  2(5) + 18 = 28  [correct]"
    ),
    problems=[
        "1)  Solve:  4x + 7 = 2x + 19",
        "2)  Solve:  6y - 5 = 3y + 10",
        "3)  Solve:  8m + 1 = 5m + 16",
        "4)  Solve:  3(n + 2) = n + 14",
        "5)  Solve:  7a - 4 = 3a + 12",
        "6)  Solve:  2(x + 5) = 3(x - 2)",
        "7)  Solve:  5(w - 1) = 2(w + 5)",
        "8)  Solve:  9x - 3 = 6x + 9",
        "9)  Solve:  4(y + 1) = 2y + 14",
        "10)  Solve:  3m + 8 = m + 20",
        "11)  Solve:  6(n - 2) = 2(n + 6)",
        "12)  Solve:  10x - 7 = 4x + 11",
        "13)  Solve:  3(2a + 1) = 5a + 7",
        "14)  Solve:  8p - 5 = 3p + 20",
        "15)  Solve:  2(4x - 3) = 3(2x + 4)",
        "16)  Solve:  7(y + 2) = 4(y + 5)",
        "17)  Solve and identify the type of solution:  5x + 3 = 5x + 7",
        "18)  Solve and identify the type of solution:  4(2x - 1) = 2(4x - 2)",
        "19)  Alice has (3x + 10) dollars; Bob has (5x - 2) dollars.\n"
        "     Find x if they have equal amounts.",
        "20)  A plumber charges $40 + $25/hr; an electrician charges $10 + $35/hr.\n"
        "     After how many hours h will their total charges be equal?",
    ],
    answers=[
        "1)  2x + 7 = 19,  2x = 12,  x = 6",
        "2)  3y - 5 = 10,  3y = 15,  y = 5",
        "3)  3m + 1 = 16,  3m = 15,  m = 5",
        "4)  3n + 6 = n + 14,  2n = 8,  n = 4",
        "5)  4a - 4 = 12,  4a = 16,  a = 4",
        "6)  2x + 10 = 3x - 6,  10 + 6 = x,  x = 16",
        "7)  5w - 5 = 2w + 10,  3w = 15,  w = 5",
        "8)  3x - 3 = 9,  3x = 12,  x = 4",
        "9)  4y + 4 = 2y + 14,  2y = 10,  y = 5",
        "10)  2m = 12,  m = 6",
        "11)  6n - 12 = 2n + 12,  4n = 24,  n = 6",
        "12)  6x - 7 = 11,  6x = 18,  x = 3",
        "13)  6a + 3 = 5a + 7,  a = 4",
        "14)  5p - 5 = 20,  5p = 25,  p = 5",
        "15)  8x - 6 = 6x + 12,  2x = 18,  x = 9",
        "16)  7y + 14 = 4y + 20,  3y = 6,  y = 2",
        "17)  Variables cancel: 3 = 7  ->  No solution",
        "18)  8x - 4 = 8x - 4  ->  Always true; infinitely many solutions",
        "19)  3x + 10 = 5x - 2,  12 = 2x,  x = 6",
        "20)  40 + 25h = 10 + 35h,  30 = 10h,  h = 3 hours",
    ],
))

# ── Lesson 7 ──────────────────────────────────────────────────────────────
LESSONS.append(dict(
    number=7,
    title="Inequalities",
    intro=(
        "An inequality compares two expressions using:\n\n"
        "    <  less than          >  greater than\n"
        "    <=  less than or equal to    >=  greater than or equal to\n\n"
        "Solving inequalities works just like solving equations, with one important rule:\n\n"
        "    *** When you multiply or divide by a NEGATIVE number,\n"
        "        FLIP the inequality sign! ***\n\n"
        "Solutions are ranges of numbers, not single values."
    ),
    example_title="Example: Solve  -3x + 4 > 13",
    example_body=(
        "Step 1:  Subtract 4 from both sides\n"
        "            -3x > 9\n\n"
        "Step 2:  Divide by -3 (FLIP the sign!)\n"
        "            x < -3\n\n"
        "The solution is all numbers less than -3."
    ),
    problems=[
        "1)  Solve:  x + 5 > 12",
        "2)  Solve:  3y - 2 <= 10",
        "3)  Solve:  -2m > 8",
        "4)  Solve:  4n + 7 >= 23",
        "5)  Solve:  -5a + 3 < -17",
        "6)  Solve:  2(x - 4) <= 6",
        "7)  Solve:  3x + 8 > x + 20",
        "8)  Solve:  x - 9 < -3",
        "9)  Solve:  -4y >= 24",
        "10)  Solve:  6n + 5 > 35",
        "11)  Solve:  2(3x - 1) <= 16",
        "12)  Solve:  -3(m + 4) > 6",
        "13)  Solve:  5a - 7 < 3a + 9",
        "14)  Solve:  4x + 11 >= 2x + 23",
        "15)  Solve:  -2(3y - 5) < 14",
        "16)  Solve:  3x - 8 <= 5x + 4",
        "17)  Solve:  7 - 4n > 19",
        "18)  Solve:  3(2x + 1) >= 5x + 8",
        "19)  A student needs at least 75 total points on four quizzes.\n"
        "     Her first three scores are 12, 18, and 20. Write and solve\n"
        "     an inequality to find the minimum score q needed on quiz 4.",
        "20)  Solve:  -2x + 9 > 4x - 9",
    ],
    answers=[
        "1)  x > 7",
        "2)  3y <= 12,  y <= 4",
        "3)  m < -4   (divided by -2, flipped sign)",
        "4)  4n >= 16,  n >= 4",
        "5)  -5a < -20,  a > 4   (divided by -5, flipped sign)",
        "6)  2x - 8 <= 6,  2x <= 14,  x <= 7",
        "7)  2x + 8 > 20,  2x > 12,  x > 6",
        "8)  x < 6",
        "9)  y <= -6   (divided by -4, flipped sign)",
        "10)  6n > 30,  n > 5",
        "11)  6x - 2 <= 16,  6x <= 18,  x <= 3",
        "12)  -3m - 12 > 6,  -3m > 18,  m < -6   (flipped sign)",
        "13)  2a - 7 < 9,  2a < 16,  a < 8",
        "14)  2x + 11 >= 23,  2x >= 12,  x >= 6",
        "15)  -6y + 10 < 14,  -6y < 4,  y > -2/3   (flipped sign)",
        "16)  -8 <= 2x + 4,  -12 <= 2x,  x >= -6",
        "17)  -4n > 12,  n < -3   (divided by -4, flipped sign)",
        "18)  6x + 3 >= 5x + 8,  x >= 5",
        "19)  12 + 18 + 20 + q >= 75,  50 + q >= 75,  q >= 25",
        "20)  -2x - 4x > -9 - 9,  -6x > -18,  x < 3   (flipped sign)",
    ],
))

# ── Lesson 8 ──────────────────────────────────────────────────────────────
LESSONS.append(dict(
    number=8,
    title="Graphing Linear Equations (Slope-Intercept Form)",
    intro=(
        "A linear equation graphs as a straight line. The most useful form is\n"
        "slope-intercept form:\n\n"
        "    y = mx + b\n\n"
        "where:\n"
        "    m = slope  (rise over run -- how steep the line is)\n"
        "    b = y-intercept  (where the line crosses the y-axis)\n\n"
        "Slope formula between two points (x1, y1) and (x2, y2):\n\n"
        "    m = (y2 - y1) / (x2 - x1)"
    ),
    example_title="Example: Graph  y = 2x - 3",
    example_body=(
        "Identify:  m = 2 (slope),  b = -3 (y-intercept)\n\n"
        "Step 1:  Plot the y-intercept at (0, -3)\n\n"
        "Step 2:  From that point, use the slope: rise 2, run 1\n"
        "            Move up 2 and right 1 to reach (1, -1)\n\n"
        "Step 3:  Plot that point and draw a line through both points.\n\n"
        "Check another point: x = 2 gives y = 2(2) - 3 = 1, so (2, 1) should be on the line."
    ),
    problems=[
        "1)  Identify the slope and y-intercept of  y = 4x + 1.",
        "2)  Identify the slope and y-intercept of  y = -3x + 5.",
        "3)  Find the slope between the points (1, 2) and (3, 8).",
        "4)  Find the slope between the points (2, 7) and (5, 1).",
        "5)  Rewrite in slope-intercept form:  2x + y = 10.",
        "6)  Rewrite in slope-intercept form:  3x - 2y = 12.",
        "7)  A line passes through (0, 4) with slope -2. Write its equation\n"
        "    and find the value of y when x = 3.",
        "8)  Identify the slope and y-intercept of  y = (1/2)x - 4.",
        "9)  Identify the slope and y-intercept of  y = -x + 7.",
        "10)  Find the slope between the points (-2, 3) and (4, 9).",
        "11)  Find the slope between the points (0, 5) and (6, 5).\n"
        "     What kind of line does this slope describe?",
        "12)  Rewrite in slope-intercept form:  4x - y = 8.",
        "13)  Rewrite in slope-intercept form:  x + 3y = 15.",
        "14)  Write the equation of a line with slope 3 and y-intercept -5.",
        "15)  Write the equation of a line with slope 0 and y-intercept 2.",
        "16)  A line passes through (0, -2) and (4, 6).\n"
        "     Find the slope and write its equation.",
        "17)  Do y = 2x + 1 and y = 2x - 3 intersect? Explain.",
        "18)  Find the slope between (-3, 4) and (1, -4).",
        "19)  Rewrite in slope-intercept form:  5x - 3y = 15.\n"
        "     Then find y when x = 6.",
        "20)  The cost to rent a bicycle is C = 3h + 8 dollars (h = hours).\n"
        "     Identify the slope and y-intercept and explain what each means.",
    ],
    answers=[
        "1)  slope m = 4,  y-intercept b = 1",
        "2)  slope m = -3,  y-intercept b = 5",
        "3)  m = (8 - 2)/(3 - 1) = 6/2 = 3",
        "4)  m = (1 - 7)/(5 - 2) = -6/3 = -2",
        "5)  y = -2x + 10   (subtract 2x from both sides)",
        "6)  -2y = -3x + 12,  y = (3/2)x - 6",
        "7)  y = -2x + 4;  when x = 3: y = -6 + 4 = -2",
        "8)  slope m = 1/2,  y-intercept b = -4",
        "9)  slope m = -1,  y-intercept b = 7",
        "10)  m = (9 - 3)/(4 - (-2)) = 6/6 = 1",
        "11)  m = (5 - 5)/(6 - 0) = 0/6 = 0  ->  horizontal line",
        "12)  -y = -4x + 8,  y = 4x - 8",
        "13)  3y = -x + 15,  y = (-1/3)x + 5",
        "14)  y = 3x - 5",
        "15)  y = 2   (horizontal line)",
        "16)  m = (6 - (-2))/(4 - 0) = 8/4 = 2;  y = 2x - 2",
        "17)  No; same slope (m = 2), different y-intercepts -> parallel lines, never intersect",
        "18)  m = (-4 - 4)/(1 - (-3)) = -8/4 = -2",
        "19)  -3y = -5x + 15,  y = (5/3)x - 5;  when x = 6: y = 10 - 5 = 5",
        "20)  slope = 3 (cost rises $3 per hour); y-intercept = 8 (base fee of $8)",
    ],
))

# ── Lesson 9 ──────────────────────────────────────────────────────────────
LESSONS.append(dict(
    number=9,
    title="Exponent Rules",
    intro=(
        "An exponent tells you how many times to multiply a base by itself:\n\n"
        "    x^3 = x * x * x\n\n"
        "Key exponent rules:\n\n"
        "    Product Rule:    x^a * x^b  =  x^(a+b)\n"
        "    Quotient Rule:   x^a / x^b  =  x^(a-b)\n"
        "    Power Rule:      (x^a)^b    =  x^(a*b)\n"
        "    Zero Exponent:   x^0 = 1    (when x is not 0)\n"
        "    Negative Exp:    x^(-n) = 1 / x^n"
    ),
    example_title="Example: Simplify  (2x^3)(5x^4)",
    example_body=(
        "Step 1:  Multiply the coefficients: 2 * 5 = 10\n\n"
        "Step 2:  Apply the product rule to x: x^3 * x^4 = x^(3+4) = x^7\n\n"
        "Result:  10x^7"
    ),
    problems=[
        "1)  Simplify:  x^5 * x^3",
        "2)  Simplify:  y^8 / y^2",
        "3)  Simplify:  (a^3)^4",
        "4)  Simplify:  (3x^2)(4x^5)",
        "5)  Simplify:  (2^3)^2",
        "6)  Evaluate:  5^0 + 3^(-2)",
        "7)  Simplify:  (6m^7) / (2m^3)",
        "8)  Simplify:  (x^2)^3 * x^4",
        "9)  Simplify:  (2a^4)(3a^2) / (6a^3)",
        "10)  Evaluate:  4^(-1) + 2^(-2)",
        "11)  Simplify:  (4x^3 y^2)(2x y^4)",
        "12)  Simplify:  (3m^2)^3",
        "13)  Simplify:  15x^6 y^4 / (5x^2 y)",
        "14)  Evaluate:  (2^3 * 2^2) / 2^4",
        "15)  Simplify:  (x^4 / x^2)^3",
        "16)  Simplify:  (2x^2)^3 * (3x)^2",
        "17)  Simplify:  (5x^0 y^3)(4x^2 y^(-1))",
        "18)  Write 10^(-4) as a decimal.",
        "19)  Simplify:  (a^2 b^3)^2 / (a^3 b)",
        "20)  A bacterium doubles every hour. Starting from 1 bacterium,\n"
        "     write an expression for the count after t hours as a power of 2.\n"
        "     Then evaluate it for t = 5.",
    ],
    answers=[
        "1)  x^(5+3) = x^8",
        "2)  y^(8-2) = y^6",
        "3)  a^(3*4) = a^12",
        "4)  12x^(2+5) = 12x^7",
        "5)  2^(3*2) = 2^6 = 64",
        "6)  1 + 1/9 = 10/9  (or approximately 1.11)",
        "7)  3m^(7-3) = 3m^4",
        "8)  x^6 * x^4 = x^10",
        "9)  6a^6 / (6a^3) = a^3",
        "10)  1/4 + 1/4 = 2/4 = 1/2",
        "11)  8x^4 y^6",
        "12)  27m^6",
        "13)  3x^4 y^3",
        "14)  2^(3+2-4) = 2^1 = 2",
        "15)  (x^2)^3 = x^6",
        "16)  8x^6 * 9x^2 = 72x^8",
        "17)  5(1)y^3 * 4x^2 y^(-1) = 20x^2 y^2",
        "18)  10^(-4) = 0.0001",
        "19)  a^4 b^6 / (a^3 b) = a b^5",
        "20)  Count = 2^t;  at t = 5: 2^5 = 32 bacteria",
    ],
))

# ── Lesson 10 ─────────────────────────────────────────────────────────────
LESSONS.append(dict(
    number=10,
    title="Introduction to Polynomials",
    intro=(
        "A polynomial is an expression with one or more terms, where each term is a\n"
        "number times a variable raised to a whole-number exponent.\n\n"
        "Examples:\n"
        "    3x^2 + 5x - 7     (a trinomial -- 3 terms)\n"
        "    4y - 1             (a binomial -- 2 terms)\n"
        "    6x^3               (a monomial -- 1 term)\n\n"
        "The degree of a polynomial is the highest exponent.\n\n"
        "To add or subtract polynomials, combine like terms.\n"
        "To multiply a monomial by a polynomial, use the distributive property."
    ),
    example_title="Example: Add  (3x^2 + 2x - 5)  +  (x^2 - 4x + 8)",
    example_body=(
        "Group like terms:\n\n"
        "    x^2 terms:  3x^2 + x^2  = 4x^2\n"
        "    x terms:    2x + (-4x)  = -2x\n"
        "    constants:  -5 + 8       = 3\n\n"
        "Result:  4x^2 - 2x + 3"
    ),
    problems=[
        "1)  Add:  (2x^2 + 3x + 1) + (x^2 - x + 4)",
        "2)  Subtract:  (5y^2 + 2y) - (3y^2 - y + 6)",
        "3)  Multiply:  3x(x^2 + 4x - 2)",
        "4)  What is the degree of  7a^3 - 2a^2 + a - 9 ?",
        "5)  Simplify:  (4m^2 - m + 3) + (2m^2 + 5m - 7)",
        "6)  Simplify:  2x(3x + 5) - x(x - 1)",
        "7)  A rectangle has length (x + 3) and width (2x - 1).\n"
        "    Write an expression for its area and expand it.",
        "8)  Add:  (x^3 - 2x + 5) + (3x^3 + x^2 - 4)",
        "9)  Subtract:  (6a^2 - 3a + 8) - (2a^2 + 5a - 1)",
        "10)  What is the degree of  4x^5 - 3x^2 + 7 ?",
        "11)  How many terms does  3x^4 - x^2 + 5x - 2  have?\n"
        "     What type of polynomial is it?",
        "12)  Multiply:  -4y(2y^2 - 3y + 1)",
        "13)  Multiply:  2a^2(a^3 - 5a + 3)",
        "14)  Simplify:  (3x^2 - x + 4) - (x^2 - 3x - 2)",
        "15)  Simplify:  3(x^2 + 2x - 1) + 2(x^2 - x + 4)",
        "16)  Evaluate  2x^2 - 3x + 1  when  x = 4.",
        "17)  A square has side length (x + 2).\n"
        "     Write and expand an expression for its area.",
        "18)  Simplify:  (5y^3 + 2y^2 - y) + (y^3 - 4y^2 + 3y + 6)\n"
        "                - (2y^3 - y + 1)",
        "19)  Is  3x^(-2) + 5  a polynomial? Explain why or why not.",
        "20)  A ball's height in feet is  h = -16t^2 + 48t + 5,\n"
        "     where t is time in seconds.\n"
        "     Find h when t = 1 and when t = 2.",
    ],
    answers=[
        "1)  3x^2 + 2x + 5",
        "2)  5y^2 + 2y - 3y^2 + y - 6 = 2y^2 + 3y - 6",
        "3)  3x^3 + 12x^2 - 6x",
        "4)  Degree 3  (from the 7a^3 term)",
        "5)  6m^2 + 4m - 4",
        "6)  6x^2 + 10x - x^2 + x = 5x^2 + 11x",
        "7)  Area = (x + 3)(2x - 1) = 2x^2 - x + 6x - 3 = 2x^2 + 5x - 3",
        "8)  4x^3 + x^2 - 2x + 1",
        "9)  4a^2 - 8a + 9",
        "10)  Degree 5  (from the 4x^5 term)",
        "11)  4 terms; it is a polynomial (4-term polynomial)",
        "12)  -8y^3 + 12y^2 - 4y",
        "13)  2a^5 - 10a^3 + 6a^2",
        "14)  3x^2 - x + 4 - x^2 + 3x + 2 = 2x^2 + 2x + 6",
        "15)  3x^2 + 6x - 3 + 2x^2 - 2x + 8 = 5x^2 + 4x + 5",
        "16)  2(16) - 3(4) + 1 = 32 - 12 + 1 = 21",
        "17)  Area = (x + 2)^2 = x^2 + 4x + 4",
        "18)  4y^3 - 2y^2 + 3y + 5",
        "19)  No; polynomials cannot have negative exponents.",
        "20)  t = 1: h = -16 + 48 + 5 = 37 ft;  t = 2: h = -64 + 96 + 5 = 37 ft",
    ],
))


# ---------------------------------------------------------------------------
# PDF Builder
# ---------------------------------------------------------------------------

class AlgebraPDF(FPDF):
    def __init__(self, is_answer_key=False):
        super().__init__()
        self.is_answer_key = is_answer_key
        self.set_auto_page_break(auto=True, margin=25)

    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(120, 120, 120)
        label = "ANSWER KEY" if self.is_answer_key else "STUDENT WORKSHEET"
        self.cell(0, 8, f"Algebra I  |  {label}", align="R", new_x="LMARGIN", new_y="NEXT")
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-20)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def lesson_title(self, number, title):
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(30, 60, 120)
        self.cell(0, 14, f"Lesson {number}", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(40, 40, 40)
        self.cell(0, 12, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def section_heading(self, text):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(30, 60, 120)
        self.cell(0, 10, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body_text(self, text):
        self.set_font("Courier", "", 11)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 6.5, text)
        self.ln(2)

    def problem_text(self, text):
        self.set_font("Courier", "", 11)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 7, text)
        self.ln(3)

    def work_space(self, lines=4):
        """Add blank lined space for student work."""
        self.set_draw_color(200, 200, 200)
        x_start = self.get_x() + 5
        x_end = 195
        for _ in range(lines):
            y = self.get_y()
            if y > 270:
                self.add_page()
                y = self.get_y()
            self.line(x_start, y, x_end, y)
            self.ln(8)
        self.ln(2)

    def divider(self):
        self.set_draw_color(180, 180, 180)
        y = self.get_y()
        self.line(10, y, 200, y)
        self.ln(6)


def build_lesson_pdf(lesson, is_answer_key=False):
    pdf = AlgebraPDF(is_answer_key=is_answer_key)
    pdf.add_page()

    # Title
    pdf.lesson_title(lesson["number"], lesson["title"])

    if not is_answer_key:
        # Lesson intro
        pdf.section_heading("Lesson")
        pdf.body_text(lesson["intro"])
        pdf.ln(2)

        # Worked example
        pdf.section_heading(lesson["example_title"])
        pdf.body_text(lesson["example_body"])
        pdf.divider()

        # Practice problems
        pdf.section_heading("Practice Problems")
        pdf.ln(2)
        items = lesson["problems"]
    else:
        pdf.section_heading("Answers")
        pdf.ln(2)
        items = lesson["answers"]

    for item in items:
        pdf.problem_text(item)
        if not is_answer_key:
            pdf.work_space(3)

    return pdf


def main():
    print("Generating Algebra I Curriculum PDFs...")
    for lesson in LESSONS:
        num = lesson["number"]
        tag = f"{num:02d}"

        # Student worksheet
        pdf = build_lesson_pdf(lesson, is_answer_key=False)
        path = os.path.join(CURRICULUM_DIR, f"Lesson_{tag}_{lesson['title'].replace(' ', '_')}.pdf")
        pdf.output(path)
        print(f"  ✓  {path}")

        # Answer key
        pdf = build_lesson_pdf(lesson, is_answer_key=True)
        path = os.path.join(ANSWERS_DIR, f"Lesson_{tag}_Answers.pdf")
        pdf.output(path)
        print(f"  ✓  {path}")

    print("\nDone! Files are in:")
    print(f"  Curriculum:   {CURRICULUM_DIR}/")
    print(f"  Answer Keys:  {ANSWERS_DIR}/")


if __name__ == "__main__":
    main()
