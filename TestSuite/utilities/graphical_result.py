import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import os

def graphical_result(path_to_xml_file):
    # Parse the pytest output XML file
    tree = ET.parse(path_to_xml_file)
    root = tree.getroot()

    # Extract the test results data
    test_results = []
    for test in root.iter('testcase'):
        test_name = test.attrib['classname'] + '.' + test.attrib['name']
        test_time = float(test.attrib['time'])
        test_result = 'pass'
        for failure in test.iter('failure'):
            test_result = 'fail'
        test_results.append((test_name, test_time, test_result))

    # Separate the pass and fail results
    pass_results = [result for result in test_results if result[2] == 'pass']
    fail_results = [result for result in test_results if result[2] == 'fail']

    # Create a bar chart of the test results
    plt.bar([result[0] for result in pass_results], [result[1] for result in pass_results], color='green')
    plt.bar([result[0] for result in fail_results], [result[1] for result in fail_results], color='red')

    plt.xticks(rotation=90)
    plt.xlabel('Test Name')
    plt.ylabel('Test Execution Time (seconds)')
    plt.title('Pytest Test Results')
    plt.legend(['Pass', 'Fail'])
    path = os.getcwd()
    plt.savefig(path+"/reports/output.png")

