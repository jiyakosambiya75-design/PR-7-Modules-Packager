# 🌟 Multi-Utility Toolkit 🧰

### Your Friendly Python Companion for Everyday Utility Tasks 🐍✨

```{=html}
<p align="center">
```
`<strong>`{=html}📅 Time • 🧮 Mathematics • 🎲 Random Tools • 🆔 UUIDs •
📁 Files • 🔍 Module Explorer`</strong>`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## 👋 Welcome!

Welcome to **Multi-Utility Toolkit**, a beginner-friendly Python project
that brings several useful utilities together in one menu-driven
application.

Instead of running many small scripts separately, you can launch one
program, choose an option from the main menu, and explore the available
tools. The project is designed to demonstrate Python modules, reusable
functions, imports, package organization, conditional logic, loops, user
input, and simple error handling.

> 💡 **Project goal:** learn how small, focused Python modules can work
> together as one application.

Whether you are practising Python basics, preparing a
modular-programming assignment, or experimenting with your own
utilities, this toolkit provides a starting point that you can expand
over time.

------------------------------------------------------------------------

## ✨ What Is Inside?

  ------------------------------------------------------------------------
  Feature                                      Emoji What it is for
  --------------------- ---------------------------- ---------------------
  Date and time                                   📅 Work with
  operations                                         date/time-related
                                                     utilities and timing
                                                     features available in
                                                     the project.

  Mathematical                                    🧮 Perform supported
  operations                                         calculations through
                                                     a dedicated menu.

  Random data                                     🎲 Generate random
  generation                                         values and use random
                                                     utilities implemented
                                                     in the project.

  Unique identifiers                              🆔 Create UUID-based
                                                     identifiers.

  File operations                                 📁 Explore the custom
                                                     file-operations
                                                     module.

  Module explorer                                 🔍 Inspect public
                                                     attributes and
                                                     functions exposed by
                                                     an importable Python
                                                     module.

  Custom mathematical                             🌡️ Use project-defined
  utilities                                          conversion and
                                                     calculation helpers,
                                                     if the module is
                                                     configured.
  ------------------------------------------------------------------------

⚠️ **Note:** The exact operations available depend on the functions
currently implemented in your local files. This README describes the
toolkit structure and intended usage; keep the feature list aligned with
your final code.

------------------------------------------------------------------------

## 🎯 Why This Project?

Python becomes easier to maintain when related functionality is divided
into modules. A single, very long script can be difficult to navigate.
By separating features into files, each module can focus on a specific
responsibility.

This project demonstrates several important ideas:

-   🧩 **Modularity:** split a larger program into smaller files.
-   📦 **Packages:** organize related modules inside a folder such as
    `Data/`.
-   🔗 **Imports:** reuse functions from one module in another.
-   🔁 **Loops:** keep a menu running until the user chooses to exit.
-   🚦 **Conditional logic:** route a menu choice to the correct
    operation.
-   ⌨️ **User input:** collect choices and values interactively.
-   🧰 **Reusable functions:** define an operation once and call it when
    needed.
-   🔎 **Introspection:** use `dir()` to explore a module's available
    names.
-   🛡️ **Basic validation:** check inputs before carrying out selected
    calculations.

------------------------------------------------------------------------

## 🧰 Requirements

Before running the toolkit, make sure you have:

-   🐍 **Python 3** installed.
-   💻 A terminal, command prompt, or an editor such as Visual Studio
    Code.
-   📂 The project files saved together in the expected folder
    structure.
-   🧠 Basic familiarity with running Python scripts and entering values
    in a terminal.

Most of the described functionality uses Python's standard library, so
external packages may not be required. If your implementation uses any
third-party package, list it in `requirements.txt` and install it
separately.

### Check your Python installation

Open a terminal and run one of these commands:

``` bash
python --version
```

If your system uses the `python3` command, try:

``` bash
python3 --version
```

You should see a Python 3 version number. If neither command works,
install Python and ensure it is available from your terminal.

------------------------------------------------------------------------

## 📂 Suggested Project Structure

A clean structure helps Python locate modules and makes the project
easier to understand.

``` text
Multi-Utility-Toolkit/
├── main_menu.py
├── README.md
├── requirements.txt
└── Data/
    ├── __init__.py
    ├── Date_time.py
    ├── maths.py
    ├── randomly.py
    ├── generate_uuid.py
    ├── file_operators.py
    ├── module_attributes.py
    └── math_util.py
```

📝 **Important:** This is a suggested structure based on the files
discussed during development. If your files are currently arranged
differently, either move them into this structure or adjust the imports
and run commands to match your actual layout.

