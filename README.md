# 🧮 **Advanced Calculator App**

A sleek, interactive **Calculator App** built with **Python** using the **CustomTkinter** library. This app supports a variety of mathematical operations with **real-time results** and **dynamic input fields**. With automatic formatting, **commas for large numbers**, and the ability to remove trailing zeros for decimal numbers, this app is both powerful and user-friendly!

---

## 📐 **Features**:
- **Real-Time Calculation**: Instant results as you type, no need to click a "Calculate" button!
- **Dynamic Input Fields**: Only the relevant input fields are shown based on the selected calculation type.
- **Flexible Result Formatting**: 
  - **Commas** for large numbers (e.g., `1,000,000`).
  - **Precision** of up to **10 decimal places**, with automatic removal of unnecessary trailing zeros (e.g., `4.0` becomes `4` and `3.1400000000` becomes `3.14`).
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
3. **View the Result**: As you type, the result will be automatically updated and formatted in real-time.
   - For example, entering `4` as a radius for a circle will display the result as `Area: 50.2654824574`, but entering `4.0000` will show `Area: 50.2654824574` (without extra zeros).

---

## 📸 **Screenshots**:

**Interactive UI** that updates instantly with user input.

![Calculator App Screenshot](assets/calculator_screenshot.png)

---

## 🛠 **Installation & Setup**:

### Prerequisites:
- Python 3.8+ installed.
- **CustomTkinter** library for the GUI:
  
  Install CustomTkinter via pip:

  ```bash
  pip install customtkinter
