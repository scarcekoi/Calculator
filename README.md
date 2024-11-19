# 🧮 **Advanced Calculator App**

A sleek, interactive **Calculator App** built with **Python** using the **CustomTkinter** library. This app supports a variety of mathematical operations with **real-time results** and **dynamic input fields**. With automatic formatting, **commas for large numbers**, and the ability to remove trailing zeros for decimal numbers, this app is both powerful and user-friendly!

---

## 📐 **Features**:
- **Real-Time Calculation**: Instant results as you type, no need to click a "Calculate" button!
- **Dynamic Input Fields**: Only the relevant input fields are shown based on the selected calculation type.
- **Flexible Result Formatting**: 
  - **Commas** for large numbers (e.g., `1,000,000`).
  - **Precision** of up to **10 decimal places**, with automatic removal of unnecessary trailing zeros (e.g., `4.0` becomes `4` and `3.1400000000` becomes `3.14`).
- **Large Number Scales**: Displays the scale of large numbers like **Million**, **Billion**, **Trillion**, and up to **Quattuordecillion**.
- **Decimal Scales**: Displays the decimal scale such as **Tenth**, **Hundredth**, **Thousandth**, and so on.
- **Error Handling**: Clear error messages for invalid input or mathematical errors (e.g., **Division by Zero**).
- **Interactive UI**: Built using **CustomTkinter**, providing a visually appealing interface.

---

## 🧑‍💻 **Available Calculations**:
1. **Area**: Calculate the area of a rectangle (length × width).
2. **Circle Area**: Calculate the area of a circle (π × radius²).
3. **Circumference**: Calculate the circumference of a circle (2 × π × radius).
4. **Fraction**: Calculate the result of a division (numerator / denominator).
5. **Perimeter**: Calculate the perimeter of a rectangle (2 × (length + width)).
6. **Volume**: Calculate the volume of a rectangular prism (length × width × height).
7. **Radius**: Calculate the radius of a circle from its diameter (diameter / 2).

---

## ⚙️ **How to Use**:

1. **Select the Calculation Type**: From the dropdown menu, choose the type of calculation you want to perform (e.g., Area, Circle Area, Fraction, etc.).
2. **Enter the Required Values**: The input fields will automatically appear based on your selection. Enter the required values.
3. **View the Result**: As you type, the result will be automatically updated and formatted in real time.
   - For example, entering `4` as a radius for a circle will display the result as `Area: 50.2654824574`, but entering `4.0000` will show `Area: 50.2654824574` (without extra zeros).

---

## 📸 **Screenshots**:

**Interactive UI** that updates instantly with user input.

![Calculator App Screenshot](assets/calc_scrnsht1.png)

---

## 🛠 **Installation & Setup**:

### Prerequisites:
- **Python 3.8+** installed. You can download Python from the official website: [python.org](https://www.python.org/downloads/).
- **CustomTkinter** library for the GUI:

### Step 1: Install CustomTkinter

To install the **CustomTkinter** library, run the following command in your terminal or command prompt:

```bash
pip install customtkinter
```

### Step 2: Clone the Repository

Clone this repository to your local machine using:

```bash
git clone https://github.com/scarcekoi/Calculator
```

### Step 3: Run the Application

Navigate to the directory where the project was cloned and run the Python file:

```bash
cd Calculator
python main.py
```

## 🔧 **Customization**:

If you want to modify the app, such as adding new features or changing the design, open the `main.py` file in your preferred text editor (e.g., VSCode, Sublime Text, PyCharm).

You can easily add more mathematical operations by adding new calculation functions and adding them to the dropdown menu.

---

## 📝 **Contributing**:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push to the branch.
6. Create a new Pull Request.

---

## 📄 **License**:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
