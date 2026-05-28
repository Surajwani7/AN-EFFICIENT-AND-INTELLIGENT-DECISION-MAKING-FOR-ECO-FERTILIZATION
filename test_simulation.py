#!/usr/bin/env python3
"""
Test Simulation Script for ECO-FERTILIZATION
This script simulates the application workflow without running the Flask server.
Run this to test if all dependencies are installed and the core logic works.
"""

import sys
import os

# Add the Code/app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Code', 'app'))

print("=" * 80)
print("ECO-FERTILIZATION - APPLICATION TEST SIMULATION")
print("=" * 80)
print()

# Test 1: Check if required files exist
print("[TEST 1] Checking for required CSV files...")
required_files = [
    'Code/app/Nutrient_recommendation.csv',
    'Code/app/mapped_crops.csv'
]

for file_path in required_files:
    if os.path.exists(file_path):
        print(f"  ✓ {file_path} - FOUND")
    else:
        print(f"  ✗ {file_path} - NOT FOUND")

print()

# Test 2: Check if required modules can be imported
print("[TEST 2] Checking Python dependencies...")
dependencies = {
    'flask': 'Flask web framework',
    'requests': 'HTTP requests library',
    'pandas': 'Data manipulation',
    'sklearn': 'Scikit-learn (Machine Learning)',
    'category_encoders': 'Category Encoder'
}

missing_deps = []
for module, description in dependencies.items():
    try:
        __import__(module)
        print(f"  ✓ {module} - INSTALLED ({description})")
    except ImportError:
        print(f"  ✗ {module} - MISSING ({description})")
        missing_deps.append(module)

print()

if missing_deps:
    print("[ALERT] Missing dependencies detected!")
    print("Install them with:")
    print(f"  pip install {' '.join(missing_deps)}")
    print()
else:
    print("[SUCCESS] All dependencies are installed!")
    print()

# Test 3: Test the modules
print("[TEST 3] Testing application modules...")
try:
    os.chdir('Code/app')
    from BestTimeToFertilizeModule import BestTimeToFertilize
    print("  ✓ BestTimeToFertilizeModule imported successfully")
except Exception as e:
    print(f"  ✗ BestTimeToFertilizeModule import failed: {e}")

try:
    from NPKEstimatorModule import NPKEstimator
    print("  ✓ NPKEstimatorModule imported successfully")
except Exception as e:
    print(f"  ✗ NPKEstimatorModule import failed: {e}")

try:
    from flask import Flask
    app = Flask(__name__)
    print("  ✓ Flask app initialization successful")
except Exception as e:
    print(f"  ✗ Flask app initialization failed: {e}")

print()

# Test 4: Simulate API call (without making actual request)
print("[TEST 4] Simulating weather API initialization...")
try:
    bttf = BestTimeToFertilize(city_name='Bangalore', state_name='Karnataka')
    print(f"  ✓ BestTimeToFertilize object created")
    print(f"    - City: {bttf.city_name}")
    print(f"    - State: {bttf.state_name}")
    print(f"    - Country: {bttf.country_name}")
    print(f"    - Days: {bttf.days}")
except Exception as e:
    print(f"  ✗ BestTimeToFertilize initialization failed: {e}")

print()

# Test 5: Test NPK Estimator
print("[TEST 5] Testing NPK Estimator initialization...")
try:
    est = NPKEstimator(data='Nutrient_recommendation.csv')
    print("  ✓ NPKEstimator object created")
    print(f"    - Data shape: {est.df.shape}")
    est.renameCol()
    print(f"    - Columns renamed: {list(est.df.columns)}")
except Exception as e:
    print(f"  ✗ NPKEstimator initialization failed: {e}")

print()

# Final summary
print("=" * 80)
print("TEST SIMULATION COMPLETE")
print("=" * 80)
print()
print("TO RUN THE FULL APPLICATION:")
print("  1. Install all missing dependencies (if any)")
print("  2. cd Code/app")
print("  3. python app.py")
print("  4. Open http://localhost:5000 in your browser")
print()
