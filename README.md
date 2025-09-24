# 🧲 Magnetic Moment Calculator

A Python script to calculate the magnetic moment of iron atoms based on physical and derived constants. The project calculates the magnetic moment of iron under high pressure conditions, based on the theoretical framework from Savić and Kašanin (1965). It includes computations for critical density, energy phases, ionization thresholds, and magnetic moment estimations relevant to celestial body materials. An example calculation demonstrates iron's contribution to the magnetic field of the Hoba meteorite.

 This includes:

- Critical density calculation  
- Radius of action and energy derivation  
- Energy phase generation  
- Ionization threshold checks for electron shells  
- Estimation of the element's contribution to the magnetic moment of a celestial body  

---

## 📦 Features

- Based on established physical and derived constants  
- Ionization checks for K, L, M, and N electron shells  
- Generates energy phase table (`i = 1 to 14`)  
- Calculates magnetic moment for a selected phase  
- Well-commented and modular code  
- Ready for educational or research extension  

---

## 🧮 Example Output


 i |   Energy (eV) |  Magnetic Moment (μB)
------------------------------------------
 1 |       7.9483  |              1.0000
 2 |      10.0144  |              1.2600
...
14 |     160.2325  |             20.1505

---


## 🚀 Getting Started

### 🔧 Requirements

- Python 3.7+
- [SciPy](https://www.scipy.org/) (for physical constants)


Install requirements via:

```bash
pip install -r requirements.txt
pip install scipy
```

## 📁 Project Structure

    magnetic-moment-calculator/
    ├── main.py     # Main script
    ├── README.md              # Project documentation
    ├── requirements.txt       # Dependencies
    └── LICENSE                # (Optional) Open source license

 Run the script via:

 ```bash
 python main.py
```

## 📚 Reference

Note: Some physical constants used in this script are derived or adapted from:  
Savić, P., & Kašanin, R. (1965). *The Behaviour of the Materials under High Pressures*.  
Serbian Academy of Sciences and Arts, Monographs IV, Belgrade.

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the issues page or contact [violeta@vin.bg.ac.rs].

