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
    ],
    answers=[
        "1)  4x + 12 + 2x = 6x + 12",
        "2)  10y - 5 + 3y = 13y - 5",
        "3)  6a + 8 - a - 5 = 5a + 3",
        "4)  -3x + 18 + 2x = -x + 18",
        "5)  2x + 6 = 16,  2x = 10,  x = 5",
        "6)  8n - 4 + 3 = 19,  8n - 1 = 19,  8n = 20,  n = 5/2 = 2.5",
        "7)  3y + 15 - 2y = 20,  y + 15 = 20,  y = 5",
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
    ],
    answers=[
        "1)  2x + 7 = 19,  2x = 12,  x = 6",
        "2)  3y - 5 = 10,  3y = 15,  y = 5",
        "3)  3m + 1 = 16,  3m = 15,  m = 5",
        "4)  3n + 6 = n + 14,  2n = 8,  n = 4",
        "5)  4a - 4 = 12,  4a = 16,  a = 4",
        "6)  2x + 10 = 3x - 6,  10 + 6 = x,  x = 16",
        "7)  5w - 5 = 2w + 10,  3w = 15,  w = 5",
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
    ],
    answers=[
        "1)  x > 7",
        "2)  3y <= 12,  y <= 4",
        "3)  m < -4   (divided by -2, flipped sign)",
        "4)  4n >= 16,  n >= 4",
        "5)  -5a < -20,  a > 4   (divided by -5, flipped sign)",
        "6)  2x - 8 <= 6,  2x <= 14,  x <= 7",
        "7)  2x + 8 > 20,  2x > 12,  x > 6",
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
    ],
    answers=[
        "1)  slope m = 4,  y-intercept b = 1",
        "2)  slope m = -3,  y-intercept b = 5",
        "3)  m = (8 - 2)/(3 - 1) = 6/2 = 3",
        "4)  m = (1 - 7)/(5 - 2) = -6/3 = -2",
        "5)  y = -2x + 10   (subtract 2x from both sides)",
        "6)  -2y = -3x + 12,  y = (3/2)x - 6",
        "7)  y = -2x + 4;  when x = 3: y = -6 + 4 = -2",
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
    ],
    answers=[
        "1)  x^(5+3) = x^8",
        "2)  y^(8-2) = y^6",
        "3)  a^(3*4) = a^12",
        "4)  12x^(2+5) = 12x^7",
        "5)  2^(3*2) = 2^6 = 64",
        "6)  1 + 1/9 = 10/9  (or approximately 1.11)",
        "7)  3m^(7-3) = 3m^4",
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
    ],
    answers=[
        "1)  3x^2 + 2x + 5",
        "2)  5y^2 + 2y - 3y^2 + y - 6 = 2y^2 + 3y - 6",
        "3)  3x^3 + 12x^2 - 6x",
        "4)  Degree 3  (from the 7a^3 term)",
        "5)  6m^2 + 4m - 4",
        "6)  6x^2 + 10x - x^2 + x = 5x^2 + 11x",
        "7)  Area = (x + 3)(2x - 1) = 2x^2 - x + 6x - 3 = 2x^2 + 5x - 3",
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