### What do these files do?

-   `main_menu.py` --- displays the main menu and dispatches the
    selected operation.
-   `Data/__init__.py` --- marks `Data` as a regular Python package and
    allows package imports.
-   `Data/Date_time.py` --- contains date/time-related operations and
    its submenu.
-   `Data/maths.py` --- contains the mathematical operations menu.
-   `Data/randomly.py` --- contains random-data utilities and related
    options.
-   `Data/generate_uuid.py` --- creates UUIDs.
-   `Data/file_operators.py` --- contains file-related operations.
-   `Data/module_attributes.py` --- explores names exposed by an
    importable module.
-   `Data/math_util.py` --- contains custom mathematical helper
    functions, if you have saved it under this name.

⚠️ Python module names are case-sensitive on many systems. For example,
`Date_time.py` and `date_time.py` may be treated as different filenames.
Ensure that imports match the filenames exactly.

------------------------------------------------------------------------

## 🚀 Getting Started

### 1. Open the project folder

Open the folder containing `main_menu.py` in your editor. In Visual
Studio Code, choose **File → Open Folder** and select the project
directory.

### 2. Check the file structure

Confirm that the main script and the `Data` folder are where you expect
them to be. Check that the package contains `__init__.py`.

### 3. Open a terminal

In Visual Studio Code, use **Terminal → New Terminal**. Make sure the
terminal's current directory is the project root---the folder that
contains `main_menu.py` or the `Data` folder, depending on your
arrangement.

### 4. Run the application

If `main_menu.py` is in the project root and the imports match that
structure, run:

``` bash
python main_menu.py
```

If `main_menu.py` is inside the `Data` folder, the correct command and
imports may be different. For a package-based layout, it is usually
cleaner to keep the launcher in the project root.

### 5. Choose an option

When the menu appears, enter the number for the feature you want to use
and press **Enter**. Follow the prompts and enter the requested values.

### 6. Return to the main menu

Use the relevant **Back to Main Menu** option in a submenu. A submenu
should return from its function, allowing the main menu's loop to
display again.

### 7. Exit safely

Choose the exit option displayed by your current main menu. The
application should finish without leaving a loop running.

------------------------------------------------------------------------

## 🧭 Main Menu Guide

The main menu brings the toolkit's features together. Your current
version is expected to show options similar to these:

1.  📅 Date and Time Operations
2.  🧮 Mathematical Operations
3.  🎲 Random Data Generation
4.  🆔 Generate Unique Identifiers (UUID)
5.  📁 File Operations
6.  🔍 Explore Module Attributes (`dir()`)
7.  🌡️ Custom Mathematical Utilities
8.  🚪 Exit

The labels and numbers should match the menu in your actual
`main_menu.py`. If you add or remove a feature, update the menu and this
README together.

### 📅 Date and Time Operations

This section groups date/time functions into one submenu. Depending on
your implementation, it may include displaying date/time information,
working with dates, or measuring elapsed time.

**How to use it:**

1.  Choose the Date and Time option in the main menu.
2.  Read the submenu choices.
3.  Enter the number of the operation you want.
4.  Follow the prompts.
5.  Choose the submenu's return option to go back to the main menu.

⏱️ **Stopwatch note:** A stopwatch should record its start time
immediately when the timing period begins, then record the end time when
the user stops it. The elapsed duration is the difference between those
timestamps.

### 🧮 Mathematical Operations

This section provides a menu for mathematical calculations implemented
in `maths.py`. Available operations depend on the current code.

A useful mathematical menu may include:

-   ➕ Addition
-   ➖ Subtraction
-   ✖️ Multiplication
-   ➗ Division
-   📈 Logarithms
-   🔢 Other calculations implemented in the module

**Example interaction (illustrative):**

``` text
==================================================
       Mathematical Operations
==================================================
Choose an operation: 1
Enter first number: 12
Enter second number: 4
Result: 16
```

The example illustrates the style of a terminal interaction only; your
actual prompts and output may differ.

#### 📈 Logarithms

A logarithm answers the question: "To what power must the base be raised
to produce this number?"

For example, (`\log`{=tex}\_2(8)=3), because (2\^3=8).

A logarithm operation should validate its inputs:

-   The number must be greater than zero.
-   The base must be greater than zero.
-   The base must not equal one.

Invalid values should produce a helpful message instead of an
unexplained traceback.

### 🎲 Random Data Generation

The random section groups utilities that use Python's `random` module.
Your project may include random integers, random choices, password or
OTP generation, dataset sampling, and a small guessing game.

#### 🎯 Random values

