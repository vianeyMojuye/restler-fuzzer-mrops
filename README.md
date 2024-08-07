# Restler-Fuzzer-MROPS

## Overview
Restler-Fuzzer-MROPS is a customized version of the RESTLER fuzzer, specifically designed to enhance its functionality with Metamorphic Relations. This project aims to improve the detection of both functional and non-functional bugs in REST APIs by leveraging metamorphic testing techniques.

## Fork Information
This project is a fork of the main [RESTLER](https://github.com/microsoft/restler-fuzzer) project. All the contributions and enhancements made are available in the `mrops` branch.

## Key Contributions in the MROPS Branch
The `mrops` branch includes the following key contributions:

1. **MROPEquivalence Checker**:
   - Verifies that different sequences of API calls that should logically produce the same outcome do indeed produce equivalent responses.
   - Ensures consistent behavior across repeated operations, equivalent inputs, and resource isolation.

2. **MROPDisjoint Checker**:
   - Ensures that operations on distinct resources are independent and do not interfere with each other.
   - Confirms that changes to one resource do not unintentionally affect another resource.

3. **MROPEquality Checker**:
   - Verifies the consistency of outputs from repeated identical inputs.
   - Ensures that repeated API calls with the same parameters produce the same results, confirming the stability and reliability of the API.

4. **MROPTimePerformance Checker**:
   - Focuses on the non-functional aspect of API performance.
   - Compares the execution times of different requests to identify performance regressions or unexpected delays.

5. **Bug Detection Enhancements**:
   - Cross-data contamination detection: Identifies cases where data from one resource contaminates another.
   - Error in equivalent sequences: Detects improper handling of sequences like POST-DELETE and POST-PUT.
   - Data consistency checks: Ensures that  requests with the same data result in consistent states.
6. **Output**: 
   - The outputs folder Provides detailed reports on the detected bugs.

## Installation
To use Restler-Fuzzer-MROPS, follow these steps:

1. Clone the repository and switch to the `mrops` branch:
   ```sh
   https://github.com/vianeyMojuye/restler-fuzzer-mrops.git
   cd restler-fuzzer-mrops
   git checkout mrops
2. Install the required dependencies using pip:
   ```sh
   pip install -r requirements.txt
3. Run the fuzzer with the following command:
   ```sh
   python restler.py --grammar <path_to_grammar> --test_engine <path_to_test_engine>
   ```
   Replace `<path_to_grammar>` with the path to the grammar file and `<path_to_test_engine>` with the path to the test engine settings file.

## Usage
Follow the steps described in the link below to use the fuzzer with the grammar file and test engine settings file: 
https://github.com/vianeyMojuye/restler-fuzzer-mrops/tree/main
