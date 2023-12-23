# VendorManagementSystem
The Vendor Management System is a Django Rest Framework (DRF) project designed to efficiently manage vendors. It provides a RESTful API for handling various aspects of vendor-related operations. This system can be utilized to streamline vendor information, monitor performance metrics, and enhance communication with vendors.

# Features
- **Vendor CRUD Operations**: Create, Read, Update, and Delete vendor information.
- **Performance Metrics**: Calculate and track vendor performance metrics such as on-time delivery rate, quality rating average, average response time, and fulfillment rate.
- **Historical Performance**: Optionally store historical performance data for analysis and reporting.
- **Flexible API**: Utilize the power of Django Rest Framework for easy integration with front-end applications or third-party services.

## Getting Started

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Jeniffer1411/VendorManagementSystem/
    cd VendorManagementSystem
    ```
2. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```
3. **Run Migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
4. **Create Superuser (Optional)**:
    
    ```bash
    python manage.py createsuperuser
    ```
    to access django admin page

5. **Run the Development Server**:

    ```bash
    python manage.py runserver
    ```
    
6. **Access the API**:

    - Open your browser and go to [http://localhost:8000/api/](http://localhost:8000/api/) to explore the API.
    - Access the Django admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/) to manage vendors and other data.
  
7. **Run Automated TestSuite**:

  ```bash
  cd TestSuite
  python -m pytest
  ```
  To run test suites for Vendor and Purchase order API test

  # Automated Test Suite Features

  Our automated test suite for the Vendor Management System offers a range of features to ensure the reliability and stability of the application. Here are some key features:
  
  1. **Comprehensive Test Coverage**:
  
  Our test suite covers a wide range of functionalities within the Vendor Management System, including CRUD operations, performance metrics calculations, and any critical business logic. This comprehensive coverage helps identify and prevent regressions.
  
  2. **Pytest Integration**:
  
  The test suite is built on the Pytest framework, a popular testing tool in the Python ecosystem. Pytest provides a simple syntax for writing tests, powerful fixtures, and clear output reporting.
  
  3. **Easily Extensible**:
  
  Contributors can easily extend the test suite to cover new features or modifications to existing functionality. The modular structure allows the addition of new test cases without significant effort.
  
  5. **Test Data Management**:
  
  Our test suite includes strategies for managing test data, ensuring that tests run consistently and without dependencies on external factors. This helps maintain a stable testing environment.

  6. **Test Suite Data Files**:

  Inside the `TestSuite` directory, you'll find a `TestData` folder dedicated to storing test data in specified CSV files. This organized structure allows you to efficiently manage and update test data, making it easy to send sets of responses in just one click. By utilizing CSV files, you can maintain a clear and structured representation of the data used in your tests.
  
 7. **Test Reports**:
  After each test run, our test suite generates comprehensive reports to provide valuable insights into the test results. These reports include detailed information on both passed and failed tests, code coverage metrics, and any encountered errors.
  
  You can access the reports in multiple formats, including:
  
  - **HTML Reports:** Detailed and interactive HTML reports for easy visualization.
  - **XML Reports:** Structured XML reports suitable for integration with other tools.
  - **Graphical Reports:** Visual representations to quickly identify trends and patterns.
  
  All reports are conveniently stored in the `TestSuite/Reports` folder, allowing you to review and analyze the test outcomes efficiently.
    
  ---

  # Screen Shots
  ![image](https://github.com/Jeniffer1411/VendorManagementSystem/assets/154697190/22b8cd06-2501-451c-87d7-2e8fe931f736)

  ![image](https://github.com/Jeniffer1411/VendorManagementSystem/assets/154697190/8f5517aa-3c44-4b82-93ef-093071345dcd)

  ![image](https://github.com/Jeniffer1411/VendorManagementSystem/assets/154697190/033b509c-186e-457b-893e-17aea6f19409)

  ![image](https://github.com/Jeniffer1411/VendorManagementSystem/assets/154697190/679334cf-864e-4696-91d6-d82388b6c4bf)


  