A random integer can be useful for demonstrations, games, and test data.
The range and output depend on the selected operation.

#### 🎒 Dataset sampling

Sampling selects a specified number of items from a larger collection,
without selecting the same position more than once. For example,
sampling three names from a list of ten names returns three selected
items.

Before sampling, the program should check that the requested sample size
is at least one and no larger than the dataset.

#### 🎮 Number guessing game

A simple guessing game chooses a secret number and asks the player to
guess it. The program reports whether the guess is correct. You can
expand it with hints, multiple attempts, or a score counter.

#### 🔐 Passwords and OTPs

If your implementation creates sample passwords or one-time codes,
remember that a classroom demonstration is not automatically suitable
for production security. Security-sensitive secrets should use Python's
`secrets` module rather than the ordinary `random` module.

### 🆔 Unique Identifier Generation

The UUID section creates unique identifier strings using Python's `uuid`
module.

A UUID can be useful for:

-   Assigning identifiers to sample records.
-   Naming objects in demonstrations.
-   Creating reference values for test data.
-   Learning how standard-library modules work.

Example output (illustrative):

``` text
Generated UUID: 123e4567-e89b-12d3-a456-426614174000
```

This is an example-shaped UUID, not a promise that the program will
produce that exact value. Each run may produce a different identifier
depending on the UUID function used.

### 📁 File Operations

The file-operations section demonstrates file handling through a custom
module. Depending on what you implemented, it may create, read, append
to, or otherwise work with files.

**Good habits when using file operations:**

-   📍 Know which directory the program is using.
-   💾 Keep backups of important files.
-   🧪 Test with sample files before using valuable data.
-   📝 Use clear filenames and understandable prompts.
-   🛡️ Handle missing files and permission errors gracefully.

If the program writes a file, check the terminal output and the folder
where the script is running to locate the result.

### 🔍 Module Explorer (`dir()`)

The module explorer demonstrates Python introspection. The built-in
`dir()` function returns a list of names associated with an object. For
a module, these names can include functions, classes, constants, and
imported names.

A dynamic explorer can ask for a module name such as `math`, `random`,
`datetime`, or `statistics`, import it, and display its public names.

Example interaction (illustrative):

``` text
Enter module name to explore: math

Available attributes and functions:
ceil
comb
cos
factorial
floor
gcd
log
sqrt
```

The exact names vary with the Python version. Also, `dir()` shows names;
it does not automatically explain how every function works.

⚠️ Only import modules you trust. Importing a module can execute its
top-level code, so do not treat arbitrary module names as harmless input
in an untrusted environment.

### 🌡️ Custom Mathematical Utilities

This feature is intended to demonstrate functions written specifically
for this project rather than relying only on built-in operations.

Depending on your `math_util.py`, the utilities may include:

-   🌡️ Celsius-to-Fahrenheit conversion.
-   ❄️ Fahrenheit-to-Celsius conversion.
-   📈 Logarithm calculation.
-   🔋 Power calculation.

Example conversions:

-   (0\^`\circ `{=tex}C = 32\^`\circ `{=tex}F)
-   (100\^`\circ `{=tex}C = 212\^`\circ `{=tex}F)
-   (32\^`\circ `{=tex}F = 0\^`\circ `{=tex}C)

A conversion utility should accept numeric input and display a clear
result. A logarithm helper should reject non-positive numbers. A power
helper should explain or handle invalid inputs appropriately.

------------------------------------------------------------------------

## 🧩 Understanding Python Modules and Packages

### What is a module?

A Python module is commonly a `.py` file containing definitions and
statements. Functions in that file can be reused by importing the
module.

For example, `maths.py` can hold math-related functions, while
`randomly.py` can hold random-data functions. Keeping them separate
helps readers find and maintain code.

### What is a package?

A package groups related modules inside a directory. In a regular
package, an `__init__.py` file helps identify the directory as a
package.

In this project, `Data/` is intended to be the package containing the
toolkit's feature modules.

### Why use `__init__.py`?

The file can be empty and still serve as the package marker. It can also
contain package initialization code, but that is not necessary for this
beginner-friendly project.

### Why use imports?

Imports allow one file to access definitions from another. This avoids
copying the same function into multiple places and encourages reuse.

Make sure the import style matches your folder structure. For example,
`from Data import math_util` assumes that Python can find the `Data`
package from the current import path.

### Why use `if __name__ == "__main__":`?

Python assigns the special variable `__name__` a value depending on how
a module is run. When a file is executed as the main script, its value
is `"__main__"`.

Using the guard lets a file provide functions for other modules to
import without automatically launching its interactive menu during
import.

A typical pattern is:

``` python
def main():
    print("Welcome to the toolkit")


if __name__ == "__main__":
    main()
```

Use this pattern in the launcher and in standalone modules that need a
direct-execution entry point. Avoid starting interactive loops at import
time.

------------------------------------------------------------------------

## 🛡️ Input Validation and Error Handling

Interactive programs should anticipate mistakes. A user might type
letters where a number is expected, choose an option that does not
exist, enter an invalid logarithm base, or request more sample items
than the dataset contains.

Helpful improvements include:

-   ✅ Check menu choices before dispatching operations.
-   🔢 Catch `ValueError` when converting user input to numbers.
-   ➗ Prevent division by zero.
-   📈 Validate logarithm arguments.
-   🎲 Validate the requested sample size.
-   📁 Handle missing files and permission errors.
-   🔄 Keep the application usable after a recoverable input error.
-   💬 Use simple, friendly error messages.

For a classroom project, implement these checks gradually and test each
one. A clear error message is often more useful than a full traceback
for a beginner using the menu.

------------------------------------------------------------------------

## 🧪 Suggested Manual Test Plan

Use this checklist before submitting the project. Mark each item only
after you have tested it in your own environment.

-   [ ] 🐍 Python starts and the main menu appears.
-   [ ] 📅 Date/time submenu opens successfully.
-   [ ] ↩️ The date/time submenu returns to the main menu.
-   [ ] 🧮 Mathematical submenu opens successfully.
-   [ ] ➕ A normal arithmetic calculation gives the expected result.
-   [ ] ➗ Division by zero is handled appropriately, if division is
    included.
-   [ ] 📈 Logarithm calculation works for valid values.
-   [ ] 🎲 Random-data options run successfully.
-   [ ] 🎒 Dataset sampling returns the requested number of items.
-   [ ] 🎮 Guessing game reports the result correctly.
-   [ ] 🆔 UUID generation produces an identifier.
-   [ ] 📁 File operations work with a test file.
-   [ ] 🔍 Module explorer works with a standard-library module such as
    `math`.
-   [ ] 🌡️ Custom conversion utilities return expected values.
-   [ ] 🚪 The exit option terminates the application.
-   [ ] 📦 `Data/__init__.py` exists.
-   [ ] 🧭 Imports work from the documented launch location.
-   [ ] 🧹 Temporary Python cache files are excluded from the final ZIP.

------------------------------------------------------------------------

## 🧯 Troubleshooting

### ❓ The main menu does not reappear after a submenu

Check the submenu's return option. A `break` statement exits the nearest
loop; it does not automatically exit a function or call the main menu.
If the submenu is inside a function, `return` is often the right way to
finish that function so the main menu's loop can continue.

Also check that the submenu's `while` loop and the main menu's `while`
loop are correctly indented.

### ❓ `ModuleNotFoundError` appears

Possible causes:

-   The terminal is in the wrong working directory.
-   The folder or filename differs from the import statement.
-   The package folder is not where Python expects it.
-   The project mixes top-level imports and package imports.

Open the project root and compare every import with the actual
filenames. On systems with case-sensitive filenames, capitalization
matters.

### ❓ `ImportError` appears for the custom math utility

Check whether the file is named `math_util.py` or `math_utils.py`. Those
are different names. The import must match the filename.

For example, `from Data import math_util` expects a module called
`math_util.py` inside `Data/`.

### ❓ The menu crashes when I type letters

If a menu uses `int(input(...))`, entering non-numeric text raises
`ValueError`. Add input validation or a `try/except` block around the
conversion.

### ❓ The module explorer says a module was not found

Check the spelling of the module name. Standard-library module names are
usually typed without the `.py` suffix. A module may also be unavailable
if it is third-party and not installed in the current Python
environment.

### ❓ The file-operation output is hard to find

Relative paths are resolved from the process's current working
directory, which may differ from the folder containing a source file.
Print or inspect the current working directory while debugging, and use
a known test folder.

### ❓ Python cache folders appear

Python may create `__pycache__/` directories and `.pyc` files while
running modules. These are generated cache files, not the main source
code. They normally do not need to be included in a source-project ZIP.

------------------------------------------------------------------------

## 🧹 Preparing a Clean Submission

Before creating your final ZIP:

1.  💾 Save all source files.
2.  🧪 Run the project and test each menu option.
3.  📦 Confirm `Data/__init__.py` is present.
4.  📖 Update this README so its filenames and options match your final
    project.
5.  🧹 Remove `__pycache__/` directories and `.pyc` files from the
    submission copy.
6.  🚫 Do not include virtual environments, editor caches, or unrelated
    temporary files.
7.  🗜️ Create the ZIP with the project folder and its source files.
8.  🔍 Open the ZIP and verify that the expected files are present.

You do not need to prevent Python from generating cache files during
normal execution; just exclude them from the submitted source archive.

------------------------------------------------------------------------

## 📚 Learning Outcomes

By completing and testing this project, you can practise:

-   🐍 Writing and calling Python functions.
-   📦 Creating a package with `__init__.py`.
-   🔗 Importing custom modules.
-   🧭 Organizing a multi-file Python application.
-   🔁 Building menu-driven programs.
-   🧮 Performing arithmetic and mathematical calculations.
-   🎲 Using random data for sampling and simple games.
-   🆔 Generating UUID values.
-   📁 Performing basic file operations.
-   🔎 Exploring modules using `dir()` and `importlib`.
-   🛡️ Validating input and handling common errors.
-   🧹 Preparing a clean source-code submission.

------------------------------------------------------------------------

## 🌈 Future Improvements

This toolkit can grow as your Python skills improve. Some ideas for
future versions:

-   🎨 Add a more colourful terminal interface.
-   🧪 Add automated unit tests for individual functions.
-   🧾 Add logging for errors and debugging.
-   🗂️ Move repeated menu code into reusable helper functions.
-   🛡️ Improve validation for every numeric input.
-   🔐 Use secure randomness for security-sensitive tokens.
-   📊 Add statistics such as mean, median, and standard deviation.
-   🧮 Add more scientific calculations.
-   📄 Add a sample data file for file-operation demonstrations.
-   🌐 Add localization or multiple-language prompts.
-   🧭 Add a help option that explains each menu feature.
-   📦 Package the project for easier installation after the source
    layout is stable.

------------------------------------------------------------------------

## 🤝 Contribution Guidelines

If you want to extend the project:

1.  🌱 Make one small change at a time.
2.  🧩 Keep each module focused on a clear responsibility.
3.  📝 Use descriptive function and variable names.
4.  💬 Write comments where they clarify non-obvious logic.
5.  🧪 Test the changed operation and its return path.
6.  📖 Update the README when a feature or command changes.
7.  🧹 Keep generated files out of the source archive.

For a student project, the best improvement is not necessarily adding
the most code. It is making each feature understandable, reliable, and
easy to demonstrate.

------------------------------------------------------------------------

## 💖 A Note for Learners

Programming is a process of building, testing, discovering mistakes, and
improving the solution. If a menu does not return properly or an import
fails, use the error message and the program flow to identify the
problem. Fix one issue at a time, then test again.

Every module you understand is another tool in your Python toolbox. Keep
experimenting, stay curious, and enjoy building! 🚀🐍

------------------------------------------------------------------------

## 📄 Project Information

-   **Project name:** Multi-Utility Toolkit
-   **Language:** Python 3
-   **Interface:** Terminal-based, menu-driven
-   **Organization:** Multiple Python modules with a custom package
-   **Primary purpose:** Practice modular programming and
    standard-library utilities
-   **Status:** Educational project; available operations depend on the
    implementation in the submitted source files

------------------------------------------------------------------------

## 🏁 Final Checklist

Before you submit, confirm:

-   [ ] The README matches the real code.
-   [ ] All listed modules exist.
-   [ ] The launcher runs from the documented directory.
-   [ ] Every menu option has a corresponding implementation.
-   [ ] Every submenu can return to the main menu.
-   [ ] The custom package includes `__init__.py`.
-   [ ] The custom math utility import matches its filename.
-   [ ] The `__main__` guard is used where appropriate.
-   [ ] The logarithm operation is present if required.
-   [ ] Random sampling and the game are implemented if listed.
-   [ ] Module exploration accepts a module name.
-   [ ] Cache files are excluded from the ZIP.
-   [ ] The final ZIP opens and contains the expected source files.
---

Explanation video: https://drive.google.com/file/d/16t-dO39Plo_GsJiFjYrb5WAuMD37dlXE/view?usp=drivesdk

---
### 🌟 Thank you for exploring Multi-Utility Toolkit!

---

🤝 Let's Connect I'd love to connect with fellow learners, developers, and Python enthusiasts! 💙

💼 LinkedIn 🔗 http://www.linkedin.com/in/jiya-kosambiya-86306141b

📧 Email ✉️ jiyakosambiya75@gmail.com
👩‍💻 Author

--- 

Jiya Kosmbiya

B.Sc. IT with AI & ML Specialization
**Keep coding. Keep learning. Keep creating.** 💻✨🐍
